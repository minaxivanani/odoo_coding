
from odoo import models,fields


class Mybook(models.Model):
    _name = 'book'

    _description = "mybook"

    name = fields.Char()

    name = fields.Char( string="Title",default="Unknown",required=True)

    description = fields.Text()
    postcode = fields.Char()
    return_date = fields.Date("Last Seen", default=lambda self: fields.Datetime.now())
    issue_date = fields.Date("Last Seen", default=lambda self: fields.Datetime.now())
    image = fields.Image()
 
   