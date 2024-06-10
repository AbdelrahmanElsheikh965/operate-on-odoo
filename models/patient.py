from odoo import models, fields, api
from datetime import datetime

class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient'
    _inherit = ['mail.thread']
    
    name = fields.Char(string='Name', required=True, tracking=True)
    
    age = fields.Integer(string='Age', tracking=True)
    
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', tracking=True)
    
    date_of_birth = fields.Date(string='Date of Birth', tracking=True)
    
    address = fields.Text(string='Address', tracking=True)

    image = fields.Binary(string='Image', tracking=True)
    
    blood_type = fields.Selection([
    ('A+', 'A+'),
    ('B+', 'B+'),
    ('AB+', 'AB+'),
    ], string='Blood_Type', tracking=True)
    
    cr = fields.Float(string='CR_Ratio', default=None, tracking=True)
    pcr = fields.Boolean(string='pcr', tracking=True)
    
    history = fields.Html('History')
    
    department_id = fields.Many2one('hms.department', tracking=True)
    department_capacity = fields.Integer(related= 'department_id.capacity', store=True)
    
    doctors_ids =  fields.Many2many('hms.doctor')
    
    states = fields.Selection([
        ('Undetermined', 'Undetermined'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Serious', 'Serious') 
    ], tracking=True)
    
    department_is_opened = fields.Boolean(string='Department Is Opened', related='department_id.is_opened')

    # ➢The history field should be hidden if the age is less than 50
    @api.depends('age')
    def _compute_is_hidden(self):
        for record in self:
            record.is_hidden = record.age < 50

    # ➢The PCR field should be automatically checked if the age is < 30 show a warning message that it has been checked            
    @api.onchange('age')
    def _onchange_age(self):
        if self.age and self.age < 30:
            return {
                'warning': {
                    'title': "Warning",
                    'message': "It has been checked!",
                }
            }
            
    # ➢ The patient can't choose a closed department
    @api.onchange('department_id')
    def _onchange_department_id(self):
        return {'domain': {'department_id': [('is_opened', '=', True)]}}
    
    # @api.onchange('department_id')
    # def get_employees(self):
    #     if self.department_id:
    #         domain = [('department_id', '=', self.department_id.id), ('department_id.is_opened', '=', True)]
    #     else:
    #         domain = []
    #     return {'domain': {'department_id': domain}}
    
    
    # ➢ If The pcr field is checked, the CR ratio field should be mandatory
    # <field name="cr" modifiers="{'required': [('pcr', '=', True)]}"/>