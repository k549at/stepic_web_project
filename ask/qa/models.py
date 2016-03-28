from django.db import models
from django.contrib.auth.models import User
from django.http import Http404
from django.core.urlresolvers import reverse

#  Create your models here.
class Question(models.Model):
#    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField()
    rating.default = '0'
    author = models.ForeignKey(User)
#    user=User.objects.get(id=1)
#    author.default=user.id
    likes = models.ManyToManyField(User, related_name='likes_set')

    def get_url(self):
#        print self.slug
        return reverse('qa.views.question',kwargs={'pk': self.slug})

    def __unicode__(self):
#        print self.title
        return self.title
    class Meta:
        ordering = ['-added_at']
    
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
#    user=User.objects.get(id=1)
#    author.default=user.id
