from odoo import api, fields, models, _
import requests
import json

class ResCountryState(models.Model):
    _inherit = 'res.country.state'

    source_id = fields.Integer(string="GHN mã tỉnh/TP", help='Mã tỉnh/TP theo Giao hàng Nhanh')

    def fetch_all_province_id(self):
        request_url = "https://online-gateway.ghn.vn/shiip/public-api/master-data/province"
        ghn_token = self.env['ir.config_parameter'].sudo().get_param('ghn_token')
        headers = {
            'Content-type': 'application/json',
            'Token': ghn_token
        }
        req = requests.get(request_url, headers=headers)
        req.raise_for_status()
        content = req.json()
        print(content)
        data = content['data']
        for rec in data:
            existed_state = self.env['res.country.state'].sudo().search([('name', 'ilike', rec['ProvinceName'])])
            if existed_state:
                for e in existed_state:
                    e.sudo().write({
                        'source_id': rec['ProvinceID']
                    })
        return content


