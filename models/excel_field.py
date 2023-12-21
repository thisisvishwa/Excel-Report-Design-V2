```python
from odoo import models, fields, api

class ExcelField(models.Model):
    _name = 'report_designer.excel_field'
    _description = 'Excel Field for Report Designer'

    name = fields.Char(string='Field Name', required=True)
    field_type = fields.Selection([
        ('char', 'Char'),
        ('int', 'Integer'),
        ('float', 'Float'),
        ('bool', 'Boolean'),
        ('date', 'Date'),
        ('datetime', 'DateTime'),
        ('selection', 'Selection'),
        ('many2one', 'Many2One'),
        ('one2many', 'One2Many'),
        ('many2many', 'Many2Many'),
    ], string='Field Type', required=True)
    formatting = fields.Char(string='Formatting')
    conditional_styling = fields.Text(string='Conditional Styling')
    formula = fields.Text(string='Excel Formula')

    @api.model
    def create(self, vals):
        field = super(ExcelField, self).create(vals)
        # Add additional logic here
        return field

    def write(self, vals):
        super(ExcelField, self).write(vals)
        # Add additional logic here

    def unlink(self):
        # Add additional logic here
        super(ExcelField, self).unlink()

    def copy(self, default=None):
        field = super(ExcelField, self).copy(default)
        # Add additional logic here
        return field
```