from __future__ import unicode_literals

from django.core.management.base import BaseCommand

from django.conf import settings

from axes.models import Settings


class Command(BaseCommand):
    args = ''
    help = ('Reset axes settings')

    def handle(self, *args, **kwargs):  # pylint: disable=unused-argument
        # Delete all settings
        stgs = Settings.objects.all()
        stgs.delete()

        # Create a settings row with values from the settings
        Settings.objects.create(
            failure_limit=settings.AXES_FAILURE_LIMIT
        )
