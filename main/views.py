from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def partnership(request):
    return render(request, 'partnership.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            organisation = form.cleaned_data['organisation']
            country = form.cleaned_data['country']
            phone_code = form.cleaned_data['phone_code']
            phone = form.cleaned_data['phone']
            help = form.cleaned_data['help']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                'Contact Form Submission',
                f'From: {name} ({email})\nOrganisation: {organisation}\nCountry: {country}\nPhone: {phone_code} {phone}\nHow can we help: {help}\n\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                ['your-email@example.com'],  # Replace with your email
                fail_silently=False,
            )
            # You can add a success message or redirect
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
