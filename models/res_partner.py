from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
  _inherit = 'res.partner'

  related_patient_id = fields.Many2one('hms.patient')
  
  _sql_constraints = [
    ('unique_patient_email', 'unique("related_patient_id")', 'A petient with that email is already linked to another customer'),
    ('required_customer_tax_id', 'CHECK(vat IS NOT NULL)', 'A tax ID is required for the customer.')
  ]
  