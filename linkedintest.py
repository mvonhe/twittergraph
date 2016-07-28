from linkedin import linkedin
#from linkedin.linkedin import NETWORK_UPDATES

#API_KEY = 'wFNJekVpDCJtRPFX812pQsJee-gt0zO4X5XmG6wcfSOSlLocxodAXNMbl0_hw3Vl'
API_KEY = '78inod5y0pnmaf'
#API_SECRET = 'daJDa6_8UcnGMw1yuq9TjoO_PMKukXMo8vEMo7Qv5J-G3SPgrAV0FqFCd0TNjQyG'
API_SECRET = 'yg2g4fMwES3R3HOn'
RETURN_URL = 'http://ligraph.mybluemix.net'

authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
print authentication.authorization_url
application = linkedin.LinkedInApplication(authentication)

#conns = application.get_connections()
application.get_connections(selectors=['headline', 'first-name', 'last-name'], params={'start':10, 'count':5})
#print conns[:10]