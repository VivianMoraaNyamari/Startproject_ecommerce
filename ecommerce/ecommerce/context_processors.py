def site_settings(request):
    """Add site-wide settings to template context"""
    return {
        'SITE_NAME': 'E-Commerce Store',
        'SITE_DESCRIPTION': 'Your one-stop shop for everything',
        'COMPANY_EMAIL': 'contact@ecommerce.com',
        'COMPANY_PHONE': '+254 720 000000',
    }
