#!/usr/bin/env python
#coding: utf—8
import sys
from models import Question, Answer
from forms import AskForm, AnswerForm, SignUpForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 
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

@login_required
def question(request, *args, **kwargs):
    quest_id = kwargs['pk']
    if request.method == "POST":
        return HttpResponse ('OK')
    else:
        try:
#            print 'get on question'
            question = Question.objects.get(id=quest_id)
            answers = question.answer_set.all()
            ans= (answers.values('text'))
            l=[l['text'] for l in ans]
            user=request.user
            form = AnswerForm(initial={'question': question, 'author': user})
        except Question.DoesNotExist:
            raise Http404
        return render(request, 'question_old.html', {'quest_title': question.title, 'quest_text': question.text, 'answers': l,'form':form,})

@login_required
def ask(request):
    if request.method == "POST":
        
        form=AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            redir_url = '/question/' + str(question.id)
        return HttpResponseRedirect(redir_url) 
    else:
        user = request.user
        form = AskForm(initial={'author':user})
    return render(request, 'ask.html', {'form': form})

@login_required
def answer(request, *args, **kwargs):
    quest_id = kwargs['pk']
#    print 'in answer'

    if request.method == "POST":
#        print 'post on answer'
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            redir_url = '/question/'+str(quest_id)
        else:
            redir_url = '/question/'+str(quest_id)
        return HttpResponseRedirect(redir_url) 
    else:
#        print 'get on answer'
        try:
            question = Question.objects.get(id=quest_id)
#            print 'from anser'
            user = request.user
#            print user
            form = AnswerForm(initial={'question': question, 'author': user})    
            answers = question.answer_set.all()        
            ans= (answers.values('text'))
            l=[l['text'] for l in ans]
            #answers =str(answers).decode('utf8')
#               print repr(answers).decode("unicode_escape")        
        except Question.DoesNotExist:
            raise Http404
    return render(request, 'question_old.html', {'form': form, 'quest_title': question.title, 'quest_text': question.text, 'answers':l,})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST.get('user'), request.POST.get('email'), request.POST.get('password'))
            user.save()
        return HttpResponseRedirect('/main/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['user']
            password = request.POST['password']
            user = authenticate(username=username, password = password)
            if user is not None:
                auth_login(request, user)
        return HttpResponseRedirect('/main/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
