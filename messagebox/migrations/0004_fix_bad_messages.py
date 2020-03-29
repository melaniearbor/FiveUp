from django.db import migrations


def remove_bad_messages(apps, schema_editor):
    Message = apps.get_model('messagebox', 'Message')
    Message.objects.filter(recipient_id__gt=154).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('messagebox', '0003_auto_20141220_1823'),
        ('fuauth', '0024_auto_20200329_1421'),
    ]

    operations = [
        migrations.RunPython(remove_bad_messages),
    ]
