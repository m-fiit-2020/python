s = """
Hello world
abcxyz
abcdef
this is test
"""
for line in s.splitlines():
    if line.startswith('abc'):
        print(line)
