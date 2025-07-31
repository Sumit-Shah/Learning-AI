book = {}
book['tom'] = {
    'name' : 'tom',
    'addresh': '1 red street, YK',
    'phone': 989898988
}
book['bob'] = {
    'name' : 'bob',
    'addresh': '1 red street, YK',
    'phone': 989898988
}


import json
s = json.dumps(book)
# print(s)
with open("book.txt", "w") as f:
    f.write(s)