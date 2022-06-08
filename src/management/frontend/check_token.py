from django.shortcuts import render


def check_token(html_to_render):
    def func_decorator(func):
        def wrapper(*args):
            request = args[1]
            token = request.COOKIES.get("Token")
            # If token is absent -> redirect to authorization
            if not token:
                return render(request, html_to_render)
            return func(*args, token=token)
        return wrapper
    return func_decorator
