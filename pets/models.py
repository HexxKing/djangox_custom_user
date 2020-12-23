from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Pet(models.Model):
  name = models.CharField(max_length=64)
  description = models.TextField(default="")
  human = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('pet_detail', args=[str(self.id)])