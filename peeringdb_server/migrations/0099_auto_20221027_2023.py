# Generated by Django 3.2.16 on 2022-10-27 20:23

from django.db import migrations


def update_existing_instance_values(apps, schema_editor):
    """
    Model instances are iterated and setting string values will be updated with new string replacement
    API_THROTTLE_RESPONSE_SIZE_ENABLED_CIDR
    API_THROTTLE_REPEATED_REQUEST_ENABLED_CIDR
    """
    model_cls = apps.get_model("peeringdb_server", "EnvironmentSetting")

    instances = model_cls.objects.all()

    for instance in instances:
        saved_value = instance.setting
        original_keyword = "RESPONSE_SIZE"
        new_keyword = "REPEATED_REQUEST"

        if original_keyword in saved_value:
            updated_value = str(saved_value).replace(original_keyword, new_keyword)
            instance.setting = updated_value
            instance.save()


def restore_existing_instance_values(apps, schema_editor):
    """
    Model instances are iterated and setting string values will be updated with new string replacement
    API_THROTTLE_REPEATED_REQUEST_ENABLED_CIDR
    API_THROTTLE_RESPONSE_SIZE_ENABLED_CIDR
    """
    model_cls = apps.get_model("peeringdb_server", "EnvironmentSetting")

    instances = model_cls.objects.all()

    for instance in instances:
        saved_value = instance.setting
        original_keyword = "REPEATED_REQUEST"
        new_keyword = "RESPONSE_SIZE"

        if original_keyword in saved_value:
            updated_value = str(saved_value).replace(original_keyword, new_keyword)
            instance.setting = updated_value
            instance.save()


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0098_alter_environmentsetting_setting"),
    ]

    operations = [
        # run function for updating data
        migrations.RunPython(
            update_existing_instance_values, restore_existing_instance_values
        ),
    ]