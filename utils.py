import os

from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra import ConsistencyLevel
from cassandra.query import dict_factory
from ssl import SSLContext, PROTOCOL_TLSv1, CERT_REQUIRED
from cassandra.auth import PlainTextAuthProvider

USERNAME = os.environ["CASSANDRA_USERNAME"]
PASSWORD = os.environ["CASSANDRA_PASSWORD"]
REGION = os.environ["AWS_REGION"]

ssl_context = SSLContext(PROTOCOL_TLSv1)
ssl_context.load_verify_locations("./AmazonRootCA1.pem")
ssl_context.verify_mode = CERT_REQUIRED
auth_provider = PlainTextAuthProvider(username=USERNAME, password=PASSWORD)
profile = ExecutionProfile(
    consistency_level=ConsistencyLevel.LOCAL_QUORUM, row_factory=dict_factory
)
cluster = Cluster(
    [f"cassandra.{REGION}.amazonaws.com"],
    ssl_context=ssl_context,
    auth_provider=auth_provider,
    port=9142,
    execution_profiles={EXEC_PROFILE_DEFAULT: profile},
)
