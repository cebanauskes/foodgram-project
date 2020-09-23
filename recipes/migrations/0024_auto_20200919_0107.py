from django.db import migrations
import os
import csv
from pathlib import Path


def get_ingredients(apps, schema_editor):
    Ingredient = apps.get_model('recipes', 'Ingredient')
    
    csv_file=os.path.join('ingredients.csv')
    data = csv.reader(open(csv_file, encoding='utf-8'), delimiter = ',')
    try:
        obj_list = [
            Ingredient( 
                title=row[0],
                dimension='г' if row[1] == '' else row[1],
            )
            for row in list(data)
        ]
    except (IndexError):
        return 'IndexError'

    Ingredient.objects.bulk_create(obj_list)


def delete_ingredients(apps, schema_editor):
    Ingredient = apps.get_model('recipes', 'Ingredient')
    Ingredient.objects.all().delete()


def get_tags(apps, schema_editor):
    Tag = apps.get_model('recipes', 'Tag')
    
    csv_file=os.path.join('tags.csv')
    data = csv.reader(open(csv_file, encoding='utf-8'), delimiter = ',')
    try:
        obj_list = [
            Tag( 
                title = row[1],
                color = row[2],
                value = row[3],
            )
            for row in list(data)
        ]
    except (IndexError):
        return 'IndexError'

    Tag.objects.bulk_create(obj_list)


def delete_tags(apps, schema_editor):
    Tag = apps.get_model('recipes', 'Tag')
    Tag.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(get_ingredients, reverse_code=delete_ingredients),
        migrations.RunPython(get_tags, reverse_code=delete_tags),
    ]
