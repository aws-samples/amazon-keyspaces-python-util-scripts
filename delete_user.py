from entities import User
from utils import cluster

session = cluster.connect()


def delete_user(username):
    print(f"Deleting {username}...")
    command = f"DELETE FROM users.users WHERE username = '{username}'"
    r = session.execute(command)
    results = r.one()
    print(f"User {username} deleted.")


delete_user("michelle72")
