# -*- coding: utf-8 -*-

import twitter, json, codecs, random

api = twitter.Api(consumer_key="UCQpUai3HNPvVQakSjq17GuKg",
                  consumer_secret="dgf58jmBmjUtTQzE2YQq6NskgefNvwaa2xBRDVhj9W584jODnj",
                  access_token_key="2805260366-UfU753RVPQc16AHS9tHO2mrC6FMFkmc1nsUry7g",
                  access_token_secret="6FOcFNT1wacIYPmVBIjMefCrAP4nyl3pmylxhpRKzhfMx")


## text input
thisname = "Archer_Sterling"

def getFriends(name):
    return api.GetFriends(screen_name=name)

def writeJson(name):
    friends=getFriends(name)
    infile = codecs.open('static/the.json', 'w', 'utf-8')
    infile.write('{\n  "nodes": [\n')
    ### don't forget the root node! :)
    infile.write('  {"id": "' + name + '", "group": ' + str(random.randint(1, 3)) + '},\n')

    ### write friend nodes
    for fr in friends[:-1]:
        infile.write('    {"id": "' + fr.name + '", "group": ' + str(random.randint(1, 3)) + '},\n')
    infile.write('    {"id": "' + friends[len(friends)-1].name + '", "group": ' + str(random.randint(1, 3)) +
                  '}\n  ],\n"links": [\n')

    ### write links [root-friend]
    for fr in friends[:-1]:
        infile.write('    {"source": "' + name + '", "target": "' + fr.name + '", "value": ' +
                     str(random.randint(1, 5)) + '},\n')
    infile.write('    {"source": "' + name + '", "target": "' + friends[len(friends)-1].name + '", "value": ' +
                 str(random.randint(1, 5)) + '}\n  ]\n}')
    for fr in friends[:-1]:
       # friendsfriends=api.GetFriends(screen_name=)
        a=fr
    infile.close()


#writeJson('Archer_Sterling')
