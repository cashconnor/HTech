from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render


class LandingPageView(generic.TemplateView):
    template_name = "index.html"


def landing_page(request):
    return render(request, "landing.html")