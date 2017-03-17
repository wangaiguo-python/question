from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField('名称', max_length=70)

    def __str__(self):
        return self.name



class Score(models.Model):
    score = models.FloatField('分数')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    user = models.ForeignKey('User', verbose_name='用户')

    def __str__(self):
        return self.score

    class Meta:
        ordering = ['-created_time']



class Category(models.Model):
    name = models.CharField('分类', max_length=100)
    description = models.TextField('描述', blank=True, null=True, help_text='简单描述,可填可不填')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name



class Question(models.Model):
    name = models.TextField('问题')
    category = models.ForeignKey('Category', verbose_name='问题分类')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = verbose_name



class Answer(models.Model):
    # answer_one = models.CharField('A')
    # answer_two = models.CharField('B')
    # answer_three = models.CharField('C')
    # answer_four = models.CharField('D')

    name = models.CharField('答案', max_length=512)
    correct = models.BooleanField('正确答案', help_text='勾选为正确答案')
    question = models.ForeignKey('Question', verbose_name='问题', related_name="answers")
    def __str__(self):
        return "{} - {}".format('答案', self.id)
    class Meta:
        verbose_name = '答案'
        verbose_name_plural = verbose_name
