from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .shift import Shift

class IndexView(generic.ListView):
    template_name = 'shift_app/index.html'
    context_object_name = 'shifts'

    def get_queryset(self):
        return Shift.objects.all()