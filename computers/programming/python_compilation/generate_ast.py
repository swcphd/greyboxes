import ast
from collections import defaultdict
import click
from graphviz import Digraph
from pprint import pprint


class AstGraphGenerator(object):
    def __init__(self):
        self.graph = defaultdict(lambda: [])

    def __str__(self):
        return str(self.graph)

    def visit(self, node):
        """Visit a node."""
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node."""
        for _, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        self.visit(item)

            elif isinstance(value, ast.AST):
                self.graph[type(node)].append(type(value))
                self.visit(value)


@click.command()
@click.argument('source', type=click.File('rb'))
def main(source):
    sourcetext = source.read()
    node = ast.parse(sourcetext)
    agg = AstGraphGenerator()
    agg.visit(node)
    pprint(ast.dump(node))
    pprint(agg.graph)
    graph = Digraph()
    graph.attr('node', shape='box')

    def draw_graph(dg, stree):
        # check if type is dict
        if isinstance(stree, dict):
            for k, v in stree.items():
                node_name = k
                # check if type is list
                if isinstance(v, list):
                    if len(v) == 2:
                        yes_node = v[0]
                        no_node = v[1]
                        dg.edge(node_name, yes_node)
                        dg.edge(node_name, no_node)
                    else:
                        yes_node = v[0]
                        dg.edge(node_name, yes_node)

    # draw_graph(graph, agg.graph)


if __name__ == "__main__":
    main()
