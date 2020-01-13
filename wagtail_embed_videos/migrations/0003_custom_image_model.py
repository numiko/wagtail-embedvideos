from django.db import migrations, models
import django.db.models.deletion
from wagtail.images import get_image_model_string

class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_embed_videos', '0002_auto_20180822_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wagtail_embed_videos.embedvideo',
            name='thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=get_image_model_string(), verbose_name='Thumbnail'),
        ),
    ]
