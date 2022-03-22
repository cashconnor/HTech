from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import send_mail


class LandingPageView(generic.TemplateView):
    template_name = "index.html"

class AboutUsPageView(generic.TemplateView):
    template_name = "about-us.html"

class ServicesPageView(generic.TemplateView):
    template_name = "services.html"

class PartnersPageView(generic.TemplateView):
    template_name = "partners.html"

# class ContactUsPageView(generic.TemplateView):
#     template_name = "contact-us.html"
#     form_class = ContactForm

#     def get_success_url(self):
#         return reverse("index.html")

#     def form_valid(self, form):
#         send_mail(
#             subject = "A lead has been created",
#             message = "Go to the site to see the new lead",
#             from_email = "test@test.com",
#             recipient_list= ["test2@test.com"]
#         )
#         # messages.success(self.request, "You have successfully created a lead")
#         return super(ContactUsPageView, self).form_valid(form)

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = "H-Tech Website Submission"
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    subject + ' from ' + name, 
                    message, 
                    email, 
                    ['ccc262@cornell.edu'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('landing-page')
    return render(request, "contact-us.html", {'form': form})