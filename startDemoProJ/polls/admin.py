from django.contrib import admin

from .models import Question, Choice

# Add to ORM page
admin.site.register(Question)
admin.site.register(Choice)