from django.shortcuts import render, redirect
from .models import Topic, Description
from .forms import DescriptionForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def index(request):
    topic = Topic.objects.all
    context = {'topic': topic}
    return render(request, 'Menu/Menu.html', context)


@login_required
def description(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    description = topic.description_set.filter(owner=request.user).order_by('date_added')
    context = {'description': description, 'topic': topic}
    return render(request, 'Menu/Description.html', context)


@login_required
def new_description(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = DescriptionForm()
    else:
        form = DescriptionForm(data=request.POST)
        if form.is_valid():
            new_description = form.save(commit=False)
            new_description.owner = request.user
            new_description.topic = topic
            new_description.save()
            return redirect('description', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'Menu/new_description.html', context)


@login_required
def edit_description(request, entry_id):
    description = Description.objects.get(id=entry_id)
    topic = description.topic
    if request.method != 'POST':
        form = DescriptionForm(instance=description)
    else:
        form = DescriptionForm(instance=description, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('description', topic_id=topic.id)
    context = {'description': description, 'topic': topic, 'form': form}
    return render(request, 'Menu/Edit_description.html', context)


@login_required
def delete_description(request, description_id):
    description = Description.objects.get(id=description_id)
    topic = description.topic
    description.delete()
    return redirect('description', topic_id=topic.id)

