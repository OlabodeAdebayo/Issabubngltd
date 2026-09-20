from django.db import models
class QuoteRequest(models.Model):
    STATUS=[('new','New'),('reviewing','Reviewing'),('quoted','Quoted'),('closed','Closed')]
    full_name=models.CharField(max_length=150);email=models.EmailField();phone=models.CharField(max_length=50);service=models.CharField(max_length=160)
    project_location=models.CharField(max_length=200,blank=True);message=models.TextField();status=models.CharField(max_length=20,choices=STATUS,default='new');created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'{self.full_name} — {self.service}'
