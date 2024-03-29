# Generated by Django 2.2.5 on 2019-10-03 15:46

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0006_auto_20191002_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('tag', models.TextField(blank=True)),
                ('pitch', models.TextField(blank=True)),
                ('Page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_images', to='home.PortfolioPage')),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
