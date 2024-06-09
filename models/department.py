from odoo import models, fields, api

class Department(models.Model):
    _name = 'hms.department'
    _description = 'Department'

    name = fields.Char(string='Name', required=True)
    is_opened = fields.Boolean(string='is_opened')
    capacity = fields.Integer(string='Capacity')
    
    # patients
    patients_ids = fields.One2many('hms.patient' , 'department_id')
   
    # doctors
    doctors_ids = fields.One2many('hms.doctor' , 'department_id')
    