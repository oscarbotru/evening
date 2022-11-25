from django.core.management import BaseCommand

from mainapp.models import Kitchen


class Command(BaseCommand):

    def handle(self, *args, **options):
        Kitchen.objects.all().delete()

        kitchens = [
            {'title': 'Украинская', 'description': 'клецки'},
            {'title': 'Казахская', 'description': 'Козы'},
            {'title': 'Немецкая', 'description': 'Пиво'},
            {'title': 'Русская', 'description': 'пельмени'},
            {'title': 'Турецкая', 'description': 'пахлава'},
            {'title': 'Грузинская', 'description': 'хинкали'}
        ]

        kitchen_list = []

        for kitchen in kitchens:

            kitchen_list.append(Kitchen(**kitchen))

        Kitchen.objects.bulk_create(kitchen_list)
