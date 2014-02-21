from django import forms
from intersections.models import *

class IntersectionsForm(forms.ModelForm):
	
    class Meta:            # Django convention for namespaces
        model = Intersection

class DevicesForm(forms.ModelForm):
    class Meta:            # Django convention for namespaces
        model = Device

class AccidentsForm(forms.ModelForm):
    class Meta:            # Django convention for namespaces
        model = Accident

class RoadsForm(forms.ModelForm):
    class Meta:            # Django convention for namespaces
        model = Road