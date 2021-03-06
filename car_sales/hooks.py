# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "car_sales"
app_title = "Car Sales"
app_publisher = "GreyCube Technologies"
app_description = "Car Sales Customizations"
app_icon = "Bookmark"
app_color = "green"
app_email = "sales@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/car_sales/css/car_sales.css"
# app_include_js = "/assets/car_sales/js/car_sales.js"

# include js, css files in header of web template
# web_include_css = "/assets/car_sales/css/car_sales.css"
# web_include_js = "/assets/car_sales/js/car_sales.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "car_sales.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "car_sales.install.before_install"
after_install = "car_sales.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "car_sales.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"car_sales.tasks.all"
# 	],
# 	"daily": [
# 		"car_sales.tasks.daily"
# 	],
# 	"hourly": [
# 		"car_sales.tasks.hourly"
# 	],
# 	"weekly": [
# 		"car_sales.tasks.weekly"
# 	]
# 	"monthly": [
# 		"car_sales.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "car_sales.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "car_sales.event.get_events"
# }

doctype_js = {
	"Customer" : "customizations/customer/customer.js",
	"Quotation" : "customizations/quotation/quotation.js",
}

