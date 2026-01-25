# Task 2: Security Best Practices (Django)

## 1) Secure Settings
Configured common security headers and settings in LibraryProject/settings.py:
- SECURE_BROWSER_XSS_FILTER = True
- SECURE_CONTENT_TYPE_NOSNIFF = True
- X_FRAME_OPTIONS = "DENY"
- CSRF_COOKIE_SECURE = True (intended for HTTPS/production)
- SESSION_COOKIE_SECURE = True (intended for HTTPS/production)

## 2) CSRF Protection
Created a CSRF-protected form template:
- bookshelf/templates/bookshelf/form_example.html
Includes {% csrf_token %} inside the <form method="post">.

## 3) SQL Injection Prevention / Secure Input Handling
Implemented a safe search view:
- Uses a Django Form (BookSearchForm) to validate and sanitize user input
- Uses Django ORM filtering (filter(...)) instead of raw SQL
This prevents SQL injection by using parameterized queries through the ORM.

## 4) Content Security Policy (CSP)
Added a CSP header using middleware:
- LibraryProject/middleware.py
- Added to MIDDLEWARE in settings.py

CSP restricts resource loading to reduce the risk of XSS attacks.

## 5) Basic Testing
- Verified the application runs with the security settings enabled.
- Verified CSP header is included in responses via browser DevTools response headers.
- Verified CSRF form includes token tag in template.
✅ Save.