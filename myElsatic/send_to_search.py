import urllib.parse, urllib.request
import sys
import json


class MySender:

    http = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(MySender, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        pass

    def send_data(self):

        data = dict()
        data['first_name'] = 'mark'
        data['last_name'] = 'zhang3'
        data['age'] = '18'
        data['about'] = 'I love to go rock climbing'
        data['interests'] = '[ "sports", "music" ]'
        target_url = 'http://localhost:9200/megacorp/employee/7'
        jdata = json.dumps(data).encode('UTF-8')
        print(jdata)
        # request_para = urllib.parse.urlencode(jdata).encode('UTF-8')
        url = urllib.request.Request(target_url, jdata)
        urllib.request.get_method = lambda: 'PUT'
        req = urllib.request.urlopen(url)
        print(req)
        print(req.status, req.read())

take = MySender()
take.send_data()


