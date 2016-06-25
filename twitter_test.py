# -*- coding: utf-8 -*-

import twitter, json, codecs, random

api = twitter.Api(consumer_key="UCQpUai3HNPvVQakSjq17GuKg",
                  consumer_secret="dgf58jmBmjUtTQzE2YQq6NskgefNvwaa2xBRDVhj9W584jODnj",
                  access_token_key="2805260366-UfU753RVPQc16AHS9tHO2mrC6FMFkmc1nsUry7g",
                  access_token_secret="6FOcFNT1wacIYPmVBIjMefCrAP4nyl3pmylxhpRKzhfMx")

## text input
name = "Archer_Sterling"

friends = api.GetFriends(screen_name=name)

def writeJson():
    cnt=0
    infile = codecs.open('the.json', 'w', 'utf-8')
    infile.write('{\n  "nodes": [\n')
    for fr in friends[:-1]:
        infile.write('    {"id": "' + fr.name + '", "group": '+ str(cnt%5) +'},\n')
        cnt+=1
    infile.write('    {"id": "' + friends[len(friends)-1].name + '", "group": 1}\n  ],\n"links": [\n')
    cnt = 0
    for fr in friends[:-1]:
        infile.write('    {"source": "' + name + '", "target": "' + fr.name + '", "value": '+str(int(random.randrange(5)))+'},\n')
        cnt+=1
    infile.write('    {"source": "' + name + '", "target": "' + friends[len(friends)-1].name + '", "value": '+str(int(random.randrange(5)))+'\n  ]\n}')
    infile.close()

## testing
print len(friends)

for f in friends[:10]:
    print f.name

writeJson()
