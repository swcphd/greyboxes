import parser
from pprint import pprint

r = open('hello.py', 'r')

# this makes a parse tree
st = parser.suite(r.read())
st_list = parser.st2list(st)
pprint(st)

code = st.compile()
# eval(code)
