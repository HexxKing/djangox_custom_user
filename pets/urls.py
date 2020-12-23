from django.urls import path
from .views import PetListView, PetDetailView, PetUpdateView, PetDeleteView, PetCreateView

urlpatterns = [
  path('', PetListView.as_view(), name='pet_list'),
  path('<int:pk>/', PetDetailView.as_view(), name='pet_detail'),
  path('<int:pk>/update/', PetUpdateView.as_view(), name='pet_update'),
  path('<int:pk>/delete/', PetDeleteView.as_view(), name='pet_delete'),
  path('create/', PetCreateView.as_view(), name='pet_create'),
]