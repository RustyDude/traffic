from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from intersections.models import Intersection
from django.template import Context, loader, RequestContext
# Create your views here.


def intersections(request):
	intersection_list = Intersection.objects.all()
	t = loader.get_template('intersections/intersections.html')
	c = Context({'intersection_list': intersection_list,})
	return HttpResponse(t.render(c))
	

