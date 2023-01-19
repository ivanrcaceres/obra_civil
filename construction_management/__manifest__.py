# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name": "Odoo Construction Management",
    "version": "11.0.0.2",
    "depends": ['base', 'project', 'stock',
                'account', 'hr', 'purchase', 'account_asset','sale','account_budget','website_form_project','note','hr_timesheet',
                ],
    "author": "Browseinfo",
    "summary": "Real Estate Management, Construction Project management, Building Construction",
    "description": """
    BrowseInfo developed a new odoo/OpenERP module apps.
    This module use for Real Estate Management, Construction management, Building Construction,
    constuction projects
    Construction Projects
    Budgets
    Notes
    Materials
    Material Request For Job Orders
    Add Materials
    Job Orders
    Create Job Orders
    Job Order Related Notes
    Issues Related Project
    Vendors
    Vendors / Contractors

    Construction Management
    Construction Activity
    Construction Jobs
    Job Order Construction
    Job Orders Issues
    Job Order Notes
    Construction Notes
    Job Order Reports
    Construction Reports
    Job Order Note
    Construction app
    Project Report
    Task Report
    Construction Project - Project Manager
    real estate property
    propery management
    bill of material
    Material Planning On Job Order

    Bill of Quantity On Job Order
    Bill of Quantity construction
    """,
    "website": "www.browseinfo.in",
    "data": [
        "security/ir.model.access.csv",
        'view/project.xml',
        "view/main_menu.xml",
        'view/bill_of_quantity_view.xml',
        'view/cost_code_view.xml',
        'view/cost_header_view.xml',
        'view/work_package_view.xml',
        'view/construction_management.xml',
        'report/construction_report.xml',
        'report/project_project_report.xml',
        'report/project_note_report.xml',
        'report/project_job_orders.xml',
        # Sub Task
        'view/sub_task.xml',
        
    ],
    "images": 'static/main_screenshot.png',
    "price": 55,
    "currency": 'EUR',
    'live_test_url':'https://youtu.be/Jdhxf-UwQpY',
    "auto_install": False,
    "installable": True,
    "images":['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
