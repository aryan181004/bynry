# support/views.py
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from service_requests.models import ServiceRequest
from .forms import SupportNoteForm

def is_support_rep(user):
    return user.is_staff or user.groups.filter(name='Support Representatives').exists()

@user_passes_test(is_support_rep)
def support_dashboard(request):
    requests = ServiceRequest.objects.filter(status__in=['PENDING', 'IN_PROGRESS']).order_by('created_at')
    return render(request, 'support/support_dashboard.html', {'requests': requests})

@user_passes_test(is_support_rep)
def manage_request(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    
    if request.method == 'POST':
        form = SupportNoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.service_request = service_request
            note.support_rep = request.user
            note.save()
            
            # Update request status if needed
            service_request.status = request.POST.get('status', service_request.status)
            service_request.save()
            
            return redirect('manage_request', pk=pk)
    else:
        form = SupportNoteForm()
    
    support_notes = service_request.support_notes.all()
    return render(request, 'support/request_management.html', {
        'request': service_request,
        'form': form,
        'support_notes': support_notes
    })