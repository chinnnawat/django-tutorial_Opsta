from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list" : latest_question_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    else:
        return render(request, "polls/detail.html", {"question": question})



def results(request, question_id):
    response = "You are Looking the result of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # choice_set.get() = method orm
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist) :
        return render(
            request, "polls/detail.html", {
                "question": question,
                "error_message" : "You didn't select a choice.",
            }
        )
    else:
        # increase vote point
        selected_choice.votes = F("votes")+1 # votes = instrucs database(ORM)
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id, )))
        
