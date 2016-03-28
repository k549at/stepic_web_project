from django import forms
from models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.HiddenInput())
    
    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError('error')
        return text

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

    def is_clean(text):
        return true

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.HiddenInput())
    question = forms.ModelChoiceField(queryset=Question.objects.all(),widget=forms.HiddenInput())
  
    def clean_text(self):
        text = self.cleaned_data['text']
        if not text:
            raise forms.ValidationError('error')
        return text

    def save(self):
        answer = Answer(**self.cleaned_data)
#        AnswerForm(initial={'question':quest_id})       

        answer.save()
        return answer
    
    def is_clean(text):
        return true
    
#    def __init__ (self, quest_id, *args, **kwargs):
#        print self
#        print 'from init form args=' + str(quest_id)
#        print str(args[0])
#        self.question = Question.objects.get(id=int(args[0]))
#        print self.question.text
#        super(AnswerForm, self).__init__(*args, **kwargs)
#       
        #self.question = int(quest_id)        

class LoginForm(forms.Form):
    user = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())

class SignUpForm(forms.Form):
    user = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()
