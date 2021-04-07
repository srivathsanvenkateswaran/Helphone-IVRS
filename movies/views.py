from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.voice_response import VoiceResponse
from django.urls import reverse 
import time


@csrf_exempt
def answer(request: HttpRequest) -> HttpResponse:
    vr = VoiceResponse()
    vr.say('Welcome to Elder Helpline!') 
    with vr.gather(
       action=reverse('choose-language'),
       numDigits=1,
       timeout=20,
    ) as gather:
    	gather.play('https://ruby-salamander-5141.twil.io/assets/Lang%20options.mp3') 
    	
    vr.say('We did not receive your selection')
    vr.redirect('')
    return HttpResponse(str(vr), content_type='text/xml')
# Create your views here.

@csrf_exempt
def choose_language(request: HttpRequest) -> HttpResponse:
	vr = VoiceResponse()
	
	digits = request.POST.get('Digits')
	
	if(digits=='1'):
		with vr.gather(
       		   action=reverse('choose-service'),
       		   numDigits=1,
       		   timeout=20,
    		) as gather:
    		    gather.play('https://ruby-salamander-5141.twil.io/assets/Tamil%20Options.mp3') 
	
	elif(digits=='2'):
		with vr.gather(
       		   action=reverse('choose-service'),
       		   numDigits=1,
       		   timeout=20,
    		) as gather:
    		    gather.say('Press 1 for Hospital, 2 for Medicine needs, 3 for Grocery needs and 4 for Dairy needs') 
		
	elif(digits=='3'):
		with vr.gather(
       		   action=reverse('choose-service'),
       		   numDigits=1,
       		   timeout=20,
    		) as gather:
    		    gather.play('https://ruby-salamander-5141.twil.io/assets/Hindi%20Options.mp3') 
		
	else:
		vr.say(f'You have entered {(digits)}')
	return HttpResponse(str(vr), content_type='text/xml')
	
	
@csrf_exempt
def choose_service(request: HttpRequest) -> HttpResponse:
	vr = VoiceResponse()
	
	digits = request.POST.get('Digits')
	
	if(digits=='1'):
		vr.say('You are being connected to the nearest Hospital')
		vr.dial('+918248754430')
	
	elif(digits=='2'):
		vr.say('You are being connected to the nearest Pharmacy')
		vr.dial('+918248754430')
		
	elif(digits=='3'):
		vr.say('You are being connected to the nearest Supermarket')
		vr.dial('+918248754430')
		
	elif(digits=='4'):
		vr.say('You are being connected to the nearest Dairy Centre')
		vr.dial('+918248754430')
		
	else:
		vr.say(f'You have entered {(digits)}')
	return HttpResponse(str(vr), content_type='text/xml')
