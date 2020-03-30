from django.db import migrations


def remove_bad_messages(apps, schema_editor):
    """
    Removes messages that are no longer associated with a user as a result
    of a previous migration that removed ids from the user model.
    """
    Message = apps.get_model("messagebox", "Message")
    Message.objects.filter(recipient_id__gt=154).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("messagebox", "0003_auto_20141220_1823"),
        ("fuauth", "0024_auto_20200329_1421"),
    ]

    operations = [migrations.RunPython(remove_bad_messages)]
