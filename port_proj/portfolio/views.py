from django.shortcuts import render, redirect
from .models import ContactSubmission
from django.urls import reverse
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')
def contact(request):
    return render(request, 'contact.html')

# Create your views here.
def submit_contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Check if all required fields are provided
        if name and email and phone and message:
            # Save the form data to the database
            submission = ContactSubmission.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            print('Success')
            return redirect('home')  # Assuming you have a URL named 'home'
        else:
            print('Fail')
            # Handle case where required fields are not provided
            return render(request, 'contact.html', {'error': 'Please fill in all required fields.'})
    
    return render(request, 'contact.html')
def redirect_with_delay(url_name, delay_seconds):
    url = reverse(url_name)
    return f"""
        <script>
            setTimeout(function() {{
                window.location.href = "{url}";
            }}, {delay_seconds * 1000});
        </script>
    """