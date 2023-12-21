from odoo import models, fields, api, exceptions

class ReportParameters(models.Model):
    _name = 'report.designer.parameters'
    _description = 'Report Parameters'

    name = fields.Char(string='Parameter Name', required=True)
    data_type = fields.Selection([
        ('string', 'String'),
        ('integer', 'Integer'),
        ('float', 'Float'),
        ('boolean', 'Boolean'),
        ('date', 'Date'),
        ('datetime', 'DateTime'),
        ('selection', 'Selection'),
    ], string='Data Type', required=True)
    default_value = fields.Char(string='Default Value')
    selection_options = fields.Text(string='Selection Options', help='Comma-separated values for selection type')

    @api.constrains('data_type', 'default_value', 'selection_options')
    def _check_default_value(self):
        for record in self:
            if record.data_type == 'selection' and not record.selection_options:
                raise exceptions.ValidationError('Selection options must be provided for selection type parameters.')
            if record.default_value and record.data_type != 'string':
                try:
                    if record.data_type == 'integer':
                        int(record.default_value)
                    elif record.data_type == 'float':
                        float(record.default_value)
                    elif record.data_type == 'boolean':
                        if record.default_value not in ['True', 'False']:
                            raise ValueError
                    elif record.data_type in ['date', 'datetime']:
                        fields.Datetime.from_string(record.default_value)
                except ValueError:
                    raise exceptions.ValidationError('Default value does not match the selected data type.')