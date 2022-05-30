# Generated by Django 3.2.13 on 2022-05-30 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mpsblog', '0010_remove_post_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreadComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='mpsblog.post')),
            ],
        ),
    ]
