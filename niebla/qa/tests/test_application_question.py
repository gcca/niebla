from django.test import TestCase
from qa.models import Question, QuestionComment
from qa import application


class ApplicationQuestionTests(TestCase):

    def setUp(self):
        from qa.models import Question, User
        user = User.objects.create()
        self.user = user

    def test_ask(self):
        question = Question(title='Q_ask', author=self.user)
        application.question.ask(question)

        question_test = Question.objects.get(title='Q_ask')

        self.assertIsNotNone(question_test)

    def test_vote_up(self):
        votes_to_up = 1
        question = Question.objects.create(title='Q_vote_up',
                                           up_votes=votes_to_up,
                                           author=self.user)
        application.question.vote_up(question)

        question_test = Question.objects.get(title='Q_vote_up')
        self.assertEqual(question_test.up_votes,
                         votes_to_up + 1)

    def test_vote_down(self):
        votes_to_down = 1
        question = Question.objects.create(title='Q_vote_down',
                                           down_votes=votes_to_down,
                                           author=self.user)
        application.question.vote_down(question)

        question_test = Question.objects.get(title='Q_vote_down')
        self.assertEqual(question_test.down_votes,
                         votes_to_down + 1)

    def test_comment(self):
        question = Question.objects.create(title='Q_comment',
                                           author=self.user)
        comment = QuestionComment.objects.create(body='comment',
                                         author=self.user,
                                         question=question)

        #application.question.comment(question, comment)

        question_test = Question.objects.get(title='Q_comment')

        print(question_test.comments.get())

        comment = QuestionComment.objects.create(body='comment',
                                         author=self.user,
                                         question=question)

        self.assertEqual(comment, question_test.comments.get())
