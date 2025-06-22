#!/usr/bin/env python3

from random import choice as rc
from faker import Faker

from app import app
from models import db, Message
from datetime import datetime

fake = Faker()

usernames = [fake.first_name() for i in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_messages():
    # Drop and recreate tables
    db.drop_all()
    db.create_all()

    messages = []

    for i in range(20):
        message = Message(
            body=fake.sentence(),
            username=rc(usernames),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        messages.append(message)

    db.session.add_all(messages)
    db.session.commit()

    print(f"✅ Seeded {len(messages)} messages.")

if __name__ == '__main__':
    with app.app_context():
        make_messages()
