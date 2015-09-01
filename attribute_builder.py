from HTMLParser import HTMLParser

class AttributeBuilder(HTMLParser):
    def __init__(self,element):
        self.reset()
        self.element = element
        self.total_attributes = []
        self.is_first = True
        self.get_text_as_attribute()
        self.feed(element.html)

    def handle_starttag(self, tag, attrs):
        if self.is_first:
            self.is_first = False
            for attr in attrs:
                if attr[0] != 'style':
                    attributes = attr[1].split(' ')
                    for attribute in attributes:
                        self.total_attributes.append((attr[0],attribute))
                
    def get_attributes(self):
        return self.total_attributes

    def get_text_as_attribute(self):
        text = self.element.text
        if text is not u'':
            self.total_attributes.append(("text",text))

