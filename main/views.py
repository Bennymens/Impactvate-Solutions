from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
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

def news(request):
    return render(request, 'news.html')

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
            
            try:
                # Send email to company
                send_mail(
                    'Contact Form Submission',
                    f'From: {name} ({email})\nOrganisation: {organisation}\nCountry: {country}\nPhone: {phone_code} {phone}\nHow can we help: {help}\n\n{message}',
                    settings.DEFAULT_FROM_EMAIL,
                    ['benymento4@gmail.com'],  # Changed to your Gmail for testing
                    fail_silently=True,
                )
                
                # Send auto-response to user
                subject = 'Thank you for contacting Impactvate Solutions'
                html_message = render_to_string('emails/auto_response.html', {
                    'name': name,
                    'logo_url': settings.STATIC_URL + 'main/img/impact_logo-removebg-preview.png'
                })
                email_message = EmailMessage(
                    subject,
                    html_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                )
                email_message.content_subtype = 'html'
                email_message.send(fail_silently=True)
                
                return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
            except Exception as e:
                # Log the error and still show success to user
                print(f"Email sending failed: {e}")
                return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
