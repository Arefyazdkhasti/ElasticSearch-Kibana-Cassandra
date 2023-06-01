from elasticsearch import Elasticsearch

es = Elasticsearch(
    hosts=['http://localhost:9200']
)
index_name = 'books_index_2'

# Get the number of children's books and their average page count
query = {
  "query": {
    "bool": {
      "must_not": {
        "term": {"parent": ""}
      }
    }
  },
  "aggs": {
    "avg_page_count": {"avg": {"field": "pages"}}
  }
}
result = es.search(index=index_name, body=query)

num_children_books = result["hits"]["total"]["value"]
avg_page_count = result["aggregations"]["avg_page_count"]["value"]

print(f"Number of children's books: {num_children_books}")
print(f"Average page count of children's books: {avg_page_count:.2f}")

query = {
  "size": 0,
  "aggs": {
    "publication_year": {
      "terms": {
        "field": "date",
        "format": "yyyy"
      },
      "aggs": {
        "doc_count": {
          "value_count": {
            "field": "trove_id"
          }
        }
      }
    }
  }
}
res = es.search(index='books_index', body=query)
largest_num_books_year = res['aggregations']['publication_year']['buckets'][0]['key_as_string']

print(f"The year with the largest number of books published is {largest_num_books_year}.")