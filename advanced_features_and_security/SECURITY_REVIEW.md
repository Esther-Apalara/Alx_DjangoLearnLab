# Security Review (Task 3)

## Implemented Measures
- SECURE_SSL_REDIRECT=True: forces HTTPS redirects
- HSTS enabled:
  - SECURE_HSTS_SECONDS=31536000
  - SECURE_HSTS_INCLUDE_SUBDOMAINS=True
  - SECURE_HSTS_PRELOAD=True
- Secure cookies:
  - SESSION_COOKIE_SECURE=True
  - CSRF_COOKIE_SECURE=True
- Secure headers:
  - X_FRAME_OPTIONS="DENY"
  - SECURE_CONTENT_TYPE_NOSNIFF=True
  - SECURE_BROWSER_XSS_FILTER=True

## Benefits
- Prevents downgrade attacks and ensures encrypted transport (HTTPS).
- HSTS reduces risk of SSL-stripping.
- Secure cookies reduce session/CSRF cookie leakage over non-HTTPS.
- Clickjacking and MIME-sniffing protections reduce browser-based attacks.

## Notes / Potential Improvements
- In production, DEBUG must be False and ALLOWED_HOSTS configured.
- Add logging/monitoring and rotate SECRET_KEY securely.
- Consider rate limiting, stronger CSP tuning, and MFA for admin accounts.