{
  'name': 'hms',
  'author': 'abdulrhman',
  'website': '',
  'description': 'Hospitals Management Systems',
  'data': [
    'security/res_groups.xml',
    'security/ir.model.access.csv',
    # 'views/menu_items.xml', 
    'views/create_patients_data.xml',
    'views/create_departments_data.xml',
    'views/create_doctors_data.xml',
    'views/create_customer_patient.xml',
    'views/show_customer_website.xml',
    'views/make_tax_id_required.xml'
  ],
  'installable': True,
  'auto_install': False,
  'depends': ['base', 'mail', 'crm'],
}
