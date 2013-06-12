# Create your views here.
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponse
def register_event(request):
		wname=request.GET.get('name')
		return HttpResponse(wname)

	
