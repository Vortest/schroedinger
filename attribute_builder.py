from HTMLParser import HTMLParser
import re
from attribute_counter import AttributeCounter


class AttributeBuilder(HTMLParser):
    SKIP_ATTRIBUTES = ['style','maxlength','data-ved']

    def __init__(self,element):
        self.reset()
        self.element = element
        self.total_attributes = []
        self.unique_attributes = []
        self.duplicate_attributes = []
        self.is_first = True
        self.get_text_as_attribute()
        self.feed(element.html)


    def handle_starttag(self, tag, attrs):
        if self.is_first:
            self.is_first = False
            for attr in attrs:
                if attr[0] not in AttributeBuilder.SKIP_ATTRIBUTES:
                    attributes = attr[1].split(' ')
                    for attribute in attributes:
                        self.total_attributes.append((attr[0],attribute))
                
    def get_attributes(self):
        return self.total_attributes

    def get_text_as_attribute(self):
        text = self.element.text
        if text is not u'':
            self.total_attributes.append(("text",text))

    def get_unique_attributes(self):
        html = self.element.driver.page_source
        for attribute in self.get_attributes():
            if self.is_attribute_unique(attribute,html):
                self.unique_attributes.append(attribute)
            else:
                self.duplicate_attributes.append(attribute)
        return self.unique_attributes

    def is_attribute_unique(self, att, html):
        try:
            if att[0] == "text":
                matches = re.findall("\>{}\<\/".format(att[1]),html)
                return len(matches) == 1
            else:
                counter = AttributeCounter(html,att)
                return counter.count == 1
        except:
            return False
