from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Award, Options
from django.urls import reverse
import matplotlib.pyplot as plt
import numpy as np
import os
from . import static
from django.templatetags.static import static
import glob
# Create your views here.

def awards(request):
    AwardListing = list(Award.objects.all())
    return render(request, 'awards/awards.html', {'Award': Award, 'AwardList': AwardListing})
    
def voting(request, award_id):
    award = get_object_or_404(Award, pk=award_id)
    OptionListing = list(award.options_set.all())
    print(OptionListing[0].option_text)
    return render(request, 'awards/voting.html', {'award': award, 'OptionListing': OptionListing, 'id': award_id})

def vote(request, award_id):
    award = get_object_or_404(Award, pk=award_id)
    try:
        selected_choice = award.options_set.get(pk=request.POST['votingfor'])
        print(selected_choice)
        # selected_choice.votes += 1
        # selected_choice.save()
        # OptionListing = list(award.options_set.all())
        # return render(request, 'awards/results.html', {'award': award, 'OptionListing': OptionListing})
    except (KeyError, Options.DoesNotExist):
        return HttpResponse("bruuh")
    else:
        selected_choice.votes += 1
        selected_choice.save()
        OptionListing = list(award.options_set.all())
        # return render(request, 'awards/results.html', {'award': award, 'OptionListing': OptionListing})
        return HttpResponseRedirect(reverse('awards:results', args=(award_id,)))
    #     OptionListing = list(award.options_set.all())
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     return render(request, 'awards/results.html', {'award': award, 'OptionListing': OptionListing})


    
 
def results(request, award_id):
    award = get_object_or_404(Award, pk=award_id)
    OptionListing = list(award.options_set.all())
    # try:
    #     print(static('awards/img/graphs/my_plot.png'))
    #     midyearsotbawards/awards/static
    #     os.remove(".{0}".format(static('awards/img/graphs/my_plot.png')))
    # except FileNotFoundError:
    #     votes=[]
    #     mylabels = []
    #     for option in OptionListing:
    #         votes+=[option.votes]
    #         mylabels+=["{0}({1})".format(option, option.votes)]
    #     z = np.array(votes)
    #     plt.pie(z, labels = mylabels)
    #     plt.savefig(static('awards/img/graphs/my_plot.png'))
    files = glob.glob('awards/static/awards/img/graphs/*')
    for f in files:
        os.remove(f)
    votes=[]
    mylabels = []
    for option in OptionListing:
        votes+=[option.votes]
        mylabels+=["{0}({1})".format(option, option.votes)]
    z = np.array(votes)
    plt.clf()
    plt.pie(z, labels = mylabels)
    files = glob.glob('awards/static/awards/img/graphs/*')
    plt.savefig('awards/static/awards/img/graphs/my_plot.png')
    return render(request, 'awards/results.html', {'awards': Award, 'OptionListing': OptionListing})

        

