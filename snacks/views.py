from django.shortcuts import render
from .models import Snack
from django.views.generic import ListView, DetailView

# Create your views here.
class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack

class SnackDetailView(DetailView):
	template_name = 'snack_detail.html'
	model = Snack