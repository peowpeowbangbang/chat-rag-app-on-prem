from elasticsearch import Elasticsearch
from langchain_elasticsearch import ElasticsearchChatMessageHistory

import os

ELASTIC_CLOUD_ID = os.getenv("ELASTIC_CLOUD_ID")
ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL")
ELASTIC_API_KEY = os.getenv("ELASTIC_API_KEY")
ELASTIC_USER = os.getenv("ELASTIC_USER")
ELASTIC_PASS = os.getenv("ELASTIC_PASS")


if ELASTICSEARCH_URL:
    elasticsearch_client = Elasticsearch(
        hosts=[ELASTICSEARCH_URL]
    )
if ELASTICSEARCH_URL and ELASTIC_USER and ELASTIC_PASS:
    verify_certs = os.getenv("VERIFY_CERTS", "False").lower() == "true"
    elasticsearch_client = Elasticsearch(
        hosts=[ELASTICSEARCH_URL], verify_certs=verify_certs, basic_auth=( ELASTIC_USER, ELASTIC_PASS)
    )
elif ELASTIC_CLOUD_ID:
    elasticsearch_client = Elasticsearch(
        cloud_id=ELASTIC_CLOUD_ID, api_key=ELASTIC_API_KEY
    )
else:
    raise ValueError(
        "Please provide either ELASTICSEARCH_URL or ELASTIC_CLOUD_ID and ELASTIC_API_KEY"
    )


def get_elasticsearch_chat_message_history(index, session_id):
    return ElasticsearchChatMessageHistory(
        es_connection=elasticsearch_client, index=index, session_id=session_id
    )
