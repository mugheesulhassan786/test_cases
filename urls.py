"""
Centralized URL mappings for all test modules
Based on backend route definitions
"""

# Supplier Management
SUPPLIER_URLS = {
    "view_categories": "/supplier-management/view-supplier-category",
    "view_suppliers": "/supplier-management/view-supplier",
    "add_category": "/supplier-management/add-supplier-category",
    "add_supplier": "/supplier-management/add-supplier",
}

# Inventory Management
INVENTORY_URLS = {
    "view_product_category": "/inventory-management/view-product-category",
    "view_inventory": "/inventory-management/view-inventory",
    "view_stock": "/inventory-management/view-stock",
    "view_listing": "/inventory-management/view-listing",
    "manage_discounts": "/inventory-management/manage-discounts",
    "manage_tax_profit": "/inventory-management/manage-tax-profit",
    "view_gtin": "/inventory-management/view-gtin",
    "add_product_category": "/inventory-management/add-product-category",
    "add_inventory": "/inventory-management/add-inventory",
    "add_stock": "/inventory-management/add-stock",
    "add_listing": "/inventory-management/add-listing",
}

# Bundles Management
BUNDLES_URLS = {
    "view_bundles": "/bundles/view-bundles",
    "add_bundle": "/bundles/add-bundle",
}

# Order Management
ORDERS_URLS = {
    "view_orders": "/orders/view-orders",
    "priority_config": "/orders/priority-config",
    "view_requests": "/orders/view-request",  # Note: singular 'request'
    "add_order": "/orders/add-order",
    "add_request": "/orders/add-request",
    "view_ebay_inquiries": "/orders/view-ebay-inquiries",
    "view_ebay_cases": "/orders/view-ebay-cases",
    "view_ebay_disputes": "/orders/view-ebay-disputes",
    "view_ebay_cancellations": "/orders/view-ebay-cancellation",  # Note: singular
    "view_ebay_returns": "/orders/view-ebay-returns",
    "view_amazon_replacements": "/orders/view-amazon-replacements",
}

# Shipping & Delivery
SHIPPING_URLS = {
    "view_shipping_rates": "/delivery-management/view-shipping-rate",
    "view_shipping_carriers": "/delivery-management/view-shipping-carrier",
    "view_custom_labels": "/delivery-management/view-custom-label",
    "add_shipping_rate": "/delivery-management/add-shipping-rate",
    "add_shipping_carrier": "/delivery-management/add-shipping-carrier",
    "add_custom_label": "/delivery-management/add-custom-label",
}

# Reviews
REVIEWS_URLS = {
    "view_reviews": "/reviews/view-review",
}

# Complaints & Ticketing
COMPLAINTS_URLS = {
    "view_complaint_categories": "/complaints-management/view-complaint-category",
    "view_complaints": "/complaints-management/view-complaint",
    "view_ebay_complaints": "/complaints-management/view-ebay-complaint",
    "view_amazon_complaints": "/complaints-management/view-amazon-complaint",
    "view_system_complaints": "/complaints-management/system-complaint",
    "view_tickets": "/ticketing-system/view-tickets",
    "add_ticket": "/ticketing-system/add-ticket",
}

# HR Management (Note: Uses multiple prefixes)
HR_URLS = {
    # User Management (under /user-management)
    "view_user_categories": "/user-management/view-user-category",
    "view_users": "/user-management/view-user",
    "view_teams": "/user-management/view-team",
    "add_user": "/user-management/add-user",
    "add_team": "/user-management/add-team",
    
    # HR (under /hr)
    "employee_shifts": "/hr/employee-shifts",
    "add_shift": "/hr/add-shift",
    "attendance": "/hr/attendance",
    "manage_leaves": "/hr/manage-leaves",
    "punch_in": "/punch-in",
    
    # Payroll (under /payroll)
    "assign_payroll": "/payroll/assign-payroll",
    "processed_payrolls": "/payroll/processed-payrolls",
    "add_payroll": "/payroll/add-payroll",
    
    # Documents (under /documents-management)
    "view_documents": "/documents-management/view-documents",
    "add_document": "/documents-management/add-document",
}

# Accounting
ACCOUNTING_URLS = {
    "view_account_categories": "/accounting-management/view-account-category",
    "view_expense": "/accounting-management/view-expense",
    "view_recurring_expense": "/accounting-management/view-recurring-expense",
    "view_taxation": "/accounting-management/view-taxation",
    "view_revenue": "/accounting-management/view-revenue",
    "view_report": "/accounting-management/view-report",
    "add_account_category": "/accounting-management/add-account-category",
    "add_expense": "/accounting-management/add-expense",
    "add_recurring_expense": "/accounting-management/add-recurring-expense",
    "add_taxation": "/accounting-management/add-taxation",
    "add_revenue": "/accounting-management/add-revenue",
}

# Content Management
CONTENT_URLS = {
    "manage_landing": "/content-management/manage-landing",
    "manage_featured_categories": "/content-management/manage-featured-categories",
}

# Deals Management
DEALS_URLS = {
    "view_deals": "/deals-management/view-deals",
    "add_deal": "/deals-management/add-deal",
}

# Affiliate Program
AFFILIATE_URLS = {
    "view_affiliates": "/affiliate-program/view-affiliates",
    "view_payout_requests": "/affiliate-program/view-payout-requests",
}

# Gamers Community
GAMERS_URLS = {
    "view_blog_categories": "/gamers-community/view-blog-category",
    "view_blogs": "/gamers-community/view-blogs",
    "view_forum_categories": "/gamers-community/view-forum-category",
    "view_forums": "/gamers-community/view-forums",
}

# Calendar
CALENDAR_URLS = {
    "tasks_calendar": "/calendar-integration/tasks-calendar",
    "deals_calendar": "/calendar-integration/deals-calendar",
    "attendance_calendar": "/calendar-integration/attendance-calendar",
    "orders_calendar": "/calendar-integration/orders-calendar",
    "warranties_calendar": "/calendar-integration/warranties-calendar",
    "add_task": "/calendar-integration/add-task",
}

# Leads
LEADS_URLS = {
    "view_leads": "/leads-management/view-leads",
    "add_lead": "/leads-management/add-lead",
}

# Policies
POLICIES_URLS = {
    "view_system_policies": "/policy-management/view-system-policy",
    "view_payment_policies": "/policy-management/view-payment-policies",
    "view_fulfillment_policies": "/policy-management/view-fulfillment-policies",
    "view_return_policies": "/policy-management/view-return-policies",
    "view_ebay_policies": "/policy-management/view-ebay-policies",
    "view_faq_categories": "/policy-management/view-faq-category",
    "view_faqs": "/policy-management/view-faq",
    "view_subscriptions": "/policy-management/view-subscriptions",
    "view_campaigns": "/policy-management/view-compaigns",
}

# Guides
GUIDES_URLS = {
    "view_guide_categories": "/guides/view-guides-category",
    "view_guides": "/guides/view-guides",
    "add_guide_category": "/guides/add-guide-category",
    "add_guide": "/guides/add-guide",
}

# Tasks Management
TASKS_URLS = {
    "view_tasks": "/tasks-management",
}

# Performance Analysis
PERFORMANCE_URLS = {
    "my_performance": "/performance-analysis/my-performance-analysis",
    "team_performance": "/performance-analysis/team-performance-analysis",
}

# System Settings
SETTINGS_URLS = {
    "ebay_auth": "/system-settings/ebay-auth",
    "user_activity_logs": "/system-settings/user-activity-logs",
}

# Customer Tracking
CUSTOMER_URLS = {
    "customer_tracking": "/customer-tracking",
}

# Order Pipeline
PIPELINE_URLS = {
    "order_pipeline": "/order-pipeline-management",
}
