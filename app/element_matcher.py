import re

from models.element_state import ElementType


class ElementFinder(object):
    def __init__(self, regexes, type):
        self.regexes = regexes
        self.type = type

    def match(self, element):
        for regex in self.regexes:
            matches = re.findall(regex,element.html.lower())
            if len(matches) >0:
                print "match is %s %s" % (matches, element.html)
                return True
        return False

class ElementMatcher(object):
    PASSWORD = ElementFinder(["[Pp][aswr \-\_\ ]{3,10}"],ElementType.PASSWORD)
    LOGIN = ElementFinder(["[Ll]og[\ ]*[Ii]n","[Ss]ign[\ ]*[Ii]n"], ElementType.LOGIN)
    LOGOUT = ElementFinder(["[Ll]og[\ ]*[Oo]ut","[Ss]ign[\ ]*[Oo]ut"], ElementType.LOGOUT)
    USERNAME = ElementFinder(["[Ee]mail", "[Uu]ser[Nname \ \-\_]"], ElementType.USERNAME)
    SUBMIT = ElementFinder(["[Ss]ubmit"], ElementType.SUBMIT)
    SEARCH = ElementFinder(["[Ss]earch"], ElementType.SEARCH)
    ADDRESS = ElementFinder(["[Aa]ddress"], ElementType.ADDRESS)
    PHONE = ElementFinder(["[Pp]hone"], ElementType.PHONE)
    ZIP = ElementFinder(["[Zz]ip"], ElementType.ZIP)
    FIRSTNAME = ElementFinder(["[Ff]irst"], ElementType.FIRSTNAME)
    LASTNAME = ElementFinder(["[Ll]ast"], ElementType.LASTNAME)
    DATE = ElementFinder(["[Dd]ate"],ElementType.DATE)
    DAY = ElementFinder(["[Dd]ate"],ElementType.DAY)
    MONTH = ElementFinder(["[Dd]ate"],ElementType.MONTH)
    YEAR = ElementFinder(["[Dd]ate"],ElementType.YEAR)

    def __init__(self):
        self.matches = [self.PASSWORD,self.LOGIN,self.LOGOUT, self.USERNAME,self.SEARCH, self.SUBMIT, self.ADDRESS,
                        self.PHONE, self.ZIP, self.FIRSTNAME, self.LASTNAME]

    def match(self, element):
        for match in self.matches:
            if match.match(element):
                return match.type
        return ElementType.UNKNOWN



