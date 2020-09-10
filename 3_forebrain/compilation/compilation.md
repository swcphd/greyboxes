Goal: What happens when you push "Enter" on a python script?

hint: here is an important file [https://hg.python.org/cpython/file/2.7/Modules/main.c](https://hg.python.org/cpython/file/2.7/Modules/main.c)

[python dictionary in C](https://github.com/python/cpython/blob/master/Objects/dictobject.c)

[compiler intro blogpost](https://cs.lmu.edu/~ray/notes/introcompilers/)

[another compiler intro blogpost](https://nicoleorchard.com/blog/compilers)

## Interpretation vs. Compilation

[https://www.cs.rpi.edu/academics/courses/fall00/ai/scheme/reference/schintro-v14/schintro_112.html](https://www.cs.rpi.edu/academics/courses/fall00/ai/scheme/reference/schintro-v14/schintro_112.html)

from wiki:

"Prior to execution, a program must first be written. This is generally done in source code, which is then compiled at compile time (and statically linked at link time) to an executable. This executable is then invoked, most often by an operating system, which loads the program into memory (load time), possibly performs dynamic linking, and then begins execution by moving control to the entry point of the program; all these steps depend on the Application Binary Interface of the operating system. At this point execution begins and the program enters run time. The program then runs until it ends, either normal termination or a crash."

to start with that, here's a very coarse map of how these things work

- what is C code
- what is the goal of compilation
    - get program into machine language
- how does C compile?
- what are assembly, object, and executable files?
    - to look inside .asm: [http://patshaughnessy.net/2016/11/26/learning-to-read-x86-assembly-language](http://patshaughnessy.net/2016/11/26/learning-to-read-x86-assembly-language)

python is text that is compiled into bytecode then evaluated by a C program

- what is the virtual machine? (what is a "machine" mean?)
- what does bytecode look like?
    - how do compile python? [http://effbot.org/zone/python-compile.htm](http://effbot.org/zone/python-compile.htm)

initalize CPython, initalize Python, run a bunch of C code to set up namespaces, frames, threads, CST, AST, code objects, frame objects, boil down the code into "opcodes" and call C functions based on those "opcodes", pop and set data from the operand stack, return values from C functions, clean up everything, and finalize.

> the parser/compiler stage of PyRun_SimpleStringFlags goes largely like this: tokenize and create a Concrete Syntax Tree (CST) from the code, transorm the CST into an Abstract Syntax Tree (AST) and finally compile the AST into a code object using ./Python/ast.c: PyAST_FromNode. For now, think of the code object as a binary string of machine code that Python VM’s ‘machinary’ can operate on – so now we’re ready to do interpretation (again, evaluation in Python’s parlance).

# Goals

- play with the `dis` module
- understand `compile`, `exec`, and `eval`
- understand the idea of ASTs
- play with the `ast` module

use the "dis" library to disassemble python code!

use the `compile()` function to get ASTs, use the `exec()` and `eval()` functions to walk through how python is interpreted by using python itself.

[https://docs.python.org/3/library/dis.html](https://docs.python.org/3/library/dis.html)

[https://docs.python.org/3/library/functions.html#compile](https://docs.python.org/3/library/functions.html#compile)

tutorial on doing this process:

[https://eli.thegreenplace.net/2009/11/28/python-internals-working-with-python-asts/](https://eli.thegreenplace.net/2009/11/28/python-internals-working-with-python-asts/)

A list of python "opcodes" (C programs/functions) with examples:

[http://unpyc.sourceforge.net/Opcodes.html](http://unpyc.sourceforge.net/Opcodes.html)

stepping through a python function to the CPython internals:

[https://medium.com/@skabbass1/how-to-step-through-the-cpython-interpreter-2337da8a47ba](https://medium.com/@skabbass1/how-to-step-through-the-cpython-interpreter-2337da8a47ba)

The point here is that a program is itself data. The program is a piece of data read evaluated by another program. This is "text all the way down" until we get to some sort of machine code that is "read" by the hardware itself in the form of bits.

What can we do in C/C++ and Python to show the differences between compilation and interpretation.

Show that Python is implemented in C and what this means.

Show a basic interpreter (maybe the python interpreter for Lisp?)

In Lisp/Scheme, the program explicitly represents the environments/frames of the program. In Python this is more subtle.

Use the white board to show how parsing, lexing works at a high level.

SO: [https://stackoverflow.com/questions/2842809/lexers-vs-parsers](https://stackoverflow.com/questions/2842809/lexers-vs-parsers)

what's a toy example here?

Explanation of a stripped-down python Lisp interpreter:

[http://www.michaelnielsen.org/ddi/lisp-as-the-maxwells-equations-of-software/](http://www.michaelnielsen.org/ddi/lisp-as-the-maxwells-equations-of-software/)

Original Python Lisp interpreter

[https://norvig.com/lispy.html](https://norvig.com/lispy.html)

[http://norvig.com/lispy2.html](http://norvig.com/lispy2.html)

A closure is a little program that intends to hold the state of the function when it was defined, such that each evaluation is based on that define-time state.

Shortest Intro Ever:

[https://www.cs.rpi.edu/academics/courses/fall00/ai/scheme/reference/schintro-v14/schintro_112.html](https://www.cs.rpi.edu/academics/courses/fall00/ai/scheme/reference/schintro-v14/schintro_112.html)

Python Dictionary implementation in C:

[https://github.com/python/cpython/blob/master/Objects/dictobject.c](https://github.com/python/cpython/blob/master/Objects/dictobject.c)

Cython is a python interpreter that helps you **compile** Python to more efficient C

[http://docs.cython.org/en/latest/src/quickstart/cythonize.html](http://docs.cython.org/en/latest/src/quickstart/cythonize.html)

## Inside the Python VM

This is the best writeup i've seen for walking through the Python VM. You need a basic working knowledge of reading C code, but not much, and this could be a good way to learn.

[https://leanpub.com/insidethepythonvirtualmachine/read#leanpub-auto-the-view-from-30000ft](https://leanpub.com/insidethepythonvirtualmachine/read#leanpub-auto-the-view-from-30000ft)

you can even add new opcodes into python at runtime...

[https://blog.hakril.net/articles/2-understanding-python-execution-tracer.html](https://blog.hakril.net/articles/2-understanding-python-execution-tracer.html)

Big long set of blogposts on Python Innards

[https://tech.blog.aknin.name/category/my-projects/pythons-innards/page/1/](https://tech.blog.aknin.name/category/my-projects/pythons-innards/page/1/)

> ...let’s start with a bird’s eye overview of what happens when you do this: $ python -c 'print("Hello, world!")'. Python’s binary is executed, the standard C library initialization
which pretty much any process does happens and then the main function
starts executing (see its source, ./Modules/python.c: main, which soon calls ./Modules/main.c: Py_Main). After some mundane initialization stuff (parse arguments, see if environment variables should affect behaviour, assess the situation of the standard streams and act accordingly, etc), [./Python/pythonrun.c: Py_Initialize](http://docs.python.org/c-api/init.html#Py_Initialize) is called. In many ways, this function is what ‘builds’ and assembles together the pieces needed to run the CPython machine and makes ‘a process’ into ‘a process with a Python interpreter in it’. Among other things, it creates two very important Python data-structures: the **interpreter state** and **thread state**. It also creates the built-in **module** [sys](http://docs.python.org/library/sys.html) and the module which hosts all [builtins](http://docs.python.org/library/functions.html#built-in-functions). At a later post(s) we will cover all these in depth. With these in place, Python will do one of several things based on how it was executed. Roughly, it will either execute a string (the -c option), execute a module as an executable (the -m option), or execute a file (passed explicitly on the commandline or passed by the kernel when used as an interpreter for a script) or run its [REPL](http://en.wikipedia.org/wiki/Read-eval-print_loop) loop (this is more a special case of the file to execute being an interactive device). In the case we’re currently following, it will execute a single string, since we invoked it with -c. To execute this single string, ./Python/pythonrun.c: PyRun_SimpleStringFlags is called. This function creates the __main__ **namespace**, which is ‘where’ our string will be executed (if you run $ python -c 'a=1; print(a)', where is a stored? in this namespace). After the namespace is created, the string is executed in it (or rather, interpreted or *evaluated* in it). To do that, you must first transform the string into something that machine can work on.

What about C?

- What are object files? [https://stackoverflow.com/questions/7718299/whats-an-object-file-in-c](https://stackoverflow.com/questions/7718299/whats-an-object-file-in-c)
- source+header —> (compiled to assembly) —> compiled (really assembled) to object files (machine code) —> linked into executable

How do I write a MakeFile?

[https://www.cs.oberlin.edu/~kuperman/help/make.html](https://www.cs.oberlin.edu/~kuperman/help/make.html)

Example of process generation

[https://github.com/remzi-arpacidusseau/ostep-code/tree/master/cpu-api](https://github.com/remzi-arpacidusseau/ostep-code/tree/master/cpu-api)

## Parsing

tiny intro [https://tomassetti.me/parsing-in-python/#useful](https://tomassetti.me/parsing-in-python/#useful)

lexing/tokenizing/scanning

parsing

building parse tree

building abstract syntax tree

interpreting/compiling from the AST

`exec` vs `eval`

[https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile](https://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile)

`exec` returns `None` and can take assignments, definitions, etc

this is the same for `compile` in `exec` mode

`eval` can take only expressions and returns their value

this is the same for `compile` in `eval` mode

`compile`  produces code objects

(ast.parse is written in Python and just calls compile(source, filename, mode, PyCF_ONLY_AST))

> If one looks into eval and exec source code in CPython 3, this is very evident; they both call PyEval_EvalCode with same arguments, the only difference being that exec explicitly returns None."

### libraries

[https://docs.python.org/release/3.6.1/library/tokenize.html](https://docs.python.org/release/3.6.1/library/tokenize.html)

[https://docs.python.org/release/3.6.1/library/parser.html](https://docs.python.org/release/3.6.1/library/parser.html)

[https://docs.python.org/release/3.6.1/library/ast.html](https://docs.python.org/release/3.6.1/library/ast.html)

what does this do?

    if __name__ == "__main__":
    	# some code

what does this do?

    import some_module

> The import statement combines two operations; it searches for the named module, then it binds the results of that search to a name in the local scope.

ASTs are like Lisp macros — it's how Python thinks of itself

[](https://www.notion.so/1513319ecc0443bd974318985e7a2514#ae6fe5870a7c40ea8fa76cf379157e6a)

[https://en.wikipedia.org/wiki/Application_binary_interface](https://en.wikipedia.org/wiki/Application_binary_interface)

# Bytecode

[https://opensource.com/article/18/4/introduction-python-bytecode](https://opensource.com/article/18/4/introduction-python-bytecode)

> CPython uses three types of stacks:

> The **call stack**. This is the main structure of a running Python program. It has one item—a "frame"—for each currently
active function call, with the bottom of the stack being the entry point of the program. Every function call pushes a new frame onto the call
stack, and every time a function call returns, its frame is popped off.

> In each frame, there's an **evaluation stack** (also called the **data stack**). This stack is where execution of a Python function occurs, and
executing Python code consists mostly of pushing things onto this stack, manipulating them, and popping them back off.

> Also in each frame, there's a **block stack**. This is used by Python to keep track of certain types of control structures: loops, `try`/`except` blocks, and `with` blocks all cause entries to be pushed onto the block stack, and the
block stack gets popped whenever you exit one of those structures. This
helps Python know which blocks are active at any given moment so that,
for example, a `continue` or `break` statement can affect the correct block.

# Python AST

the "docs":

[https://greentreesnakes.readthedocs.io/en/latest/](https://greentreesnakes.readthedocs.io/en/latest/nodes.html#function-and-class-definitions)

online ast explorer:

[https://python-ast-explorer.com/](https://python-ast-explorer.com/)

    import ast
    ast.parse<function parse at 0x7f062731d950
    ast.parse("x = 42")
    >>> <_ast.Module object at 0x7f0628a5ad10
    ast.dump(ast.parse("x = 42"))
    >>> "Module(body=[Assign(targets=[Name(id='x', ctx=Store())], value=Num(n=42))])"

    print(compile(ast.parse("x = 42"), '<input>', 'exec'))
    >>> <code object <module> at 0x111b3b0, file "<input>", line 1>
    eval(compile(ast.parse("x = 42"), '<input>', 'exec'))
    print(x)
    >>>42

    import ast
    class ReplaceBinOp(ast.NodeTransformer):
    """Replace operation by addition in binary operation"""
    	def visit_BinOp(self, node):
    	  return ast.BinOp(left=node.left,op=ast.Add(),right=node.right)

    tree = ast.parse("x = 1/3")
    ast.fix_missing_locations(tree)
    eval(compile(tree, '', 'exec'))
    print(ast.dump(tree))
    print(x)

    tree = ReplaceBinOp().visit(tree)
    ast.fix_missing_locations(tree)
    print(ast.dump(tree))
    eval(compile(tree, '', 'exec'))
    print(x)

### Hy examples (from Python hacker's guide)

S-expressions are just binary trees of atoms or pairs of s-expressions

[https://en.wikipedia.org/wiki/S-expression](https://en.wikipedia.org/wiki/S-expression)

building Python  from AST:

    hello_world = ast.Str(s='hello world!', lineno=1, col_offset=1)
    print_call = ast.Print(values=[hello_world], lineno=1, col_offset=1, nl=True)
    module = ast.Module(body=[print_call])
    code = compile(module, '', 'exec')
    eval(code)
    >>> hello world!

> An abstract syntax tree can be generated by passing ast.PyCF_ONLY_AST as a flag to the compile() built-in function, or using the parse() helper provided in this module. The result will be a tree of objects whose classes all inherit from ast.AST. An abstract syntax tree can be compiled into a Python code object using the built-in compile() function.