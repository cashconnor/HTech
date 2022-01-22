from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render


class LandingPageView(generic.TemplateView):
    template_name = "index.html"

class AboutUsPageView(generic.TemplateView):
    template_name = "about-us.html"

class ServicesPageView(generic.TemplateView):
    template_name = "services.html"

class PartnersPageView(generic.TemplateView):
    template_name = "partners.html"

class ContactUsPageView(generic.TemplateView):
    template_name = "contact-us.html"