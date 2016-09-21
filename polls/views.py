from polls.models import Question, Choice
from django.http import HttpResponse

from functools import reduce

def index(request):
    output = ''

    for q in Question.objects.all():
        output += '<h4>' + str(q) + '</h4>'
        output += reduce(lambda p, c: p + '<p>' + str(c) + '</p>', q.choice_set.all(), '')

    return HttpResponse(output);

