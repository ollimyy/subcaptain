# Generated by Django 4.2.1 on 2023-05-30 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subcaptain', '0002_rename_user_recurringpayment_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentcategory',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recurringpayment',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='recurringPayments', to='subcaptain.paymentcategory'),
        ),
    ]
