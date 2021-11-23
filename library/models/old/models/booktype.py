from odoo import models, fields


class Booktype(models.Model):
    _name="booktypes"

    name = fields.Char(string="Title")
    author = fields.Char()
    category = fields.Selection([('fiction','Fiction'), ('bio', 'Biography')])
    price = fields.Float()
    publication = fields.Char()
    image = fields.Image()

class Bookauthor(models.Model):

    _name="author"

    name = fields.Char(string="Title")
    type = fields.Char(string="Title")
    price = fields.Float()
    publication = fields.Char()
    image = fields.Image()