from odoo import api, fields, models, _
import requests
import json

class ResWard(models.Model):
    _name = 'res.ward'
    _description = 'Res Ward'
    _order = 'state_id'

    name = fields.Char("Name", required=True, translate=True)
    country_id = fields.Many2one('res.country', string='Country', required=True)
    state_id = fields.Many2one('res.country.state', 'State', domain="[('country_id', '=', country_id)]")
    district_id = fields.Many2one('res.district', 'District', domain="[('state_id', '=', state_id)]")
    ghn_ward_id = fields.Char("GHN Ward Code", help='Mã phường/xã theo Giao hàng Nhanh')
    acu_cd = fields.Char(string='Acu code', help='Mã phường/xã theo Acumatica')

    def create_ward_data(self):
        all_district = self.env['res.district'].sudo().search([('source_id', '>', 0)])
        i = 1
        
        for dis in all_district:
            request_url = "https://online-gateway.ghn.vn/shiip/public-api/master-data/ward?district_id="+str(dis.source_id)
            ghn_token = self.env['ir.config_parameter'].sudo().get_param('ghn_token')
            headers = {
                'Content-type': 'application/json',
                'Token': ghn_token
            }
            req = requests.get(request_url, headers=headers)
            req.raise_for_status()
            content = req.json()    
            data = content['data']
            print(request_url)
            print(i)
            if data is None:
                print('Error --------')
                continue
            
            for rec in data:
                existed_district = self.env['res.district'].sudo().search([('source_id', '=', rec['DistrictID'])],limit=1)
                if existed_district:
                    vals = {}
                    vals['state_id'] = existed_district.state_id.id
                    vals['country_id'] = existed_district.country_id.id
                    vals['district_id'] = existed_district.id
                    vals['name'] = rec['WardName']
                    vals['ghn_ward_id'] = rec['WardCode']
                    i += 1
                    self.env['res.ward'].sudo().create(vals)