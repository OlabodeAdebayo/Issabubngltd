from django.db import models
class Project(models.Model):
    CATEGORY_CHOICES=[('commercial','Commercial'),('residential','Residential'),('retrofitting','Retrofitting & Restoration'),('structural','Structural Steel')]
    title=models.CharField(max_length=220);slug=models.SlugField(unique=True);category=models.CharField(max_length=30,choices=CATEGORY_CHOICES)
    description=models.TextField();location=models.CharField(max_length=180,blank=True);image=models.CharField(max_length=255,blank=True);featured=models.BooleanField(default=False);created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=['id']
    def __str__(self): return self.title
