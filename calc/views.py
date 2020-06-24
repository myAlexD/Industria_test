from django.shortcuts import render,HttpResponse
from .models import Currency
from .forms import CurrencyForm
from django.http import JsonResponse


def calc(request):
    context = {}
    context["form"] = Currency.objects.all()
    if request.method == "GET":
        return render(request, "calc.html", context)
    if request.method == "POST":
        options = {}
        input_in_leva = float(request.POST["currency_in_amt"]) * Currency.objects.filter(id = request.POST["currency_in"]).first().rate
        output = input_in_leva * Currency.objects.filter(id = request.POST["currency_out"]).first().rev_rate
        options["output"] = "{:.2f}".format(output)
        print(options)
        return JsonResponse(options)


def home(request):
    context = {}

    for curr in Currency.objects.all():
        context[str(curr.name)] = [curr.abv, curr.rate, curr.rev_rate]
    print(context)
    return render(request, "home.html", {"data": context})
    #context = {x:x.rate for x in Currency.objects.all()}
    #print(context)


 