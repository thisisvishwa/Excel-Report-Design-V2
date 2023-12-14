```python
from odoo import models, fields

class ReportStructure(models.Model):
    _name = 'report.designer.structure'
    _description = 'Report Structure'

    name = fields.Char(string='Section Name', required=True)
    parent_id = fields.Many2one('report.designer.structure', string='Parent Section')
    child_ids = fields.One2many('report.designer.structure', 'parent_id', string='Subsections')
    title = fields.Char(string='Title')
    header = fields.Text(string='Header')
    footer = fields.Text(string='Footer')

    def create_section(self, vals):
        return self.create(vals)

    def delete_section(self):
        self.unlink()
```