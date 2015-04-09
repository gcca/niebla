"""Site use cases.

This module contains functions to build the parts of the main pages.

.. todo:: Restrict the number of questions returned.

"""
from qa.models import Question


def questions_by_datetime():
    """Returns a question list ordered by creation date-time, from the
    most recent question to the latest."""
    return list(Question.objects.order_by('-created'))


def questions_by_votes():
    """Returns a question list ordered by score = up votes - down votes."""
    # Be carefull with `extra` method
    return list(Question.objects
                .extra(select={'score': 'up_votes - down_votes'})
                .order_by('score')
                .reverse())
