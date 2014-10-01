from django.contrib import admin

# Register your models here.
from .models import Account

# Displays Account model inside the Admin page
class AccountAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'created_at', 'updated_at']
	class Meta:
		model = Account

admin.site.register(Account, AccountAdmin)
