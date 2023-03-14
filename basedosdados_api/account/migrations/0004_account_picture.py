# Generated by Django 4.1.7 on 2023-03-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_remove_account_picture"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="picture",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="profile_pictures",
                verbose_name="Imagem",
            ),
        ),
    ]
