from django.shortcuts import render
from Team_FAQ.models import TeamModel, FAQModel
from offers_problems.models import OfferModel
# Create your views here.


def index_view(request):
    team = TeamModel.objects.all()
    faqs = FAQModel.objects.all()
    offers = OfferModel.objects.all()
    context = {
        'team': team,
        'faqs': faqs,
        'offers': offers,
    }
    return render(request, 'index.html', context=context)
