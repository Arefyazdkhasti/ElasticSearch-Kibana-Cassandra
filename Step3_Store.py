from elasticsearch import Elasticsearch
import pandas as pd
from cassandra.cluster import Cluster
import json

es = Elasticsearch(
    hosts=['http://localhost:9200']
)
index_name = 'books_index_2'

# Get the number of children's books and their average page count
query_children = {
  "query": {
    "bool": {
      "must_not": {
        "term": {"parent": ""}
      }
    }
  },
  "size" : 1422
}

books_info_children = es.search(index=index_name, body=query_children)
print(f"Number of matching documents: {books_info_children['hits']['total']['value']}")

query_adults = {
  "query": {
    "bool": {
      "must_not": {
        "term": {"children": ""}
      }
    }
  },
  "size" :  239
}

books_info_adults = es.search(index=index_name, body=query_adults)
print(f"Number of matching documents: {books_info_adults['hits']['total']['value']}")

# Connect to the Cassandra cluster
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

# Specify a keyspace
session.execute("CREATE KEYSPACE IF NOT EXISTS elasticSearchKS WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}")

session.execute("DROP TABLE IF EXISTS elasticSearchKS.childrenBooks")
session.execute("DROP TABLE IF EXISTS elasticSearchKS.parentBooks")

# Create table for children's books
session.execute("""
    CREATE TABLE IF NOT EXISTS elasticSearchKS.childrenBooks (
        id_trove text PRIMARY KEY,
        title text,
        contributors text,
        full_text_url text,
        format text,
        pages int,
        publication_date int
    )
""")

# Create table for parent books
session.execute("""
    CREATE TABLE IF NOT EXISTS elasticSearchKS.parentBooks (
        id_trove text PRIMARY KEY,
        title text,
        contributors text,
        full_text_url text,
        format text,
        pages int,
        publication_date int
    )
""")
                
# Insert data into appropriate table based on the age group of the book
index = 0
for source in books_info_children['hits']['hits']:
    source_dict = source['_source']
    index += 1
    session.execute("""
         INSERT INTO elasticSearchKS.childrenBooks (id_trove, title, contributors, full_text_url, format, pages, publication_date)
         VALUES (%s, %s, %s, %s, %s, %s, %s) IF NOT EXISTS"""
                    , (source_dict["trove_id"], source_dict["title"], 
                       source_dict["contributors"], source_dict["fulltext_url"],
                         source_dict["format"], int(source_dict["pages"]), int(source_dict["date"])))

print(index)    

index = 0    
for source in books_info_adults['hits']['hits']:
    source_dict = source['_source']
    index += 1
    session.execute("""
         INSERT INTO elasticSearchKS.parentBooks (id_trove, title, contributors, full_text_url, format,pages, publication_date)
         VALUES (%s, %s, %s, %s, %s, %s, %s) IF NOT EXISTS"""
                    , (source_dict["trove_id"], source_dict["title"], 
                       source_dict["contributors"], source_dict["fulltext_url"],
                         source_dict["format"],  int(source_dict["pages"]), int(source_dict["date"])))

print(index)    
    
   