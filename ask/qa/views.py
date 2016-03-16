# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    tmp = loader.get_template('index.html')
    context = Context()
    return HttpResponse(tmp.render(context));

def test(request, *args, **kwargs):
    return HttpResponse('OK');
