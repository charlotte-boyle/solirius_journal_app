from django.http import HttpResponse
from django.shortcuts import render
from journal.models import Resource
from django.template import loader
from journal.forms import ResourceForm
from django.shortcuts import redirect


# Create your views here.
def home(request):
    resources = Resource.objects.all()
    return render(request, 'home.html', {
        'journal_resource': resources
    })


def add_resource(request, resource_id=None):
    if resource_id:
        main_message = 'Update resource'
        resource = Resource.objects.get(id=resource_id)
    else:
        main_message = 'Create new resource'
    if request.method == 'POST':
        if resource_id:
            resource_form = ResourceForm(request.POST, instance=resource)
        else:
            resource_form = ResourceForm(request.POST)
        resource_form.save()
        return redirect('journal:home')
    else:
        if resource_id:
            resource_form = ResourceForm(instance=resource)
        else:
            resource_form = ResourceForm()
    return render(request, 'new_resource.html', {
        'resource_form': resource_form,
        'main_message': main_message
    })


def delete_resource(request, resource_id=None):
    if resource_id:
        main_message = 'Delete resource'
        resource = Resource.objects.get(pk=resource_id)
    else:
        return redirect('journal:home')
    if request.method == 'POST':
        if resource_id:
            resource_form = ResourceForm(request.POST, instance=resource)
        else:
            resource_form = ResourceForm(request.POST)
        resource.delete()
        return redirect('journal:home')
    else:
        if resource_id:
            resource_form = ResourceForm(instance=resource)
        else:
            resource_form = ResourceForm()
    return render(request, 'delete_resource.html', {
        'resource_form': resource_form,
        'main_message': main_message
    })


def profile(request):
    return render(request, 'profile.html')
