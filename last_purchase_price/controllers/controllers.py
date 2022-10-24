# -*- coding: utf-8 -*-
# from odoo import http


# class ./lastPurchasePrice(http.Controller):
#     @http.route('/./last_purchase_price/./last_purchase_price', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./last_purchase_price/./last_purchase_price/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('./last_purchase_price.listing', {
#             'root': '/./last_purchase_price/./last_purchase_price',
#             'objects': http.request.env['./last_purchase_price../last_purchase_price'].search([]),
#         })

#     @http.route('/./last_purchase_price/./last_purchase_price/objects/<model("./last_purchase_price../last_purchase_price"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./last_purchase_price.object', {
#             'object': obj
#         })
