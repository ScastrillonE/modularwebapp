import json
from os import listdir, path

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from modularwebapplication.base.models import Plugin

class Command(BaseCommand):

    def handle(self, *args, **options):
        # ================================================================== #
        self.stdout.write(
            self.style.MIGRATE_HEADING(_('*** Generating base migrations...'))
        )
        call_command('makemigrations', 'base', interactive=False)

        # ================================================================== #
        self.stdout.write(
            self.style.MIGRATE_HEADING(_('*** Migrating the base database...'))
        )
        call_command('migrate', interactive=False)
        
        self.stdout.write(
            self.style.MIGRATE_HEADING(_('Initialized apps'))
        )
        
        if not Plugin.objects.all().exists():
            open("installed_apps.py","w").close()
            content_apps = f"{settings.APPS_DIR}"
            FILE_APP_DATA = "__manifest__.py"
            installed_apps = open('installed_apps.py', 'a+')
            
            for folder in listdir(content_apps):
                file = content_apps + "/" + folder + "/" + FILE_APP_DATA
                if path.isfile(file):
                    with open(file) as manifest:
                        data = json.load(manifest)
                        plugin = Plugin(
                            name = data["name"],
                            author = data["author"],
                            description = data["description"],
                            category = data["category"],
                            installable = data["installable"],
                            installed = data["installed"],
                            color = data["color"],
                            icon = data["icon"],
                            version = data["version"],
                        )
                        
                        plugin.save()
                        if data['installed'] == '1' and data["installable"] == '1':
                            installed_apps.write(f"modularwebapplication.{data['name'].lower()}\n")
            installed_apps.close()
            self.stdout.write(
                self.style.MIGRATE_HEADING(_('Principal apps installed'))
            )