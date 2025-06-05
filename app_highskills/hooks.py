from frappe import _

def get_hooks():
    return {
        "app_name": "Highskills",
        "app_title": _("Highskills"),
        "app_publisher": "Your Name",
        "app_description": _("A description of your app."),
        "app_icon": "octicon octicon-file-directory",
        "app_color": "grey",
        "app_email": "your.email@example.com",
        "app_license": "MIT",
        "app_version": "0.0.1",
        "app_include_js": "/assets/app_highskills/js/app_highskills.js",
        "app_include_css": "/assets/app_highskills/css/app_highskills.css",
        "web_include_js": "/assets/app_highskills/js/app_highskills_web.js",
        "web_include_css": "/assets/app_highskills/css/app_highskills_web.css",
        "on_start": "app_highskills.utils.on_start",
        "before_install": "app_highskills.utils.before_install",
        "after_install": "app_highskills.utils.after_install",
        "on_update": "app_highskills.utils.on_update",
        "on_uninstall": "app_highskills.utils.on_uninstall",
        "scheduler_events": {
            "all": [
                "app_highskills.tasks.all"
            ],
            "daily": [
                "app_highskills.tasks.daily"
            ],
            "hourly": [
                "app_highskills.tasks.hourly"
            ],
            "weekly": [
                "app_highskills.tasks.weekly"
            ],
            "monthly": [
                "app_highskills.tasks.monthly"
            ]
        },
        "doctype_js": {
            "Your Doctype": "public/js/your_doctype.js"
        },
        "doctype_list_js": {
            "Your Doctype": "public/js/your_doctype_list.js"
        },
        "doctype_tree_js": {
            "Your Doctype": "public/js/your_doctype_tree.js"
        },
        "doctype_calendar_js": {
            "Your Doctype": "public/js/your_doctype_calendar.js"
        }
    }