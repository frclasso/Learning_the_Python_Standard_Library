#!/usr/bin/env python3

# HTML parser module
from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag: ",tag)
        for attr in attrs:
            print('attr: ', attr)

    def handle_endtag(self, tag):
        print('End tag: ', tag)

    def handle_comment(self, data):
        print("Comment: ", data)

    def handle_data(self, data):
        print("Data: ", data)


parser = HTMLParser()
parser.feed("<html><head><title>Coder</title></head><body><h1><!--Hi-->"
            "I am a coder</h1></body></html>")
print()

# input data dynamically
# input = input("Put in HTML code.")
# parser.feed(input)
# print()

# Input data from external file
htmlFile = open("sampleHTML.html")
s = ""
for line in htmlFile:
    s += line
parser.feed(s)