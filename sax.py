import xml.sax

class StudentHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        self.current = name
        if name == "person":
            print(f"--person {attrs[id]}--")

    def 