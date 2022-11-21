import re

def to_camel_case(text):
    res = re.split(r'[-_]', text)
    for i in range(1, len(res)):
        res[i] = res[i].title()
    return ''.join(res)

### we do not need the first one to be title()
