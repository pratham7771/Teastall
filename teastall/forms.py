
from charset_normalizer import models
from django import forms

from .models import signupuser
from .models import paymentuser
from .models import usersuggestion,contactuser


class signupForm(forms.ModelForm):
    class Meta:
        model=signupuser
        fields='__all__'
        #fields=['stfirstname','stlastname','username','password','stcity','mo']

class paymentForm(forms.ModelForm):
    class Meta:
        model=paymentuser
        fields='__all__'

class suggestionform(forms.ModelForm):
    class Meta:
        model=usersuggestion
        fields='__all__'

class contactForm(forms.ModelForm):
    class Meta:
        model=contactuser
        fields='__all__'