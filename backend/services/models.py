from django.db import models
class Service(models.Model):
    title=models.CharField(max_length=160);slug=models.SlugField(unique=True);number=models.CharField(max_length=10)
    description=models.TextField();key_benefits=models.JSONField(default=list,blank=True);applications=models.TextField(blank=True)
    image=models.CharField(max_length=255,blank=True);active=models.BooleanField(default=True);created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=['number']
    def __str__(self): return self.title
