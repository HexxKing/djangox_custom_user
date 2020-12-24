from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Pet
from django.urls import reverse_lazy

class PetListView(ListView):
  template_name = "pets/pet-list.html"
  model = Pet

class PetDetailView(DetailView):
  template_name = "pets/pet-detail.html"
  model = Pet

class PetUpdateView(UpdateView):
  template_name = "pets/pet-update.html"
  model = Pet
  fields = ['name', 'description', 'human']

class PetDeleteView(DeleteView):
  template_name = "pets/pet-delete.html"
  model = Pet
  success_url = reverse_lazy('pet_list')

class PetCreateView(CreateView):
  template_name = "pets/pet-create.html"
  model = Pet
  fields = ['name', 'description', 'human']