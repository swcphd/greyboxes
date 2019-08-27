import ast
from pprint import pprint

# read the python file as text
r = open('hello.py', 'r')
source = r.read()

# make an AST
node = ast.parse(source, mode='exec')
pprint(ast.dump(node))

# make a code object
code_object = compile(node, '<string>', mode='exec')
# run the code
exec(code_object)
