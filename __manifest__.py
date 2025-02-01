{
    'name': "Location Việt Nam",
    'summary': """Danh sách tỉnh thành, quận huyện, phường xã Việt Nam""",
    'author': "tinh.nguyenvan",
    'website': "https://tweb.com.vn/?utm_source=odoo_apps",
    'sequence':'10',
    'category': 'Studio',
    'version': '17.0.1.0.1',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner.xml',
        'views/res_company.xml',
        'views/res_state_district_view.xml',
        'views/res_ward_view.xml',
        'views/res_config_settings_view.xml',
        'views/res_country_state.xml',
        'views/lunch_call_api.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'GPL-3'
}