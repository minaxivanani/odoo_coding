# -*- coding: utf-8 -*-
# from odoo import http


# class Estate.account(http.Controller):
#     @http.route('/estate.account/estate.account/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estate.account/estate.account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('estate.account.listing', {
#             'root': '/estate.account/estate.account',
#             'objects': http.request.env['estate.account.estate.account'].search([]),
#         })

#     @http.route('/estate.account/estate.account/objects/<model("estate.account.estate.account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estate.account.object', {
#             'object': obj
#         })
