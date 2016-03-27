#!/usr/bin/env python
#coding: utf—8
import sys
from models import Question
from models import Answer
from forms import AskForm
from forms import AnswerForm
from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

reload(sys)
sys.setdefaultencoding('utf8')

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
    quest_id = kwargs['pk']
    try:
        question = Question.objects.get(id=quest_id)
        answers = question.answer_set.all()
        answers = answers.values('text')
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'question_old.html', {'quest_title': question.title, 'quest_text': question.text, 'answers': answers,})

def ask_add(request):
    if request.method == "POST":
        form=AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            redir_url = '/question/' + str(question.id)
        return HttpResponseRedirect(redir_url) 
    else:
        form = AskForm()        
    return render(request, 'ask_add.html', {'form': form})

def answer_add(request, *args, **kwargs):
    quest_id = kwargs['pk']
    try:
        question = Question.objects.get(id=quest_id)
        if request.method == "POST":
            form = AnswerForm(request.POST)
            if form.is_valid():
                form.save()
                redir_url = '/question/'+str(quest_id)
            return HttpResponseRedirect(redir_url) 
        else:
            form = AnswerForm(initial={'question': question})    
        answers = question.answer_set.all()
        
#        answers =repr(answers.values('text')).decode("unicode_escape")
        ans= (answers.values('text'))
        l=[l['text'] for l in ans]
        #answers =str(answers).decode('utf8')
#        print repr(answers).decode("unicode_escape")        
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'question_old.html', {'form': form, 'quest_title': question.title, 'quest_text': question.text, 'answers':l,})
