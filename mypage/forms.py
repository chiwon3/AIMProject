from django.forms import ModelForm
from .models import *

class Urlform1(ModelForm):
    class Meta:
        model = CustomUrl1
        fields = ('title',"url")

class Urlform2(ModelForm):
    class Meta:
        model = CustomUrl2
        fields = ('title',"url")

class Urlform3(ModelForm):
    class Meta:
        model = CustomUrl3
        fields = ('title',"url")