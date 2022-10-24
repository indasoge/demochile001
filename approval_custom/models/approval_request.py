from odoo import api, fields, models

class ApprovalRequest(models.Model):
    _inherit = 'approval.request'
    _description = 'Approval Request Inherit'
       
    # ext_payment_flag = fields.Selection(related="category_id.ext_payment_flag")

    has_defined_hours = fields.Selection(related="category_id.has_defined_hours")
    has_worked_hours = fields.Selection(related="category_id.has_worked_hours")
    has_extra_hours = fields.Selection(related="category_id.has_extra_hours")

    #asigned_employee = fields.Selection(related="category_id.asigned_employee")

    defined_hours = fields.Integer(string='Horas Pactadas')
    worked_hours = fields.Integer(string='Horas Trabajadas')
    extra_hours = fields.Integer(string='Horas Extra')
    
    