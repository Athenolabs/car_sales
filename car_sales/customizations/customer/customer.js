frappe.ui.form.on("Customer", {
    "fetch_customer_frm_si":function(frm, cdt, cdn){        
        frappe.call({
            method : "car_sales.utils.get_customer_from_sales_inquiry",
            args : {
                customer_no : frm.doc.contact_no_car_sales
            },
            callback : function(r){
                if (r.message ){
                    frm.set_value("customer_name", r.message['client_name']);
                    frm.set_value("customer_group", r.message['customer_group']);
                    frm.set_value("email_id", r.message['customer_email']);
                    frm.set_value("customer_type", r.message['customer_type']);
                    frm.set_value("default_sales_partner", r.message['sales_partner']);
                }
            }
        });
    }
})