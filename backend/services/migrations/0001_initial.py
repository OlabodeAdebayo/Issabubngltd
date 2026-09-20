from django.db import migrations,models
class Migration(migrations.Migration):
    initial=True;dependencies=[]
    operations=[migrations.CreateModel(name='Service',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('title',models.CharField(max_length=160)),('slug',models.SlugField(max_length=50,unique=True)),('number',models.CharField(max_length=10)),('description',models.TextField()),('key_benefits',models.JSONField(blank=True,default=list)),('applications',models.TextField(blank=True)),('image',models.CharField(blank=True,max_length=255)),('active',models.BooleanField(default=True)),('created_at',models.DateTimeField(auto_now_add=True))]),migrations.AlterModelOptions(name='service',options={'ordering':['number']})]
