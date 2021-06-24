from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from .models import Question, Choice
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list' : latest_question_list}
    return render(request, poll/'index.html', context)

def details(request, question_id):
    try:
        question =Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, poll/'details.html', {'question' : question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, poll/'results.html', {'question': question})


def prefer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, poll/'details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.prefers+= 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results', args=(question_id,)))



