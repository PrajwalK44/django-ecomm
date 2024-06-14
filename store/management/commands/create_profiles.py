from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import Profile

class Command(BaseCommand):
    help = 'Create profiles for users who do not have one'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            if not hasattr(user, 'profile'):
                Profile.objects.create(user=user)
        self.stdout.write(self.style.SUCCESS('Successfully created missing profiles'))