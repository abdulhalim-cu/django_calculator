from django.shortcuts import render
from .models import MediaType, CustomerType, SquareFeetRange


def index(request):
	media_type = MediaType.objects.all()
	customers = CustomerType.objects.all()
	context = { "media_type": media_type, "customers": customers }
	if request.method == "POST":
		media = request.POST['media']
		customer = request.POST['customer']
		width = request.POST.getlist('width')
		height = request.POST.getlist('height')
		total_print = request.POST.getlist('total_print')

		media_type = MediaType.objects.get(media_type=media)
		customer_type = CustomerType.objects.get(customer_type=customer)

		amount_list = []

		for i in range(len(width)):
			sqft = float(width[i]) * float(height[i]) * int(total_print[i])
			square_feet = int(sqft)
			if square_feet >= 1 and square_feet <= 100:
				sqft_range = '001-100'
			elif square_feet >= 101 and square_feet <= 200:
				sqft_range = '101-200'
			elif square_feet >= 201 and square_feet <= 300:
				sqft_range = '201-300'
			elif square_feet >= 301 and square_feet <= 400:
				sqft_range = '301-400'
			elif square_feet >= 401 and square_feet <= 500:
				sqft_range = '401-500'
			elif square_feet >= 501:
				sqft_range = '501+'
			else:
				msg = "Please insert valid width or height"
		
			amount = SquareFeetRange.objects.filter(media=media_type.id, customer=customer_type.id,square_feet=sqft_range)
			amount_list.append(float(amount[0].cost_per_sqft) * sqft)
		context["msg"] = amount_list
	return render(request, 'calc/index.html', context)


def ajax_rate(request, media, customer, square_feet):
	#cost = SquareFeetRange.objects.filter(media=media,
	#									   customer=customer,
	#									   square_feet='101-200').get()
	value = str(media)+str(customer)+str(square_feet)
	print(value)