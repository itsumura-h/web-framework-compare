from starlette.applications import Starlette
from starlette.routing import Route
from starlette.config import Config
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette_wtf import CSRFProtectMiddleware

from app.controllers.sign_in_controller import SignInController

config = Config(".env")
DATABASE_URL = config('DATABASE_URL')

middleware = [
    Middleware(SessionMiddleware, secret_key=config('SECRET_KEY')),
    Middleware(CSRFProtectMiddleware, csrf_secret=config('CSRF_SECRET'))
]

app = Starlette(
    debug=True,
    middleware=middleware,
    routes=[
        Route('/', SignInController.signin_page, methods=['GET']),
        Route('/', SignInController.signin, methods=['POST']),
    ],
)
