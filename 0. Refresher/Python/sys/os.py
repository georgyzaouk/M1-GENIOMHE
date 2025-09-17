

import os

str1 = os.popen('ls').read()
lst1 = str1.strip()

print(lst1)
