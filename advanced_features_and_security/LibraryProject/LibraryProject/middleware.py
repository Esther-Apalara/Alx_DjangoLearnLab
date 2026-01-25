def ContentSecurityPolicyMiddleware(get_response):
    """
    Function-based middleware that adds a Content-Security-Policy header.
    """

    def middleware(request):
        response = get_response(request)
        response["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self'; "
            "img-src 'self' data:; "
            "font-src 'self'; "
            "object-src 'none'; "
            "base-uri 'self'; "
            "frame-ancestors 'none'; "
        )
        return response

    return middleware