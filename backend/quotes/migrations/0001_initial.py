from django.db import migrations,models
class Migration(migrations.Migration):
    initial=True;dependencies=[]
    operations=[migrations.CreateModel(name='QuoteRequest',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('full_name',models.CharField(max_length=150)),('email',models.EmailField(max_length=254)),('phone',models.CharField(max_length=50)),('service',models.CharField(max_length=160)),('project_location',models.CharField(blank=True,max_length=200)),('message',models.TextField()),('status',models.CharField(choices=[('new','New'),('reviewing','Reviewing'),('quoted','Quoted'),('closed','Closed')],default='new',max_length=20)),('created_at',models.DateTimeField(auto_now_add=True))])]
