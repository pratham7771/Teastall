from django.contrib import admin 
from .models import signupuser,contactuser,paymentuser,usersuggestion

# Register your models here.
admin.site.register(signupuser)
admin.site.register(contactuser)
admin.site.register(paymentuser)
admin.site.register(usersuggestion)
