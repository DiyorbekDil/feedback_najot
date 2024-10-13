from django.shortcuts import render
from team_faq.models import TeamModel, FAQModel
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


def _404_page_view(request):
    return render(request, 'main/404/404.html')
