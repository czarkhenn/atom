from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://coinmarketcap.com/currencies/eternal-token/')

print(r.html)
