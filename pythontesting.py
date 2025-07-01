import re
import os

text=['subfolder20','subfolder21']
relearning=[[int(s) if s.isdigit() else s for s in re.split(r'(\d+)', item)] for item in text]

print(f'relearning:\n{relearning}\n')

singletext='assetstorage5'
x=re.split(r'(\d+)', singletext)
print(x)
