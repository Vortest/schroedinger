import re

def get_domain_from_url(url):
    domain = re.findall("\.(\w*)\.",str(url))
    if len(domain) == 0:
        domain = re.findall("(\w*)\.",str(url))
    if len(domain) > 0:
        return domain[0]