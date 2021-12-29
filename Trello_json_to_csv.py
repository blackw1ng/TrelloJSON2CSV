#!/usr/bin/python3

import sys, json;

# read json from STDIN
data = json.load(sys.stdin)

# make the lists of ids accessible as dicts for de-referencing
users = {item['id']:item for item in data['members']}
lists = {item['id']:item for item in data['lists']}
cards = {item['id']:item for item in data["cards"]}
actions = {item['id']:item for item in data['actions']}
comments = {item['id']:item for item in data['actions'] if item["type"] == "commentCard"}

# make sure we have the field separators right...
sep = ","
sep2 = ";"
newline_replacement = "; "

def sanitize(record):
    
    if sep == ",":
        record = record.replace(",","")
    
    return(record.replace("\n",newline_replacement))


print(f"ID{sep}TrelloURL{sep}List{sep}Name{sep}Description{sep}Labels{sep}LastModified{sep}Assignee{sep}DueDate{sep}Completed{sep}Comments")

for id,card in cards.items():
    
    line = f'{card["id"]}{sep}{card["url"]}{sep}'
    line += lists[card["idList"]]["name"]+sep
    line += sanitize(card["name"])+sep
    line += sanitize(card["desc"])+sep
    
    num=-1
    for num,label in enumerate(card["labels"]):
        line += label["name"] + sep2
    if num < 0:
        line += sep
    else:
        line = line[:-1]+sep
    
    line += card["dateLastActivity"]+sep
    
    num=-1
    for num,userId in enumerate(card["idMembers"]):
        line += users[userId]["fullName"] +sep2
    if num < 0:
        line += sep
    else:
        line = line[:-1]+sep
        
    
    line += f'{card["due"]}{sep}'
    if card["dueComplete"]:
        line += "True"+sep
    else:
        line += "False"+sep
    
    relevant_comments = 0
    for commentId,comment in comments.items():
         if comment["data"]["card"]["id"] == id:
                relevant_comments += 1
                
                line += "Comment by "+users[comment["idMemberCreator"]]["fullName"] + " on "+ comment["date"] + ": "
                line += sanitize(comment["data"]["text"])+sep2
                
    if relevant_comments >0:
        line = line[:-1]
    
    print(line)