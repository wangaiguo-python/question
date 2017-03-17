from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import User, Score, Category, Question, Answer
from django.http.response import HttpResponseNotFound

# Create your views here.
def show_category(request):
    categorys = get_list_or_404(Category)
    return render(request,'question/index.html',
                  {
                      'categorys':categorys,
                  })

def show_question(request, id):
    category = get_object_or_404(Category, id = id)
    questions = Question.objects.filter(category=category)
    print(questions)
    if not questions:
        return HttpResponseNotFound()


    return render(request, 'question/question.html',
                  {
                      'questions':questions,
                  })

def show_answer(request, id):
    question = get_object_or_404(Question,id)
    answers = Answer.objects.filter(question=question)
    if not answers:
        return HttpResponseNotFound()
    return  render(request, 'question/question.html',
                   {
                       'answers' : answers,
                   })