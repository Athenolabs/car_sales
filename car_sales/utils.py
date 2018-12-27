import frappe

@frappe.whitelist()
def get_customer_from_sales_inquiry(customer_no='',sales_inquiry=''):
    data = ''
    if customer_no:
        data = frappe.get_all('Sales Inquiry', 
                filters={'phone_no': customer_no},
                order_by='date desc',
                fields=['client_name','customer_group','customer_email','date','transaction_type','customer_type','sales_partner',] 
            )
        return data[0] if data else {}
    if sales_inquiry:
        data = frappe.get_all('Inquiry Item', 
                filters={'parent': sales_inquiry},
                fields=['item','quantity'] 
            )
        return data

@frappe.whitelist()
def create_contact_from_si(customer_no='', customer=''):
    sales_inquiry = frappe.get_all('Sales Inquiry', 
            filters={'phone_no': customer_no},
            order_by='date desc',
            fields=['client_name','customer_group','customer_email','date','transaction_type','customer_type','sales_partner',] 
        )
    if sales_inquiry:
        contact = frappe.new_doc('Contact')
        contact.update({
            'first_name': sales_inquiry[0].client_name,
            'email_id' : sales_inquiry[0].customer_email,
            'mobile_no' : customer_no,
            'links' :{
                'link_doctype' : 'Customer',
                'link_name' : customer,
            }
            
        })
        contact.save(ignore_permissions=True)
