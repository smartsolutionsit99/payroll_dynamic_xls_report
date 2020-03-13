{
    'name': 'Dynamic Payroll Report Excel',
    'version': '1.0',
    'category': 'payroll',
    'sequence': 60,
    'summary': 'Dynamic Payroll Report Excel',
    'description': "It shows payroll report in excel for given month,create your own report",
    'author':'Smart Solutions',
    'depends': ['base','hr', 'hr_payroll','web_widget_color'],
    'data': [
        'security/ir.model.access.csv',
        'views/payroll_report.xml',
        'wizard/payroll_report_wiz.xml'
      ],
    'images': ['static/description/cover.jpg'],
    'auto_install': False,
    'installable': True,
    'application': True,
    #'licence': 'GPL-3',
    'price': 25,
    'currency': 'USD',
    'support': 'smartsolutionsit99@gmail.com',
}
