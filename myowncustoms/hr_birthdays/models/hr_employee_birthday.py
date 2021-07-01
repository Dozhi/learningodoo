from dateutil.relativedelta import relativedelta
from datetime import date

from odoo import models, fields, api


def get_next_birthday(dt):
	date_today = date.today()
	age = date_today.year - dt.year
	dt_next_birthday = dt + relativedelta(years=age)
	if dt_next_birthday < date_today:
		dt_next_birthday += relativedelta(years=1)
	return dt_next_birthday


class HrEmployeeBirthdays(models.Model):
	"""Extend to add field of birthday with its date tracking """

	_inherit = "hr.employee"

	date_next_birthday = fields.Date(string="Next Birthday", compute='_compute_date_next_birthday')

	def _compute_date_next_birthday(self):
		for empl in self.filtered('birthday'):
			empl.date_next_birthday = get_next_birthday(empl.birthday)
