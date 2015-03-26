"""
Domain model.
"""

from django.db import models as db
from django.contrib.auth.models import User


class Comment(db.Model):
    content = db.CharField(max_length=500)
    user = db.ForeignKey(User)


class QAValueObject(db.Model):
    up_votes = db.IntegerField(default=0)
    down_votes = db.IntegerField(default=0)
    content = db.CharField(max_length=2000)
    comments = db.ManyToManyField(Comment)
    user = db.ForeignKey(User)

    class Meta:
        abstract = True


class Question(QAValueObject):
    title = db.CharField(max_length=200)


class Answer(QAValueObject):
    checked = db.BooleanField(default=False)
