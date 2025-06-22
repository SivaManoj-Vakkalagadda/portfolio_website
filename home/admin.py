from django.contrib import admin
from .models import Profile, CodingProfile, Skill, Project, ContactInfo

admin.site.register(Profile)
admin.site.register(CodingProfile)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ContactInfo)