from frappe.custom.doctype.custom_field.custom_field import create_custom_field
from frappe import _
def after_install():
	create_custom_field('Customer', {
		'label': _('Contact No'),
		'fieldname': 'contact_no_car_sales',
		'fieldtype': 'Data',
		'insert_after': 'customer_name'
	})
	create_custom_field('Customer', {
		'label': _('Fetch Customer from Sales Inquiry'),
		'fieldname': 'fetch_customer_frm_si',
		'fieldtype': 'Button',
		'depends_on':'eval:doc.contact_no_car_sales',
		'insert_after': 'contact_no_car_sales'
	})
	create_custom_field('Quotation', {
		'label': _('Sales Inquiry'),
		'fieldname': 'sales_inquiry',
		'fieldtype': 'Link',
		'options': 'Sales Inquiry',
		'insert_after': 'customer'
	})
	create_custom_field('Quotation', {
		'label': _('Fetch Customer from Sales Inquiry'),
		'fieldname': 'fetch_customer_frm_si',
		'fieldtype': 'Button',
		'depends_on':'eval:doc.sales_inquiry',
		'insert_after': 'sales_inquiry'
	})