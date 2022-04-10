from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question

# request is a HttpRequest object.
# request is generated when user accesses th URL.
# request has many methods.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)
    # return HttpResponse(template.render(context, request))
    # render() takes two arguments:
    # 1. template name
    # 2. context dictionary
    # reder() returns an HttpResponse object.
    # render() is a shortcut for loader.get_template().render()

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    # get_object_or_404() is a shortcut for Question.objects.get()
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
