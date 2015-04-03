# installs required:
# pip install lxml
# pip install requests


from lxml import html
import requests

page = requests.get("www.nytimes.com")
tree = html.fromstring(page.text)

print tree
