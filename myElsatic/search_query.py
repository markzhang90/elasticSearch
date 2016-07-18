import urllib.parse, urllib.request
import sys
import json


class MySearcher:

    http = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(MySearcher, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def search_query(self):

        search_data = dict()
        query = dict()
        matchers = dict()
        matchers['last_name'] = 'zhang3'
        matchers['age'] = '15'
        query["match"] = matchers
        search_data['query'] = query

        target_url = 'http://localhost:9200/megacorp/employee/_search'
        jdata = json.dumps(search_data).encode('UTF-8')
        print(jdata)
        # request_para = urllib.parse.urlencode(jdata).encode('UTF-8')
        url = urllib.request.Request(target_url, jdata)
        req = urllib.request.urlopen(url)
        print(req)
        print(req.status, req.read())

take = MySearcher()
take.search_query()


