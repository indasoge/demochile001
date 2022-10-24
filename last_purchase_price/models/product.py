# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'


    last_purchase_price = fields.Float(string='Last Purchase Cost',compute='_compute_last_purchase_price',
        inverse='_set_last_purchase_cost', search='_search_last_purchase_price',
        digits='Product Price', groups="base.group_user",
        help= """Shows the price of last purchase""")

    last_purchase_date = fields.Date(string='Last Purchase Date', tracking=True)

    def _set_last_purchase_cost(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.last_purchase_price = template.last_purchase_price
    
    def _compute_last_purchase_price(self):
        # Depends on force_company context because standard_price is company_dependent
        # on the product_product
        unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
        for template in unique_variants:
            template.last_purchase_price = template.product_variant_ids.last_purchase_price
        for template in (self - unique_variants):
            template.last_purchase_price = 0.0

    
    def _search_last_purchase_price(self, operator, value):
        products = self.env['product.product'].search([('last_purchase_price', operator, value)], limit=None)
        return [('id', 'in', products.mapped('product_tmpl_id').ids)]

    
class ProductProduct(models.Model):
    _name = 'product.product'
    _inherit = 'product.product'

    
    last_purchase_price = fields.Float(string='Last Purchase Cost',
        company_dependent=True,
        digits='Product Price', groups="base.group_user",
        help= """Shows the price of last purchase""")

    last_purchase_date = fields.Date(string='Last Purchase Date', 
        company_dependent=True,
         tracking=True)
       

