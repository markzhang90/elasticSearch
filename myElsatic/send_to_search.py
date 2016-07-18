import urllib.parse, urllib.request
import sys
import json


class MySender:

    def send_data(self):

        data = dict()
        data['first_name'] = 'mark'
        data['last_name'] = 'zhang'
        data['age'] = '11'
        data['about'] = 'I love to go rock climbing'
        data['interests'] = '[ "sports", "music" ]'
        target_url = 'http://localhost:9200/megacorp/employee/3'
        jdata = json.dumps(data)
        print(jdata)
        # request_para = urllib.parse.urlencode(jdata).encode('UTF-8')
        url = urllib.request.Request(target_url, jdata.encode('UTF-8'))
        urllib.request.get_method = lambda: 'PUT'
        req = urllib.request.urlopen(url)
        print(req)
        print(req.status, req.reason)

take = MySender()
take.send_data()


