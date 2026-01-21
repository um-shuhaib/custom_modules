from odoo import http, Command
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal,pager as portal_page


class TestPortal(CustomerPortal):

    @http.route(['/my/patients'],type="http",website=True,auth="user")
    def TestPortalView(self,**kw):
        patient_obj=request.env['hospital.patient']
        print("........................................................................")
        patient=patient_obj.search([])
        return request.render('om_hospital.test_portal_list_view',{'patient':patient,'page_name':'patients'})
        # return request.render('test_portal_list_view',{})
        # return {}

    

    @http.route(['/my/patients/<model("hospital.patient"):patient_id>','/my/patients/<model("hospital.patient"):patient_id>/page/<int:page>'],website=True,type="http",method=['GET'])
    def TestPortalFormView(self,patient_id,page=1,**kw):
        print()
        values = self._prepare_portal_layout_values()
        total=len(patient_id.product_ids)
        pager=portal_page(
            url=f'/my/patients/{patient_id.id}',
            total=total,
            step=3,
            page=page

        )
        values.update({
            'patient': patient_id,
            'page_name': 'patient_form',
            'pager':pager
        })
        return request.render('om_hospital.test_portal_form_view',values)
        # return request.render('om_hospital.test_portal_form_view',{'patient':patient_id})

    @http.route(['/my/patients/<model("hospital.patient"):patient_id>'],website=True,type="http",method=['POST'],csrf=False)
    def AddProductLine(self,patient_id,**post):
        patient=patient_id
        product_id=int(post.get("product_id"))
        product=request.env['product.product'].sudo().browse(product_id)
        quantity=post.get("qty")
        # quantity=post.get("qty")
        patient.write({
            # 'product_ids':[(0,0,{
            'product_ids':[Command.create({
                'patient_id':patient,
                'product_id':product.id,
                'quantity':quantity
            })]
        })
        return request.redirect('/my/patients')


