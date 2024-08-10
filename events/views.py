from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Participant
from .forms import EventForm


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})


def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    return render(request, 'event_form.html', {'form': form})


def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'event_confirm_delete.html', {'event': event})


def add_participant(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Participant.objects.create(event=event, name=name, email=email)
        return redirect('event_detail', event_id=event.id)
    return render(request, 'add_participant.html', {'event': event})


