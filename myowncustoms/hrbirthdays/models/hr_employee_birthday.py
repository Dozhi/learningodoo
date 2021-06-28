from odoo import models, fields

class HrEmployeeBirthdays(models.Model):
	"""Extend to add field of birthday with its date tracking """

	_inherit = "hr.employee"

	asset_employee_birthday = "birthday"

# birthday / hr.employee