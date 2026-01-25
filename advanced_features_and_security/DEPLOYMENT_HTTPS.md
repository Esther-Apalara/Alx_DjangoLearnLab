[18:50, 25/01/2026] Esther: # -------------------------
# HTTPS + Secure Redirects
# -------------------------

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Secure cookies (only send cookies over HTTPS)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Security headers
X_FRAME_OPTIONS = "DENY"
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True

# If you're behind a proxy/load balancer (common in deployment), keep this:
# SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
[18:57, 25/01/2026] Esther: # Deployment HTTPS Configuration (Example)

## Goal
Serve the Django app over HTTPS using an SSL/TLS certificate and enforce secure redirects.

## Example with Nginx + Certbot (Let's Encrypt)

### 1) Install Certbot (Ubuntu/Debian)
- Install nginx and certbot packages (depends on OS).
- Use certbot to obtain a certificate for your domain.

### 2) Nginx configuration example

HTTP -> HTTPS redirect:
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    return 301 https://$host$request_uri;
}

HTTPS server:
server {
    listen 443 ssl;
    server_name your-domain.com www.your-domain.com;

    ssl_certificate     /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;

    # Optional hardening
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;

    location /static/ {
        alias /path/to/static/;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;  # gunicorn/uvicorn upstream
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto https;
    }
}

## Django note (behind proxy)
If using a reverse proxy that sets X-Forwarded-Proto, enable:
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")