from django.core.management.base import BaseCommand


class command(BaseCommand):
    help = "he love me"

    def add_arguments(self, parser):
        parser.add_arguments("--times", help="how many time s")

    def handle(self, *args, **options):
        print(args, options)
        print("ddd")
