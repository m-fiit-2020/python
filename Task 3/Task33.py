s = """
Hello world
abcxyz
abcdef
sdfnoasd
asdasdyz
this is test
"""
for line in s.splitlines():
    if line.startswith('ab') or line.endswith('yz') or 'no' in line:
        print(line)
