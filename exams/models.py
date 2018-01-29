from users.models import Base, User
from django.db import models


class Exam(Base):
    examnee = models.ManyToManyField(User, blank=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.name)


class Question(Base):
    ques_text = models.CharField(max_length=50)
    exam_name = models.ManyToManyField(Exam, blank=True)
    choice_1 = models.CharField(max_length=20)
    choice_2 = models.CharField(max_length=20)
    choice_3 = models.CharField(max_length=20)
    choice_4 = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.ques_text)


class Response(Base):
    response_field = models.TextField(null=True, blank=True, )
    user = models.CharField(max_length=20, null=True, blank=True)
    exam_fkey = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=True, null=True, related_name='exam_rel',
                                  related_query_name='exam_rel_q')
    question_fkey = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, null=True,
                                      related_name='ques_rel', related_query_name='ques_rel_q')

    def __str__(self):
        return "{}".format(self.user)
