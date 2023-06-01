from elasticsearch import Elasticsearch

# Create Elasticsearch client instance
es = Elasticsearch(
    hosts=['http://localhost:9200']
)
# Specify index to be deleted
index_name = 'books_indx'

# Delete the index
response = es.indices.delete(index=index_name)
print(response)