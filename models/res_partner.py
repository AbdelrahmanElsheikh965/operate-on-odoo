from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
  _inherit = 'res.partner'

  related_patient_id = fields.Many2one('hms.patient')

  @api.constrains('related_patient_id', 'email')
  def _check_unique_email(self):
      for record in self:
          if record.related_patient_id and record.email:
              partners = self.search([
                  ('email', '=', record.email),
                  ('id', '!=', record.id),
                  ('related_patient_id', '!=', False)
              ])
              if partners:
                  raise ValidationError("A patient with this email is already linked to a different customer.")