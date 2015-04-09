"""
Domain model.
"""

from django.db import models as db
from django.contrib.auth.models import User


class QAValueObject(db.Model):
    up_votes = db.IntegerField(default=0)
    down_votes = db.IntegerField(default=0)
    body = db.CharField(max_length=10000)
    created = db.DateTimeField(auto_now_add=True)
    author = db.ForeignKey(User)

    class Meta:
        abstract = True


class Question(QAValueObject):
    title = db.CharField(max_length=400)


class Answer(QAValueObject):
    checked = db.BooleanField(default=False)
    question = db.ForeignKey(Question)


class CValueObject(db.Model):
    body = db.CharField(max_length=1000)
    created = db.DateTimeField(auto_now_add=True)
    author = db.ForeignKey(User)

    class Meta:
        abstract = True


class QuestionComment(CValueObject):
    question = db.ForeignKey(Question, related_name='comments')


class AnswerComment(CValueObject):
    answer = db.ForeignKey(Answer, related_name='comments')
