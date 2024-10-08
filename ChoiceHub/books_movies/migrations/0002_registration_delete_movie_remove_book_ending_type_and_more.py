# Generated by Django 5.1 on 2024-09-24 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.RemoveField(
            model_name='book',
            name='ending_type',
        ),
        migrations.RemoveField(
            model_name='book',
            name='is_character_driven',
        ),
        migrations.AddField(
            model_name='book',
            name='api_source',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='character',
            field=models.CharField(default='hero', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='character_vs_plot',
            field=models.CharField(blank=True, choices=[('Character', 'Character-driven'), ('Plot', 'Plot-driven')], max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='emotional_tone',
            field=models.CharField(default='lighthearted', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='ending',
            field=models.CharField(default='open', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='mood',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='narrative_style',
            field=models.CharField(default='third_person', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='pace',
            field=models.CharField(default='medium', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='romance',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='setting',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='themes',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='world_building_importance',
            field=models.CharField(default='somewhat', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='writing_style',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='length',
            field=models.CharField(default='medium', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
