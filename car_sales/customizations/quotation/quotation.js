frappe.ui.form.on("Quotation", {
    "fetch_customer_frm_si":function(frm, cdt, cdn){        
        frappe.call({
            method : "car_sales.utils.get_customer_from_sales_inquiry",
            args : {
                sales_inquiry : frm.doc.sales_inquiry
            },
            callback : function(r){
                if (r.message ){
                    debugger;
                    var data = r.message;
                    for( data in r.message){
                        console.log(r.message[data]);
                        var row = frappe.model.add_child(cur_frm.doc, "Quotation Item", "items");
        				row.item_code = r.message[data].item;
        				row.qty = r.message[data].quantity;
        				refresh_field("items");
                    }
                }
            }
        });
    }
})