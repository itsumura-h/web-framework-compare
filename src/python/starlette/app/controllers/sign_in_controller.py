from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates
from starlette_wtf import csrf_protect, StarletteForm


class SignInController:
    async def signin_page(request: Request) -> HTMLResponse:
        form = await StarletteForm.from_formdata(request)
        templates = Jinja2Templates(directory='./app/views')
        return templates.TemplateResponse(
            'signin.html', {
                'request': request,
                'form': form
            }
        )

    @csrf_protect
    async def signin(request: Request) -> RedirectResponse:
        print(await request.form())
        return RedirectResponse('/', 302)
