from django.db import models
class CompanyProfile(models.Model):
    name=models.CharField(max_length=200,default='ISSABUB Nigeria Limited')
    tagline=models.CharField(max_length=255,default='Your vision, our execution.')
    description=models.TextField()
    mission=models.TextField()
    vision=models.TextField()
    address=models.CharField(max_length=300)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    business_hours=models.JSONField(default=dict,blank=True)
    statistics=models.JSONField(default=dict,blank=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self): return self.name
