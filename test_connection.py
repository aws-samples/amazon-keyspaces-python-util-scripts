from entities import User
from utils import cluster

session = cluster.connect()
r = session.execute("SELECT * FROM users.users LIMIT 5")
print(
    f"Connected to Keyspaces table. There are {len(r.current_rows)} rows in the results."
)
for row in r.current_rows:
    print(User(**row))
