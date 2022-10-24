from odoo import api, fields, models

CATEGORY_SELECTION = [
    ('required', 'Requerido'),
    ('optional', 'Opcional'),
    ('no', 'Ninguno')]

class ApprovalCategory(models.Model):
    _inherit = 'approval.category'
    _description = 'Approval Category Inherit'    

    ext_payment_flag = fields.Boolean(string='Es Pago Externo')

    has_defined_hours = fields.Selection(CATEGORY_SELECTION, string="Horas Pactadas", default="no", required=True)
    has_worked_hours = fields.Selection(CATEGORY_SELECTION, string="Horas Trabajadas", default="no", required=True)
    has_extra_hours = fields.Selection(CATEGORY_SELECTION, string="Horas Extra", default="no", required=True)

    asigned_employee = fields.Many2one(comodel_name='hr.employee', string='Talento')

    
    
