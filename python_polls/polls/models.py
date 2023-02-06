from django.db import models
from django.utils import timezone

import datetime

# Create your models here.


class Question(models.Model):
    # question_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # question = models.ForeignKey(Question,on_delete=models.CASCADE)
    # choce_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Post(models.Model):
    title = models.CharField(max_length=100)    #post's title
    content = models.TextField()                #post's contents


class Article(models.Model):
    title = models.CharField(max_length=100)        #Article's title
    content = models.TextField()                    #Article's contents
    created_at = models.DateTimeField(auto_now_add=True)    #create datetime
    updated_at = models.DateTimeField(auto_now=True)        #update datetime



