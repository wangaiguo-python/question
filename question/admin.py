from django.contrib import admin
from .models import Category,Question,Answer

# Register your models here.
'''
    超级管理员: admin
    密码:      question123
'''

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'id')


class AnswerInline(admin.TabularInline):
    model = Answer
    min_num = 4
    extra = 0
    can_delete = True

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ('name', 'id')
    list_display = ('name', 'id')

    inlines = [AnswerInline,]

# class AnswerAdmin(admin.ModelAdmin):
#     search_fields = ('name', 'id')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Answer, AnswerAdmin)