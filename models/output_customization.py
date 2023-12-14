```python
from odoo import models, fields, api

class OutputCustomization(models.Model):
    _name = 'report_designer.output_customization'
    _description = 'Output Customization for Report Designer'

    name = fields.Char(string='Name', required=True)
    file_naming_convention = fields.Char(string='File Naming Convention')
    wizard_description = fields.Text(string='Wizard Description')

    @api.model
    def create(self, vals):
        result = super(OutputCustomization, self).create(vals)
        return result

    def write(self, vals):
        result = super(OutputCustomization, self).write(vals)
        return result

    def unlink(self):
        result = super(OutputCustomization, self).unlink()
        return result

    def copy(self, default=None):
        result = super(OutputCustomization, self).copy(default)
        return result
```