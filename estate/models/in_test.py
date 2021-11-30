from odoo import models ,fields,api
from odoo.exceptions import UserError,ValidationError

class MyTest(models.Model):
	_name = 'my.test'
	_description = 'My test'


	name = fields.Char()
	address = fields.Text()
	email = fields.Char()
	pincode = fields.Integer()

class MyTest(models.Model):
	_name = 'my.gvp'
	_description = 'My test'


	name = fields.Char()
	address = fields.Text()
	email = fields.Char()
	pincode = fields.Integer()

class G(models.Model):

	_inherit = "my.gvp"
	

	country = fields.Char()
	state = fields.Char()
	city = fields.Char()


class GG(models.Model):

	_name = "g2"
	_inherit = "my.gvp"

	pancard = fields.Char()
	aadharcard = fields.Char()

class GGG(models.Model):
	_name = "g3"
	_inherit = {"my.gvp" : "test_id"}

	test_id =  fields.Many2one("mygvp")

class BankProperty(models.Model):
	_inherit = "estate.property"

	bankname = fields.Char()
	bankintrest = fields.Float()




