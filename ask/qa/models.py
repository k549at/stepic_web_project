from django.db import models
from django.contrib.auth.models import User
from django.http import Http404

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(blank=False)
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-id']
    
class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)
