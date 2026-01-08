from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'name@example.com'}))
    organisation = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Organisation name'}))
    country = forms.ChoiceField(choices=[
        ('', 'Select your country'),
        ('ghana', 'Ghana'),
        ('nigeria', 'Nigeria'),
        ('cote-divoire', 'Côte d’Ivoire'),
        ('senegal', 'Senegal'),
        ('other', 'Other'),
    ], required=False, widget=forms.Select())
    phone_code = forms.ChoiceField(choices=[
        ('+233', '+233'),
        ('+234', '+234'),
        ('+225', '+225'),
        ('+221', '+221'),
    ], required=False, widget=forms.Select())
    phone = forms.CharField(max_length=20, required=False, widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))
    help = forms.ChoiceField(choices=[
        ('', 'Select an option'),
        ('project-design', 'Project Design & Feasibility'),
        ('implementation', 'Implementation Support'),
        ('m-e', 'Monitoring & Evaluation'),
        ('capacity-building', 'Capacity Building'),
        ('partnership', 'Partnership Opportunities'),
        ('other', 'Other'),
    ], required=False, widget=forms.Select())
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Tell us about your initiative...'}))