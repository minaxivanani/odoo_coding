from odoo import models, fields, api
from datetime import datetime


class Book(models.Model):
    _name = 'book'
    _description = 'my book'

    name = fields.Char(string="Title", default="Enter Book Name")
    author_id = fields.Many2one('author')
    category_id = fields.Many2one('bookcategory')
    department_id = fields.Many2one('bookdepartment')
    edition = fields.Char()
    date = fields.Date()
    code = fields.Integer()
    book_image = fields.Binary(string='Image',attachment=True,readonly=False)

    book_description = fields.Text()
    price = fields.Float()
    publisher_id = fields.Many2one('bookspublisher')
    state = fields.Selection([('new', 'New'), ('issued', 'Issued'), ('cancel', 'Cancel')], default='new')

    def action_issued(self):
        for record in self:
            if record.state == 'cancel':
                raise UserError("Book is cancel")
            record.state = 'issued'

    def action_cancel(self):
        for record in self:
            if record.state == 'issued':
                raise UserError("Book is issued")
            record.state = 'cancel'


class Author(models.Model):
    _name = 'author'
    _description = 'author name'

    name = fields.Char()
    author_ids = fields.One2many('book', 'author_id')

    book_name = fields.Char()
    book_code = fields.Integer()


class BookCategory(models.Model):
    _name = 'bookcategory'
    _description = 'Books category'

    name = fields.Char()

    book_type = fields.Char()

    author_name = fields.Char()
    price = fields.Float()
    publication = fields.Char()


class BookDepartment(models.Model):
    _name = 'bookdepartment'
    _description = 'Book Department'

    name = fields.Char()


class BookPublisher(models.Model):
    _name = 'books.publisher'
    _description = 'Book Publisher'

    name = fields.Char()


class Issue(models.Model):
    _name = 'issue'
    _description = 'Book issued'

    name = fields.Char(default="User", required=True)
    email = fields.Char()
    address = fields.Text()
    issue_date = fields.Date()
    ret_date = fields.Date()
    dept_ids = fields.Many2one('bookdepartment', 'department_id')
    cat_ids = fields.Many2one('bookcategory', 'category_id')
    image = fields.Image()
    rem_days = fields.Char(string="Count Days", readonly=True)
    penlaty = fields.Char(string="Penlaty", readonly=True)

    @api.onchange('ret_date')
    def _onchange_ret_date(self):
        for record in self:
            if record.ret_date:
                date_format = "%Y-%m-%d"
                book_issued_date = datetime.strptime(str(record.issue_date), date_format)
                book_return_date = datetime.strptime(str(record.ret_date), date_format)
                cntdays = book_return_date - book_issued_date
                x = str(cntdays).split(",")[0]
                print(x.split("days")[0])
                y = x.split("days")[0]
                c = int(y) * 10
                record.rem_days = int(y)
                record.penlaty = c

            else:
                pass
                # record.rem_days = 0


class Shelf(models.Model):
    _name = 'shelf'
    _description = 'Shelf'

    name = fields.Char()
    rack_id = fields.Many2one('rack')


class Rack(models.Model):
    _name = 'rack'
    _description = 'Rack'

    name = fields.Char()
    shelf_ids = fields.One2many('shelf', 'rack_id')
