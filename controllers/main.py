```python
from odoo import http
from odoo.http import request

class ReportDesignerController(http.Controller):

    @http.route('/report_designer/generate_report', type='http', auth='user')
    def generate_report(self, **kwargs):
        report_designer = request.env['report.designer']
        report_id = kwargs.get('report_id')
        report = report_designer.browse(int(report_id))
        if not report:
            return request.not_found()
        try:
            file_data = report.generate_report()
        except Exception as e:
            return request.make_response('Error: %s' % str(e))
        return request.make_response(file_data,
                                     [('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                                      ('Content-Disposition', 'attachment; filename=report.xlsx;')])

    @http.route('/report_designer/email_report', type='json', auth='user')
    def email_report(self, report_id, email_to):
        report_designer = request.env['report.designer']
        report = report_designer.browse(int(report_id))
        if not report:
            return {'error': 'Report not found'}
        try:
            report.email_report(email_to)
            return {'success': 'Report emailed successfully'}
        except Exception as e:
            return {'error': str(e)}
```