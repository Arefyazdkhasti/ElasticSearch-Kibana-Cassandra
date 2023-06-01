from cassandra.cluster import Cluster

# Connect to the Cassandra cluster
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

# Define a SELECT query to retrieve data from your Cassandra table
query = "SELECT * FROM elasticSearchKS.childrenBooks"

# Execute the query and retrieve the query results
rows = session.execute(query)

# Loop over the rows in the query results and print each row
index = 0
for row in rows:
    index += 1
    # print(row)
print(f"Number of stored children book=> {index}")


# Define a SELECT query to retrieve data from your Cassandra table
query = "SELECT * FROM elasticSearchKS.parentBooks"

# Execute the query and retrieve the query results
rows = session.execute(query)

# Loop over the rows in the query results and print each row
index = 0
for row in rows:
    index += 1
    # print(row)
print(f"Number of stored parent book=> {index}")

