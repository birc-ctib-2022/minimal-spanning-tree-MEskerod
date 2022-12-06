"""
Testing.

I haven't written any tests, but if you want, you can add
some here.
"""
import sys

from prim_eloge import (prim, Edge)
from prim_eloge import Graph as Graph_eloge


"""Tests for prim_eloge"""
def build_graph_eloge(): 
    graph1 = Graph_eloge(
        (
            Edge(0, 0.1, 2),
            Edge(0, 2, 1),
            Edge(2, 12, 3),
            Edge(3, 2, 0),
            Edge(3, 0.2, 4),
            Edge(4, 1, 5),
            Edge(5, 1, 2)
        )
    )

    graph2 = Graph_eloge(
        (
            Edge(0, 3, 1),
            Edge(0, 6, 3),
            Edge(0, 9, 9),
            Edge(1, 2, 2),
            Edge(1, 4, 3),
            Edge(1, 9, 4),
            Edge(1, 9, 9),
            Edge(2, 2, 3),
            Edge(2, 8, 4),
            Edge(2, 9, 5),
            Edge(3, 9, 5),
            Edge(4, 7, 5), 
            Edge(4, 9, 7),
            Edge(4, 10, 8),
            Edge(4, 8, 9),
            Edge(5, 4, 6),
            Edge(5, 5, 7),
            Edge(6, 1, 7),
            Edge(6, 4, 8),
            Edge(7, 3, 8),
            Edge(8, 18, 9)
        )
    )

    return graph1, graph2

def test_prim() -> None: 
    graph1, graph2 = build_graph_eloge()

    assert prim(graph1) == [Edge(src=0, w=0.1, dst=2), Edge(src=2, w=1, dst=5), 
    Edge(src=5, w=1, dst=4), Edge(src=4, w=0.2, dst=3), Edge(src=0, w=2, dst=1)]

    assert prim(graph2) == [Edge(src=0, w=3, dst=1), Edge(src=1, w=2, dst=2), 
    Edge(src=2, w=2, dst=3), Edge(src=2, w=8, dst=4), Edge(src=4, w=7, dst=5), 
    Edge(src=5, w=4, dst=6), Edge(src=6, w=1, dst=7), Edge(src=7, w=3, dst=8), 
    Edge(src=4, w=8, dst=9)]

def test_graph_for_prim(capsys) -> None: 
    graph1, graph2 = build_graph_eloge()
    
    Graph_eloge(prim(graph1)).to_dot(sys.stdout)
    out, err = capsys.readouterr()
    assert out == 'graph { rankdir=LR;\n0 -- 2 [label="0.1"]\n0 -- 1 [label="2"]\n'\
        '2 -- 5 [label="1"]\n3 -- 4 [label="0.2"]\n4 -- 5 [label="1"]\n}\n'

    Graph_eloge(prim(graph2)).to_dot(sys.stdout)
    out, err = capsys.readouterr()
    assert out == 'graph { rankdir=LR;\n0 -- 1 [label="3"]\n1 -- 2 [label="2"]\n'\
        '2 -- 3 [label="2"]\n2 -- 4 [label="8"]\n4 -- 5 [label="7"]\n4 -- 9 '\
            '[label="8"]\n5 -- 6 [label="4"]\n6 -- 7 [label="1"]\n7 -- 8 [label="3"]\n}\n'


"""Tests for prim_elogv"""