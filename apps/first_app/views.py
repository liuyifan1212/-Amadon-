from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string

def index(request):
	return render(request,'first_app/index.html')
def process(request):
	items = {'1001': 19.99,
		 '1002': 24.99,
		 '1003': 4.99,
		 '1004': 49.99
		 }
	request.session['purchase'] = items[request.POST['product_id']] * int(request.POST['quantity'])

	if 'item_count' not in request.session:
		request.session['item_count'] = 0
	if 'total_spent' not in request.session:
		request.session['total_spent'] = 0

	request.session['item_count'] += int(request.POST['quantity'])
	request.session['total_spent'] += float(request.session['purchase'])
	return redirect('/result')
	


def result(request):
	return render(request,'first_app/2.html')
