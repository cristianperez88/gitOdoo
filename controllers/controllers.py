# -*- coding: utf-8 -*-
# from odoo import http


# class GitOdoo(http.Controller):
#     @http.route('/git_odoo/git_odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/git_odoo/git_odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('git_odoo.listing', {
#             'root': '/git_odoo/git_odoo',
#             'objects': http.request.env['git_odoo.git_odoo'].search([]),
#         })

#     @http.route('/git_odoo/git_odoo/objects/<model("git_odoo.git_odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('git_odoo.object', {
#             'object': obj
#         })

