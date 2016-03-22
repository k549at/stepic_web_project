from models import Question
from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render, render_to_response

def index(request):
    tmp = loader.get_template('index.html')
    context = Context()
    return HttpResponse(tmp.render(context));

def test(request, *args, **kwargs):
    return HttpResponse('OK');

def main(request, *args, **kwargs):
    templ = loader.get_template('main.html')
    context = Context()
    return HttpResponse(templ.render(context));


def popular(request, *args, **kwargs):
    templ = loader.get_template('popular.html')
    context = Context()
    return HttpResponse(templ.render(context));

def question(request, *args, **kwargs):
    templ = loader.get_template('question.html')
    context = Context()
    quest = kwargs['pk']
    try:
        question = Question.objects.get(id=quest)
    except Question.DoesNotExist:
        raise Http404
   # return HttpResponse(templ.render(context));
    return render(request, 'question.html', {'quest_title': question.title, 'quest_text': question.text})
