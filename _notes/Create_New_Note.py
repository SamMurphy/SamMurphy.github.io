import io
import time
import os

title = input("Enter post title: ")
module = input("Enter Module Code: ")

title = title.title()

yamlFrontMatter = "---\ntitle: \"" + title + "\"\nlayout: single\nauthor_profile: true\n"
yamlFrontMatter += "read_time: true\ncomments: true\nshare: true\nrelated: true\n"
yamlFrontMatter += "categories:\n  - " + module + "\n"
yamlFrontMatter += "tags:\n  - " + module + "\n"
yamlFrontMatter += "---\n\n"

fileName = time.strftime("%Y") + "-" + time.strftime("%m") + "-" + time.strftime("%d") + "-"
postTitle_array = [x.strip() for x in title.split(' ')]
for word in postTitle_array:
    fileName += word

with io.FileIO(fileName + ".md", "w") as file:
    file.write(bytes(yamlFrontMatter, 'UTF-8'))

print("Post Created: " + fileName)

os.system("typora " + fileName + ".md &")


