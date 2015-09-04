from HTMLParser import HTMLParser


class AttributeCounter(HTMLParser):
    def __init__(self, html, attribute):
        self.reset()
        self.html = html
        self.attribute = attribute
        self.type = self.attribute[0]
        self.value = self.attribute[1]
        self.count = 0
        self.feed(html)


    def handle_starttag(self, tag, attrs):
        if self.type != "text":
            for attr in attrs:
                if attr[0] == self.type and self.value in attr[1]:
                    self.count += 1



