# service_requests/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ServiceRequestForm
from .models import ServiceRequest

@login_required
def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('request_detail', pk=service_request.pk)
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/create_request.html', {'form': form})

@login_required
def request_list(request):
    requests = ServiceRequest.objects.filter(customer=request.user).order_by('-created_at')
    return render(request, 'service_requests/request_list.html', {'requests': requests})

@login_required
def request_detail(request, pk):
    request_obj = get_object_or_404(ServiceRequest, pk=pk, customer=request.user)
    return render(request, 'service_requests/request_detail.html', {'request': request_obj})