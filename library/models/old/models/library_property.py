from odoo import models,fields

class Mylibrary(models.Model):

    _name = 'mybook'
    _description = 'my books details'
 

    name=fields.Char()

    name = fields.Char( string="Title",default="Unknown",required=True)

    description = fields.Text()
    bookcode = fields.Char()
    issue_date= fields.Date("Last Seen", default=lambda self: fields.Datetime.now())
    return_date  = fields.Date("Last Seen", default=lambda self: fields.Datetime.now())
    price = fields.Float()
    image = fields.Image()
    author = fields.Text()



