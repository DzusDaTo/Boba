# Generated by Django 4.0.3 on 2022-11-15 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_hosting', '0003_alter_video_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, verbose_name='IP-адрес')),
            ],
            options={
                'verbose_name': 'IP',
                'verbose_name_plural': 'IP',
            },
        ),
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='post_views', to='video_hosting.ip'),
        ),
    ]