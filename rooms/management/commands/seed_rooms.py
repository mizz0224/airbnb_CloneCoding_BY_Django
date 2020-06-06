from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from rooms.models import room_models


class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many users do you want me to creat?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(room_models.Room, number, {})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number}users created!"))
