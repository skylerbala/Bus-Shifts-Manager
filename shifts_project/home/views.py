from django.shortcuts import render
from django.views import generic

class HomeView(generic.View):
  template_name = 'home/index.html'
   
  def get(self, request):
    return render(request, self.template_name, {})