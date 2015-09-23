# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import notifications.models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notification_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='level',
            field=models.CharField(choices=[('success', 'success'), ('info', 'info'), ('warning', 'warning'), ('error', 'error')], max_length=20, default='info'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='timestamp',
            field=models.DateTimeField(default=notifications.models.now),
        ),
    ]
