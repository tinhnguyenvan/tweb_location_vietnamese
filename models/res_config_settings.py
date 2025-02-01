from odoo import api, fields, models, _

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    ghn_token = fields.Char('GHN Token', config_parameter='ghn_token')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        refresh_token = self.env['ir.config_parameter'].sudo().get_param('ghn_token', False)
        if refresh_token:
            res.update({'ghn_token': refresh_token})
        return res

    @api.model
    def set_values(self):
        if self.ghn_token:
            self.env['ir.config_parameter'].sudo().set_param('ghn_token', self.ghn_token)
        super(ResConfigSettings, self).set_values()