import gc
from collections import defaultdict
import random
import string

sbuffer = None


def sortme(default_in=string.ascii_lowercase):
    global sbuffer

    if sbuffer == None:
        return ""

    d = defaultdict(lambda: 0)
    for i in range(len(sbuffer)):
        d[sbuffer[i]] += 1

    sbuffer = None
    gc.collect()

    format_buffer = ""
    for ch in default_in:
        format_buffer += "{{:{}<{}}}".format(ch, d[ch])

    values = [''] * len(default_in)
    return format_buffer.format(*values)


SIZE = 100
sbuffer = ''.join(random.choice(string.ascii_lowercase) for _ in range(SIZE))
print("In:", sbuffer)

result = sortme()
print("Out:", result)
