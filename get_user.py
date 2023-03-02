from entities import User
from utils import cluster

session = cluster.connect()


def get_user(username):
    print(f"Retrieving {username}...")
    command = f"SELECT * FROM users.users WHERE username = '{username}'"
    r = session.execute(command)
    results = r.one()
    if not results:
        raise Exception(f"User {username} does not exist")
    user = User(**results)
    print(user)
    return user


user = get_user("michelle72")
