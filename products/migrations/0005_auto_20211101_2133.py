# Generated by Django 3.2.7 on 2021-11-01 21:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0004_productreview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productreview',
            options={'ordering': ['-date_added']},
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='stars',
        ),
        migrations.AddField(
            model_name='productreview',
            name='rating',
            field=models.IntegerField(choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')], default=3),
        ),
        migrations.AddField(
            model_name='productreview',
            name='title',
            field=models.CharField(default='Review', max_length=254),
        ),
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='products.product'),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
