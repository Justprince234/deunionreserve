from django.contrib import admin

from .models import UpdateUser

# Register your models here.
class UpdateUserAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'surname', 'date_updated')
  list_display_links = ('id', 'first_name')
  search_fields = ('first_name',)
  list_per_page = 25

admin.site.register(UpdateUser, UpdateUserAdmin)