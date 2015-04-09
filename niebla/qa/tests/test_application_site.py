from django.test import TestCase
from qa import application


class ApplicationSiteTests(TestCase):

    def setUp(self):
        from datetime import datetime
        from qa.models import Question, User
        from django.utils.timezone import utc

        user = User.objects.create()

        q1 = Question.objects.create(title='Q1',
                                     up_votes=10,
                                     down_votes=4,
                                     author=user)
        q1.created = datetime(2015, 5, 15, tzinfo=utc)
        q1.save()

        q2 = Question.objects.create(title='Q2',
                                     up_votes=12,
                                     down_votes=2,
                                     author=user)
        q2.created = datetime(2015, 6, 15, tzinfo=utc)
        q2.save()

        q3 = Question.objects.create(title='Q3',
                                     up_votes=7,
                                     down_votes=6,
                                     author=user)
        q3.created = datetime(2015, 7, 15, tzinfo=utc)
        q3.save()

        self.questions_ordered_by_datetime = [q3, q2, q1]
        self.questions_ordered_by_votes = [q2, q1, q3]

    def test_questions_by_datetime(self):
        """
        application.site.questions_by_datetime() should return a
        question `list` ordered by `created` attribute.
        """
        questions_to_test = application.site.questions_by_datetime()
        self.assertListEqual(questions_to_test,
                             self.questions_ordered_by_datetime)

    def test_questions_by_votes(self):
        """
        application.site.questions_by_votes() should return a
        question `list` ordered by `up_votes - down_votes` value.
        """
        questions_to_test = application.site.questions_by_votes()
        self.assertListEqual(questions_to_test,
                             self.questions_ordered_by_votes)
