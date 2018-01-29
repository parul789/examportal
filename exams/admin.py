from django.contrib import admin
from .models import Exam,Question,Response

class ExamModelAdmin(admin.ModelAdmin):
    list_display = ['id','name']
class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'ques_text','choice_1','choice_2','choice_3','choice_4']
class ResponseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','exam_fkey','question_fkey','response_field']

admin.site.register(Exam,ExamModelAdmin)
admin.site.register(Question,QuestionModelAdmin)
admin.site.register(Response,ResponseModelAdmin)

