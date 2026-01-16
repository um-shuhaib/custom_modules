from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal


class TestPortal(CustomerPortal):

    @http.route(['/my/test'],type="http",website=True,auth="user")
    def TestPortalView(self,**kw):
        patient_obj=request.env['hospital.patient']
        print("........................................................................")
        patient=patient_obj.search([])
        return request.render('om_hospital.test_portal_list_view',{'patient':patient})
        # return request.render('test_portal_list_view',{})
        # return {}