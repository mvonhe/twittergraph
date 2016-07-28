import twitter_test

api=twitter_test.api

#from twitter_test import name
#twitter_test.writeJson('mvheyl')

friends=api.GetFriends(screen_name='mvheyl')

print 'hiii there n00b'
for fr in friends[5:10]:
    name=fr.name
    fid = fr.id
    print 'fr name= '+name, 'fr id = '+str(fid)
    #friendsfriends=api.GetFriends(screen_name=name).AsDict()
    #for f in friendsfriends[:10]:
    #    print 'f= '+str(f)
    #print len(friendsfriends)
#print friends[:10]
#print len(friendsfriends)

twitter_test.writefile(friends[0].name)
