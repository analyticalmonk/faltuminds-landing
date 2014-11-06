from django.contrib import admin

from .models import join

#CHECK OUT WTF THIS SHIZZZ PRECISELY MEANS!!
#CHECK OUT WTF THIS SHIZZZ PRECISELY MEANS!!
#CHECK OUT WTF THIS SHIZZZ PRECISELY MEANS!!

class JoinAdmin(admin.ModelAdmin):
	list_display = ["email", "timestamp", "update"]
	class Meta:
		model = join

admin.site.register(join, JoinAdmin)

#CHECK OUT WTF THIS SHIZZZ PRECISELY MEANS!!
#CHECK OUT WTF THIS SHIZZZ PRECISELY MEANS!!
#CHECK OUT WTF THIS SHIZZZ PRECISELY MEANS!!

