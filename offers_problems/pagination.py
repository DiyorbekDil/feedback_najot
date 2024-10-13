from django.core.paginator import Paginator
from django.shortcuts import render
from offers_problems.models import OfferModel, ProblemModel


def index_view(request):
    category = request.GET.get('category', 'offers')

    if category == 'demands':
        items_list = ProblemModel.objects.all()
    else:
        items_list = OfferModel.objects.all()

    paginator = Paginator(items_list, 3)
    page_number = request.GET.get('page')
    items = paginator.get_page(page_number)

    return render(request, 'main/offers/offer.html', {'items': items, 'category': category})

