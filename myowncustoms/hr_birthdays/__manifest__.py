{
    'name': "hr employee birthday field",
    'version': '1.0',
    'author': "Dominykas Zogas",
    'category': 'Category',
    'description': """
    Add custom birthday field to hr module
    """,
    'depends': [
        'hr',
    ],
    'data': [
        'views/hr_employee_birthday_views.xml',
    ],
    'installable': True,
}