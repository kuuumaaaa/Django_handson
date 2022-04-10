from django.http import HttpResponse


def index(request, question_id):
    return HttpResponse("Hello, world. You're at the polls index.")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)