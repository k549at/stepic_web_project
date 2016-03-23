from models import Question
from models import Answer
from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator

def index(request):
    tmp = loader.get_template('index.html')
    context = Context()
    return HttpResponse(tmp.render(context));

def test(request, *args, **kwargs):
    return HttpResponse('OK');

def main(request):
    questions = Question.objects.all()
    questions = questions.order_by('-added_at')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page',1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request,'main.html',{'questions': page.object_list, 'paginator': paginator, 'page': page,});


def popular(request):
    questions = Question.objects.all()
    questions = questions.order_by('-rating')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page',1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request,'popular.html',{'questions': page.object_list, 'paginator': paginator, 'page': page,});

def question(request, *args, **kwargs):
    templ = loader.get_template('question.html')
    context = Context()
    quest_id = kwargs['pk']
    try:
        question = Question.objects.get(id=quest_id)
        #answers = Answer.objects.all()
        answers = question.answer_set.all()
        answers = answers.values('text')
        
    except Question.DoesNotExist:
        raise Http404
   # return HttpResponse(templ.render(context));
    return render(request, 'question.html', {'quest_title': question.title, 'quest_text': question.text, 'answers': answers,})
