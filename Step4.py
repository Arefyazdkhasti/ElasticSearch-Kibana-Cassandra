from cassandra.cluster import Cluster

# Connect to the Cassandra cluster
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

# Retrieve all data from childrenBooks table
rows_children = session.execute('SELECT * FROM elasticSearchKS.childrenBooks')
data_children = [(row.title, row.pages) for row in rows_children]

# Retrieve all data from parentBooks table
rows_parent = session.execute('SELECT * FROM elasticSearchKS.parentBooks')
data_parent = [(row.title, row.pages) for row in rows_parent]

# Find books that exist in both tables
common_books = set([book[0] for book in data_children]).intersection(set([book[0] for book in data_parent]))
books_to_avg = [book for book in data_children + data_parent if book[0] in common_books]

# Calculate the average number of pages
avg_pages = sum([int(book[1]) for book in books_to_avg]) / len(books_to_avg)

print(f"The average number of pages for books in both tables is {avg_pages}.")


# Get all children's books published before 2000
children_query = "SELECT * FROM elasticSearchKS.childrenBooks WHERE publication_date < 2000 ALLOW FILTERING"
children_results = session.execute(children_query)

print("Children's books published before 2000:---------------------------")
for index, result in enumerate(children_results):
    print(f"{index} -> {result.publication_date} : {result.title}")

# Get all parent books published before 2000
parent_query = "SELECT * FROM elasticSearchKS.parentBooks WHERE publication_date < 2000 ALLOW FILTERING"
parent_results = session.execute(parent_query)

print("Parent books published before 2000:-------------------------------")
for index, result in enumerate(parent_results):
    print(f"{index} -> {result.publication_date} : {result.title}")
