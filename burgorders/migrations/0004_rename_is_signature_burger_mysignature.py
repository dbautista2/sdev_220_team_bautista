# Generated by Django 5.0 on 2023-12-13 18:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("burgorders", "0003_burger_is_signature"),
    ]

    operations = [
        migrations.RenameField(
            model_name="burger",
            old_name="is_signature",
            new_name="MySignature",
        ),
    ]
