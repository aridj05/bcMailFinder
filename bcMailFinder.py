import mechanize
import urllib
import sys
import cookielib
from bs4 import BeautifulSoup

email = sys.argv[1]

def findEmail(email):
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
	email = urllib.quote_plus(email)
	url = "https://blockchain.info/wallet/forgot-identifier?param1=" + email
	response = br.open(url)
	html = response.read()
	if 'Email Not Found' in html:
		print '[-] Email not found'
	else:
		print '[+] Email found'

findEmail(email)
