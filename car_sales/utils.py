import frappe

@frappe.whitelist()
def get_customer_from_sales_inquiry(customer_no="",sales_inquiry=""):
    data = ""
    if customer_no:
        data = frappe.get_all('Sales Inquiry', 
                filters={'phone_no': customer_no},
                order_by='date desc',
                fields=['client_name','customer_group','customer_email','date','transaction_type','customer_type','sales_partner',] 
            )
        return data[0]
    if sales_inquiry:
        data = frappe.get_all('Inquiry Item', 
                filters={'parent': sales_inquiry},
                fields=['item','quantity'] 
            )
        return data
