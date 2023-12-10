from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = 'admin'

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_superuser(username)
            user.set_password('admin')
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" successfully created'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser "{username}" already exists'))

