from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings

def home(request): return render(request, 'main/home.html')
def about(request): return render(request, 'main/about.html')
def subjects(request): return render(request, 'main/subjects.html')
def work(request): return render(request, 'main/work.html')
def skills(request): return render(request, 'main/skills.html')
def projects(request): return render(request, 'main/projects.html')
# def contact(request): return render(request, 'main/contact.html')

def contact(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"Contact from {form.cleaned_data['name']}"
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']
            recipients = [settings.EMAIL_HOST_USER]

            send_mail(subject, message, sender, recipients)
            sent = True
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {'form': form, 'sent': sent})
