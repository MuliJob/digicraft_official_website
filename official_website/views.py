from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def service_detail(request):
  return render(request, 'service-details.html')

def portfolio_detail(request):
  return render(request, 'portfolio-details.html')