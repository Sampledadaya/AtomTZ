# data/create_test_data.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'atom_chat.settings')
django.setup()

from users.models import User
from chat.models import Channel, Message


def create_test_data():
    user1 = User.objects.create_user(username='user1', password='pass123')
    user2 = User.objects.create_user(username='user2', password='pass123')

    channel = Channel.objects.create(name='General')
    channel.users.add(user1, user2)

    Message.objects.create(channel=channel, user=user1, content='Hello from user1!')
    Message.objects.create(channel=channel, user=user2, content='Hello from user2!')


if __name__ == '__main__':
    create_test_data()
