from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PredictResult(models.Model):
    name = models.CharField(max_length=20, null=False)
    image = models.ImageField(null=False, blank=False, upload_to='images/')
    result = models.CharField(max_length=20)

    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self) -> str:
        return f'{self.name} :: {self.result}'
    
    class Meta:
        verbose_name_plural = 'Predict Result'