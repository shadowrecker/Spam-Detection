# import random
# from django.core.management.base import BaseCommand
# from django.contrib.auth import get_user_model
# from api.models import Contact, SpamNumber
# from faker import Faker

# User = get_user_model()

# class Command(BaseCommand):
#     help = 'Populate the database with dummy data'

#     def handle(self, *args, **kwargs):
#         fake = Faker()

#         # Create users
#         for _ in range(10):
#             username = fake.user_name()
#             phone_number = fake.phone_number()
#             email = fake.email()
#             password = 'password123'
#             user = User.objects.create_user(username=username, phone_number=phone_number, email=email, password=password)
#             self.stdout.write(self.style.SUCCESS(f'Created user {username}'))

#             # Create contacts for each user
#             for _ in range(10):
#                 contact_name = fake.name()
#                 contact_phone_number = fake.phone_number()
#                 Contact.objects.create(owner=user, name=contact_name, phone_number=contact_phone_number)
#                 self.stdout.write(self.style.SUCCESS(f'  Created contact {contact_name} for user {username}'))

#         # Create spam numbers
#         for _ in range(10):
#             phone_number = fake.phone_number()
#             SpamNumber.objects.create(phone_number=phone_number, reports=random.randint(1, 100))
#             self.stdout.write(self.style.SUCCESS(f'Created spam number {phone_number}'))

#         self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data'))

import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Contact, SpamNumber
from faker import Faker

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):
            username = fake.user_name()
            phone_number = fake.phone_number()
            email = fake.email()
            password = 'password123'
            user = User.objects.create_user(username=username, phone_number=phone_number, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Created user {username}'))

            for _ in range(10):
                contact_name = fake.name()
                contact_phone_number = fake.phone_number()
                Contact.objects.create(owner=user, name=contact_name, phone_number=contact_phone_number)
                self.stdout.write(self.style.SUCCESS(f'  Created contact {contact_name} for user {username}'))

        for _ in range(10):
            phone_number = fake.phone_number()
            SpamNumber.objects.create(phone_number=phone_number, reports=random.randint(1, 100))
            self.stdout.write(self.style.SUCCESS(f'Created spam number {phone_number}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with dummy data'))
