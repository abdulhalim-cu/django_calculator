from django.shortcuts import render
from .models import MediaType, CustomerType


def index(request):
	media_type = MediaType.objects.all()
	customers = CustomerType.objects.all()
	context = { "media_type": media_type, "customers": customers }
	if request.method == "POST":
		media = request.POST['media']
		customer = request.POST['customer']
		width = request.POST['width']
		height = request.POST['height']
	return render(request, 'calc/index.html', context)

