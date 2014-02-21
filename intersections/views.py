from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from intersections.models import *
from django.template import Context, loader, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_user(request):
	logout(request)
	username = password = ''
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				#t = loader.get_template('intersections/home.html')
				#c =  Context({'username' : username,})
				return HttpResponseRedirect('/intersections/')
				#return HttpResponse(t.render(c))
			else:
				return render_to_response("login/login.html",{'inactive': True })
		else:
			return render_to_response("login/login.html",{'invalid': True })
	return render_to_response('login/login.html', context_instance=RequestContext(request))


	
@login_required(login_url='/login/')

def intersections(request):
	intersection_list = Intersection.objects.all()
	t = loader.get_template('intersections/intersections.html')
	c = Context({'intersection_list': intersection_list,})
	return HttpResponse(t.render(c))

@login_required(login_url='/login/')
	
def roads(request):
	road_list = Road.objects.all()
	t = loader.get_template('intersections/road.html')
	c = Context({'road_list': road_list,})
	return HttpResponse(t.render(c))
	
@login_required(login_url='/login/')	
	
def accidents(request):
	accident_list = Accident.objects.all()
	t = loader.get_template('intersections/accident.html')
	c = Context({'accident_list': accident_list,})
	return HttpResponse(t.render(c))
	
@login_required(login_url='/login/')	

def devices(request):
	device_list = Device.objects.all()
	t = loader.get_template('intersections/device.html')
	c = Context({'device_list': device_list,})
	return HttpResponse(t.render(c))

def homepage(request):
	return HttpResponseRedirect('/login/')
