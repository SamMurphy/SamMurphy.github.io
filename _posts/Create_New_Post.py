import io
import time

title = input("Enter post title: ")
categories = input("Enter categories (seperate with comma): ")
tags = input("Enter tags (seperate with comma): ")
teaser = input("Enter teaser image name: ")

title = title.title()
categories_array = [x.strip() for x in categories.split(',')]
tags_array = [x.strip() for x in tags.split(',')]

yamlFrontMatter = "---\ntitle: \"" + title + "\"\nlayout: single\nauthor_profile: true\n"
yamlFrontMatter += "read_time: true\ncomments: true\nshare: true\nrelated: true\n"
yamlFrontMatter += "categories:\n"

for cat in categories_array:
    yamlFrontMatter += "  - " + cat + "\n"

yamlFrontMatter += "tags:\n"

for tag in tags_array:
    yamlFrontMatter += "  - " + tag + "\n"

yamlFrontMatter += "header:\n  teaser: " + teaser
yamlFrontMatter += "\n---\n\n"

fileName = time.strftime("%Y") + "-" + time.strftime("%m") + "-" + time.strftime("%d") + "-"
postTitle_array = [x.strip() for x in title.split(' ')]
for word in postTitle_array:
    fileName += word

with io.FileIO(fileName + ".md", "w") as file:
    file.write(bytes(yamlFrontMatter, 'UTF-8'))

print("Post Created: " + fileName)
