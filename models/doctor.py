from odoo import models, fields

class Doctor(models.Model):
    _name = 'hms.doctor'
    _description = 'Doctor'

    first_name = fields.Char(string='first_name', required=True)
    last_name = fields.Char(string='last_name', required=True)
    image = fields.Binary(string='Image')
    
    department_id = fields.Many2one('hms.department')
    
    # patients_ids =  fields.Many2many('hms.patient')
    