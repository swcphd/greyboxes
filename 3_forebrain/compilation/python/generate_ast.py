import ast
import click
from astmonkey import visitors, transformers
import os

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    node = ast.parse(open(filename).read())
    node = transformers.ParentChildNodeTransformer().visit(node)
    visitor = visitors.GraphNodeVisitor()
    visitor.visit(node)
    visitor.graph.write_png('graph.png')
    os.system("open graph.png")

if __name__ == "__main__":
    main()
