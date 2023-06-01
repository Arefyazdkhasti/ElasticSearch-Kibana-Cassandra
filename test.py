import pandas as pd

# Read the CSV file into a pandas dataframe
df = pd.read_csv('final_2.csv')

# Calculate the total number of records where the 'parent' column is not null
num_records_with_parent = df['parent'].notnull().sum()

# Print the total number of records with a non-null parent value
print("Total number of records with a non-null parent value:", num_records_with_parent)


# Calculate the total number of records where the 'childer' column is not null
num_records_with_children = df['children'].notnull().sum()

# Print the total number of records with a non-null children value
print("Total number of records with a non-null children value:", num_records_with_children)


from elasticsearch import Elasticsearch
import pandas as pd

es = Elasticsearch(
    hosts=['http://localhost:9200']
)
index_name = 'books_index'

# Get the number of children's books and their average page count
query_children = {
  "query": {
    "bool": {
      "must_not": {
        "term": {"parent": ""}
      }
    }
  }
}

books_info_children = es.search(index=index_name, body=query_children, size= 1000)
print(f"Number of matching documents: {books_info_children['hits']['total']['value']}")

query_adults = {
  "query": {
    "bool": {
      "must_not": {
        "term": {"children": ""}
      }
    }
  }
}

books_info_adults = es.search(index=index_name, body=query_adults, size = 8747)
print(f"Number of matching documents: {books_info_adults['hits']['total']['value']}")

index = 0
for source in books_info_children['hits']['hits']:
    source_dict = source['_source']
    #print(index)
    index += 1
    #print(f"{source_dict['title']}/{source_dict['date']} -> {source_dict['pages']}") 