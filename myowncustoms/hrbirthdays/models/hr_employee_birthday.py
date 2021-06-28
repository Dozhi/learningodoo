from odoo import models, fields, api

class HrEmployeeBirthdays(models.Model):
	"""Extend to add field of birthday with its date tracking """

	_inherit = "hr.employee"

	asset_employee_birthday = "birthday"


#	TODO
# birthday / hr.employee