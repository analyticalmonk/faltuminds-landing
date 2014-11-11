from django.contrib import admin

from .models import join

# def get_ip(request):
# 	try:
# 		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
# 		if x_forward:
# 			ip = x_forward.split(",")[0]
# 		else:
# 			ip = request.META.get("REMOTE_ADDR")
# 	except:
# 		ip = ""
# 	return ip

#CHECK OUT WTF THIS SHIZZZ PRECISELY MEANS!!
#CHECK OUT WTF THIS SHIZZZ PRECISELY MEANS!!
#CHECK OUT WTF THIS SHIZZZ PRECISELY MEANS!!

class JoinAdmin(admin.ModelAdmin):
	list_display = ["email", "friend", "timestamp", "update"]
	class Meta:
		model = join

admin.site.register(join, JoinAdmin)

#CHECK OUT WTF THIS SHIZZZ PRECISELY MEANS!!
#CHECK OUT WTF THIS SHIZZZ PRECISELY MEANS!!
#CHECK OUT WTF THIS SHIZZZ PRECISELY MEANS!!

