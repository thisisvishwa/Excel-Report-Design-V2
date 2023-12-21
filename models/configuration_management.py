```python
from odoo import models, fields, api

class ConfigurationManagement(models.Model):
    _name = 'report_designer.configuration_management'
    _description = 'Configuration Management for Report Designer'

    name = fields.Char(string='Configuration Name', required=True)
    description = fields.Text(string='Description')
    template_ids = fields.One2many('report_designer.template', 'configuration_id', string='Templates')

    @api.multi
    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        default.update({
            'name': _("%s (copy)") % self.name,
        })
        return super(ConfigurationManagement, self).copy(default)

class Template(models.Model):
    _name = 'report_designer.template'
    _description = 'Excel Report Template'

    name = fields.Char(string='Template Name', required=True)
    file_data = fields.Binary(string='Template File', required=True)
    configuration_id = fields.Many2one('report_designer.configuration_management', string='Configuration')
```
