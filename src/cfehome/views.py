from django.http import HttpResponse
import pathlib
from django.conf import settings

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    html = (settings.BASE_DIR / 'cfehome/home.html').read_text()
    return HttpResponse(html)
    return HttpResponse('<h1>Hello World!</h1>')