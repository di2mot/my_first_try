from xml.etree.ElementTree import XMLParser

class MaxDepth:  # The target object of the parser
    maxDepth = 0
    depth = 0
    colors = {'red': 0, 'green': 0, 'blue': 0}

    def start(self, tag, attrib):  # Called for each opening tag.
        # print('color:', attrib['color'])
        self.depth += 1
        # print('def start_self.depth: ', self.depth)
        self.colors[attrib['color']] += self.depth
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth
            # print('def start_self.maxDepth: ', self.maxDepth)

    def end(self, tag):  # Called for each closing tag.
        self.depth -= 1
        # print('def end_self.depth: ', self.depth)

    def data(self, data):
        pass  # We do not need to do anything with data.

    def close(self):  # Called when all data has been parsed.
        return self.colors


target = MaxDepth()
parser = XMLParser(target=target)

parser.feed(input())
fin = parser.close()
print(fin['red'], fin['green'], fin['blue'])
