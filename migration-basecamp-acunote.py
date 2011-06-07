#!/usr/bin/env python
import sys
import xml.etree.ElementTree as ElementTree
from basecampclient.basecamp import Basecamp
import params

if len(sys.argv) != 2:
    print "usage: migration-basecamp-acunote [listid]"
    sys.exit(1)

listid = int(sys.argv[1])
xml = Basecamp(params.url, params.apikey).todo_list(listid)
items = ElementTree.fromstring(xml).findall('todo-items/todo-item')

# Basecamp fields
# position, content, completed, due-at, id, created-on, creator-name, creator-id, created-at, updated-at, commented-at, comments-count

# Acunote fields
print "Level,Number,Description,Tags,Owner,Status,Priority,Estimate,Remaining,Wiki,Watchers,Related,Duplicate,Version 1"

for item in items:
    if item.find('completed').text == "true":
        status = "Completed"
    else:
        status = "Not Started"    
        
    creatorName = params.creatorNames[item.find('creator-id').text]
    
    print ',"%s","%s",,"%s","%s",,,,,,,,' % (
        item.find('position').text,
        item.find('content').text,
        creatorName,
        status
    )
