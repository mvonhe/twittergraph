import twitter_test

api=twitter_test.api

#from twitter_test import name
#twitter_test.writeJson('mvheyl')

friends=api.GetFriends(screen_name='mvheyl')

for fr in friends[10]:
    print len(api.GetFriends())
print friends[:10]
#print len(friendsfriends)