import twitter_test

api=twitter_test.api

#from twitter_test import name
#twitter_test.writeJson('mvheyl')

#friends=api.GetFriends(screen_name='mvheyl')

result=api.GetUsersSearch('clanx')

print result[0].name
