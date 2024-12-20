from django.contrib import admin
from .models import Member

# Model Registration
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)

admin.site.register(Member, MemberAdmin)

