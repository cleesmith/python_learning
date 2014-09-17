from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(host='192.168.0.2', port=9200)
es.get(index="signatures", doc_type="gen_sid_msg_maps", id="1:2009580")['_source']
