from django.core.management.base import BaseCommand
from django.conf import settings

import helpers

STATICFILES_VENDOR_DIR = settings.STATICFILES_VENDOR_DIR

VENDOR_STATICFILES = {
    #"saas-theme.min.css": "https://raw.githubusercontent.com/codingforentrepreneurs/SaaS-Foundations/main/src/staticfiles/theme/saas-theme.min.css",
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    #"flowbite.min.js.map": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map"
}

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Downloading vendor staticfiles")

        for name, url in VENDOR_STATICFILES.items():
            # helpers.download_file(url, name)
            output_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, output_path)
            if dl_success:
                self.stdout.write(f"Downloaded {name} from {url} to {output_path}")
            else:
                self.stderr.write(f"Failed to download {name} from {url} to {output_path}")