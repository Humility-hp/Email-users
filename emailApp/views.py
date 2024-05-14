from django.shortcuts import render
from .forms import Nameform
from django.core.mail import send_mail
# Create your views here.
def get_name(request):
 form = Nameform()
 # subject= form['subject']
 # message = form['message']
 # sender = form['sender']
 # cc_myself = form['cc_myself']
 return render(request, "name.html", {'form':form})
