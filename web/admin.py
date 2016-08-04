from django.contrib import admin
from web.models import APP, Skill
from web.models import Profile

# Register your models here.

admin.site.register(Profile)
admin.site.register(APP)
admin.site.register(Skill)
