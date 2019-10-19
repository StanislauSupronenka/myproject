from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response

from market.forms import CreateDealForm
from market.models import Deal


@login_required
def rates(request):
    return render(request, 'rates.html')

@login_required
def create_deal(request):
    if request.method == 'POST':
        form = CreateDealForm(
            request.POST
        )
        if form.is_valid():
            deal = form.save()
            deal.owner = request.user
            deal.save()
            return render(request,'complete.html')
        else:
            print(form)
            form = CreateDealForm()
            return render(request, "create_deal.html", context={
                "form": form,
                "error": True
            })
    else:
        form = CreateDealForm()
        return render(request, "create_deal.html", context={
            "form": form
        })
@login_required
def deal_list(request):
    q = request.GET.get("q")
    page_num = request.GET.get("page", 1)
    deals = Deal.objects.filter(owner = request.user)
    return render(request, "deals.html", context={
        "deals": deals,
    })
@login_required
def get_stats(request):
    RUB = Deal.objects.filter(owner=request.user,currency_code='RUB')
    USD = Deal.objects.filter(owner=request.user,currency_code='USD')
    EUR = Deal.objects.filter(owner=request.user,currency_code='EUR')
    PLN = Deal.objects.filter(owner=request.user,currency_code='PLN')
    UAH = Deal.objects.filter(owner=request.user,currency_code='UAH')
    return render(request,'statisctic.html',
                  {'RUB':RUB,
                  'PLN': PLN,
                  'USD': USD,
                  'EUR': EUR,
                  'UAH': UAH
                   })

@login_required
def get_count(request):
    RUBc = Deal.objects.annotate(Count('currency_rate'))
    USDc= len(Deal.objects.filter(owner=request.user,currency_code='USD'))
    EURc = Deal.related_set.filter(owner=request.user,currency_code='EUR').count()
    PLNc = len(Deal.objects.filter(owner=request.user,currency_code='PLN'))
    UAHc = Deal.related_set.filter(owner=request.user,currency_code='UAH').count()
    print(RUBc)
    return render(request,'statisctic.html',
                  {'RUB':RUBc,
                  'PLN': PLNc,
                  'USD': USDc,
                  'EUR': EURc,
                  'UAH': UAHc
                   })