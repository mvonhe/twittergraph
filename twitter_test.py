# -*- coding: utf-8 -*-

import twitter, json, codecs, random, os, re, glob

api = twitter.Api(consumer_key="UCQpUai3HNPvVQakSjq17GuKg",
                  consumer_secret="dgf58jmBmjUtTQzE2YQq6NskgefNvwaa2xBRDVhj9W584jODnj",
                  access_token_key="2805260366-UfU753RVPQc16AHS9tHO2mrC6FMFkmc1nsUry7g",
                  access_token_secret="6FOcFNT1wacIYPmVBIjMefCrAP4nyl3pmylxhpRKzhfMx",
                  sleep_on_rate_limit=True)

## text input
thisname = "Archer_Sterling"

def getFriends(name):
    return api.GetFriends(screen_name=name)

def writeJson(name):
    #get correct filename
    oldfile = glob.glob('static/the*.json')[0]
    try:
        number = int(re.search('\d+', oldfile).group(0))
    except AttributeError:
        number=0
    number += 1
    filename = 'static/the' + str(number%10) + '.json'
    infile = codecs.open(filename, 'w', 'utf-8')

    friends = getFriends(name)
    cnt=0
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

    infile.close()
    os.remove(oldfile)
    return filename

#writeJson('Archer_Sterling')

def writefile(name):
    oldfile = glob.glob('static/example*.txt')[0]
    print oldfile
    number = int(re.search('\d+', oldfile).group(0))
    print number
    number += 1
    filename = 'static/example' + str(number) + '.txt'
    infile = codecs.open(filename, 'w', 'utf-8')
    infile.write('test' + str(number) + ' ' + name)
    os.remove(oldfile)
    infile.close()


