from odoo import http
from odoo.http import request

class MyController(odoo.http.Controller):
    @route('/dozhiurl', auth='public')
    def handler(self):
        return stuff()