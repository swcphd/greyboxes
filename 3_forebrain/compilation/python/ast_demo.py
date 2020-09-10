import ast

module = ast.Module(
    lineno=1,
    col_offset=0,
    body=[
        ast.Expr(
            lineno=1,
            col_offset=0,
            value=ast.Call(
                keywords=[],
                lineno=1,
                col_offset=0,
                func=ast.Name(
                    id='print',
                    ctx=ast.Load(),
                    lineno=1,
                    col_offset=0,
                ),
                args=[ast.Str(
                    s=u'Hello',
                    lineno=1,
                    col_offset=0,
                )]))
    ])

code = compile(module, 'test.py', 'exec')
print(type(code))
exec(code)
