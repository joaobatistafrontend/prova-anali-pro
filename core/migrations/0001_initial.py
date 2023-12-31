# Generated by Django 4.2.7 on 2023-11-15 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participacao', models.CharField(choices=[('cliente', 'Cliente'), ('tecnico', 'Técnico'), ('engenheiro', 'Engenheiro'), ('fiscal', 'Fiscal')], max_length=20)),
                ('motivos', models.TextField()),
                ('dados_contratante', models.TextField()),
                ('anexos', models.FileField(upload_to='anexos/')),
                ('normas_compliance', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
