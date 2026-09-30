from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="quoterequest",
            name="email_sent",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="quoterequest",
            name="email_sent_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="quoterequest",
            name="email_error",
            field=models.TextField(blank=True),
        ),
    ]
