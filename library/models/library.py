from odoo import models,fields

class Book(models.Model):
    _name = 'book'

    _description = "book"

    name = fields.Char()
    
    
  
    name = fields.Char( string="Title",default="Unknown",required=True)

    description = fields.Text()
    postcode = fields.Char()
    return_date = fields.Date("Last Seen", default=lambda self: fields.Datetime.now())
    issue_date = fields.Date("Last Seen", default=lambda self: fields.Datetime.now())
    image = fields.Image()

class Author(models.Model):
    _name = 'author'

    _description = "book"

    name = fields.Char()
    
    
  
    name = fields.Char( string="Title",default="Unknown",required=True)

    description = fields.Text()
    code = fields.Char()
    

class Authorbook(models.Model):
    _name = 'authorbook'

class Booktype(models.Model):
    _name = 'booktype'
    _description = 'book type'

    name = fields.Char( string="Title",default="Unknown",required=True)

    description = fields.Text()
    postcode = fields.Char()
    image = fields.Image()

class Bookauthor(models.Model):
    name = 'authorbook'

class 

