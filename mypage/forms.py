from django.forms import ModelForm
from .models import tab11

class Tabform(ModelForm):
    class Meta:
        model = tab11
        fields = ('title',"result")