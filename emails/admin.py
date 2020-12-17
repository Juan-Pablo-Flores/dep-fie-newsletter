from django.contrib import admin
from .models import InterestGroup, Subscriber, SentEmail

admin.site.register(InterestGroup)
admin.site.register(Subscriber)
admin.site.register(SentEmail)