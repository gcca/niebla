"""Answer use cases.

.. todo:: Restrict the number of questions returned.

"""
from qa.models import Question


def ask(question):
    question.save()


def vote_up(question):
    question.up_votes += 1
    question.save()


def vote_down(question):
    question.down_votes += 1
    question.save()


def comment(question, comment):
    # comment.question = question
    comment.save()
