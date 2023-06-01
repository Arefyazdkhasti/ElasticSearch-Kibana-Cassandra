import csv
from elasticsearch import Elasticsearch

# create a connection to Elasticsearch
es = Elasticsearch(
    hosts=['http://localhost:9200']
)

# create an index for the books
index_name = 'books_index'
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

# create a mapping for the index
mapping = {
    "properties": {
        "title": {"type": "text"},
        "url": {"type": "keyword"},
        "contributors": {"type": "text"},
        "date": {
            "type": "date",
            "format": "yyyy"
        },
        "format": {"type": "keyword"},
        "full_text_url": {"type": "keyword"},
        "trove_id": {"type": "keyword"},
        "language": {"type": "keyword"},
        "rights": {"type": "keyword"},
        "pages": {"type": "integer"},
        "form": {"type": "keyword"},
        "volume": {"type": "keyword"},
        "parent": {"type": "keyword"},
        "children": {"type": "keyword"},
        "text_downloaded": {"type": "keyword"},
        "text_file": {"type": "keyword"}
    }
}

es.indices.put_mapping(index=index_name, body=mapping)

# read the data from the csv file and index it
with open('final.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        es.index(index=index_name, body=row)