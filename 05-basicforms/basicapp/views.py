from django.shortcuts import render
from . import forms
#from basicapp import forms
# Create your views here.

def index(request):
    return render(request, "basicapp/index.html")

def form_name_view(request):
    form = forms.FormName()
    
    if request.method == "POST":    # means someone hit something and posted something back
        form = forms.FormName(request.POST) # pass this request to forms
        if form.is_valid():                 # form validation
            # do something
            print("VALIDATION SUCCESS")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])
            
            
    
    return render(request, "basicapp/form_page.html", {'form': form})

