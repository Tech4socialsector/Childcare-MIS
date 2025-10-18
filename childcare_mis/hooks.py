app_name = "childcare_mis"
app_title = "Childcare MIS"
app_publisher = "Augustin Moses"
app_description = "MIS for managing child care homes"
app_email = "tech4socialsector@azimpremjifoundation.org"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "childcare_mis",
# 		"logo": "/assets/childcare_mis/logo.png",
# 		"title": "Childcare MIS",
# 		"route": "/childcare_mis",
# 		"has_permission": "childcare_mis.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/childcare_mis/css/childcare_mis.css"
# app_include_js = "/assets/childcare_mis/js/childcare_mis.js"

# include js, css files in header of web template
# web_include_css = "/assets/childcare_mis/css/childcare_mis.css"
# web_include_js = "/assets/childcare_mis/js/childcare_mis.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "childcare_mis/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "childcare_mis/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "childcare_mis.utils.jinja_methods",
# 	"filters": "childcare_mis.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "childcare_mis.install.before_install"
# after_install = "childcare_mis.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "childcare_mis.uninstall.before_uninstall"
# after_uninstall = "childcare_mis.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "childcare_mis.utils.before_app_install"
# after_app_install = "childcare_mis.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "childcare_mis.utils.before_app_uninstall"
# after_app_uninstall = "childcare_mis.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "childcare_mis.notifications.get_notification_config"

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
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"childcare_mis.tasks.all"
# 	],
# 	"daily": [
# 		"childcare_mis.tasks.daily"
# 	],
# 	"hourly": [
# 		"childcare_mis.tasks.hourly"
# 	],
# 	"weekly": [
# 		"childcare_mis.tasks.weekly"
# 	],
# 	"monthly": [
# 		"childcare_mis.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "childcare_mis.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "childcare_mis.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "childcare_mis.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "childcare_mis.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["childcare_mis.utils.before_request"]
# after_request = ["childcare_mis.utils.after_request"]

# Job Events
# ----------
# before_job = ["childcare_mis.utils.before_job"]
# after_job = ["childcare_mis.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"childcare_mis.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

