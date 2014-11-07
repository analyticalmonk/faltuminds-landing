from django.shortcuts import render

from .forms import EmailForm, joinForm
from .models import join
from .admin import get_ip

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

def home(request):
	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_join, created = join.objects.get_or_create(email = email)
	form = joinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False)

		email = form.cleaned_data['email']
		new_join_old, created = join.objects.get_or_create(email = email)
		if created:
			new_join_old.ip = get_ip(request)
			new_join_old.save()
		# new_join.ip = get_ip(request)
		# new_join.save()
		# print new_join_old.timestamp

	context = {"form":form}
	template = "home.html"
	return render(request, template, context)