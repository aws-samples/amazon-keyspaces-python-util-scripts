from entities import User
from utils import cluster

session = cluster.connect()


def create_user(user):
    print(f"Creating {user.username}...")
    command = f"INSERT INTO users.users (username, name, email, address, birthdate) VALUES ('{user.username}', '{user.name}', '{user.email}', '{user.address}', '{user.birthdate}') IF NOT EXISTS"
    r = session.execute(command)
    results = r.one()
    applied = results["[applied]"]
    if not applied:
        raise Exception(f"User {user.username} already exists")
    print(f"User {user.username} created successfully!")
    return user


user = User(
    username="michelle72",
    name="Thomas Davis",
    email="jake74@hotmail.com",
    address="136 Ryan Knolls, East Tiffany, AL 29438",
    birthdate="1986-07-14",
)

create_user(user)
