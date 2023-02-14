from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from .models import Services, Blog, RequestQuote,Subscriber
from .forms import ContactFormService, ContactForm, CareerForm
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from rest_framework.generics import CreateAPIView
from .serializers import RequestQuoteSerializer
from django.core.mail import EmailMessage
from rest_framework.permissions import AllowAny
import json


# Create your views here.

class RequestQuoteApiView(CreateAPIView):
    serializer_class = RequestQuoteSerializer
    queryset = RequestQuote.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        #   recaptcha_response = request.POST.get('g-recaptcha-response')
        #     data = {
        #         'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        #         'response': recaptcha_response
        #     }
        #     r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        #     result = r.json()
        #     ''' End reCAPTCHA validation '''
        serializer.save()
        
        
        name = serializer.data['name']
        
        email = serializer.data['email']
        text = serializer.data['services']
        
        
        text = f'Name: {name} \nEmail: {email} \nServices: {text}'
        send_mail(
            'New REQUEST from Client',
            text,
            settings.EMAIL_HOST_USER,
            ['hi_usa@bridgerds.com'],
            fail_silently=False,
        )
      

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()[:3]
        context['4th_blog'] = Blog.objects.all()[3]
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ServicesView(FormView):
    template_name = 'services.html'
    form_class = ContactFormService

    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services_21'] = Services.objects.all()[:21]
        return context

    def form_valid(self, form):
        messages.success(
            self.request, 'Your message has been sent successfully')
        name = form.cleaned_data['name']
        company = form.cleaned_data['company']
        website = form.cleaned_data['website']
        message = form.cleaned_data['message']
        text = f'Name: {name} \nCompany: {company} \nWebsite: {website} \nMessage: {message}'
        send_mail(
            'New REQUEST from Client',
            text,
            settings.EMAIL_HOST_USER,
            ['hi_usa@bridgerds.com'],
            fail_silently=False,
        )
        form.save()
        return super().form_valid(form)

    


class ServiceDetailView(TemplateView):
    template_name = 'service-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BlogView(TemplateView):
    template_name = 'blogs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()
        return context


class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all()[:3]
        return context


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        messages.success(
            self.request, 'Your message has been sent successfully')
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        company = form.cleaned_data['company']
        website = form.cleaned_data['website']
        location = form.cleaned_data['location']
        message = form.cleaned_data['message']
        text = f'Name: {name} \nEmail: {email} \nCompany: {company} \nWebsite: {website} \nLocation: {location} \nMessage: {message}'
        send_mail(
            'New REQUEST from Client',
            text,
            settings.EMAIL_HOST_USER,
            ['hi_usa@bridgerds.com'],
            fail_silently=False,
        )
        form.save()
        return super().form_valid(form)


class CareerView(FormView):
    template_name = 'career.html'
    form_class = CareerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        messages.success(
            self.request, 'Your message has been sent successfully')
        resume = form.cleaned_data['resume']
        
        text = f'Resume: {resume}'
        
        email = EmailMessage(
        'New REQUEST from Client', 'Resume', settings.EMAIL_HOST_USER, ['hi_usa@bridgerds.com'])
        email.attach("document.pdf",form.cleaned_data['resume'].read())
        email.send()
        form.save()
        return super().form_valid(form)
        


class ApplyView(TemplateView):
    template_name = 'apply.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PrivacyView(TemplateView):
    template_name = 'policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReviewsView(TemplateView):
    template_name = 'reviews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


        
def Subscribe(request):
      data=json.loads(request.body)
      subscriber,created=Subscriber.objects.get_or_create(email=data["email"])
      subscriber.save()
      return JsonResponse("subscribed", safe=False)


def robots(request):
    return render(request, 'robots.txt', content_type='text/plain')