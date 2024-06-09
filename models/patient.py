from odoo import models, fields, api

class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient'

    name = fields.Char(string='Name', required=True)
    
    age = fields.Integer(string='Age')
    
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    
    date_of_birth = fields.Date(string='Date of Birth')
    
    address = fields.Text(string='Address')

    image = fields.Binary(string='Image')
    
    blood_type = fields.Selection([
    ('A+', 'A+'),
    ('B+', 'B+'),
    ('AB+', 'AB+'),
    ], string='Blood_Type')
    
    cr = fields.Float(string='CR_Ratio', default=None)
    pcr = fields.Boolean(string='pcr')
    
    history = fields.Html('History')
    
    department_id = fields.Many2one('hms.department')
    department_capacity = fields.Integer(related= 'department_id.capacity', store=True)
    
    doctors_ids =  fields.Many2many('hms.doctor')
    
    states = fields.Selection([
        ('Undetermined', 'Undetermined'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Serious', 'Serious') 
    ])
    
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