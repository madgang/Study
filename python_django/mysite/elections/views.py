from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Candidate, Poll, Choice
from django.db.models import Sum
from django.http import HttpResponseNotFound

import datetime


# Create your views here.
def index(request):
    candidates = Candidate.objects.all()
    contexts = {'candidates' : candidates}
    return render(request,'elections/index.html',contexts)

def areas(request,area):
    today = datetime.datetime.now()
    try :
        poll = Poll.objects.get(area = area, start_date__lte = today,
        end_date__gte = today)
        candidates = Candidate.objects.filter(area = area)
    except:
        poll = None
        candidates = None
    contexts = {'candidates' : candidates,
                'area' : area,
                'poll': poll}
    return render(request, 'elections/area.html',contexts)

def polls(request, poll_id):
    poll = Poll.objects.get(pk = poll_id)
    selection = request.POST['choice']
    try:
        choice = Choice.objects.get(poll_id = poll.id, candidate_id = selection)
        choice.votes += 1
        choice.save()
    except:
        choice = Choice(poll_id = poll.id, candidate_id = selection, votes = 1)
        choice.save()
    return HttpResponseRedirect("/area/{}/results".format(poll.area))

def results(request,area):
    candidates = Candidate.objects.filter(area = area)
    polls = Poll.objects.filter(area = area)
    poll_results = []

    for poll in polls:
        result = {}
        result['start_date'] = poll.start_date
        result['end_date'] = poll.end_date

        # total_votes = Choice.objects.filter(poll_id = poll.id).        total_votes = Choice.objects.filter(poll_id = poll.id).aggregate(sum('votes'))
        total_votes = Choice.objects.filter(poll = poll).aggregate(Sum('votes'))

        result['total_votes'] = total_votes['votes__sum']

        rates = []
        for candidate in candidates:
            try:
                choice = Choice.objects.get(poll = poll, candidate = candidate)
                rates.append(
                    round(choice.votes * 100 / result['total_votes'] ,1 )
                    )
            except Exception as e:
                rates.append(0)
        print(rates)
        result['rates'] = rates
        poll_results.append(result)

    context = {'candidates' : candidates,
                'area':area,
                'poll_results':poll_results}

    return render(request, 'elections/results.html',context)


def candidates(request, name):
    try :
        candidate = Candidate.objects.get(name = name)
    except Exception as e:
        print(e)
        return HttpResponseNotFound("없는 페이지")
    return HttpResponse(candidate.name)
