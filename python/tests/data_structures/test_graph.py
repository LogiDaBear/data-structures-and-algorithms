import pytest
from data_structures.graph import Graph, Vertex


def test_exists():
    assert Graph


# @pytest.mark.skip("TODO")
def test_add_node():

    graph = Graph()

    expected = "spam"  # a vertex's value that comes back

    actual = graph.add_node("spam").value

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_size():

    graph = Graph()

    graph.add_node("spam")

    expected = 1

    actual = graph.size()

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_add_edge():
    g = Graph()
    apple = g.add_node("apple")
    banana = g.add_node("banana")
    g.add_edge(apple, banana, 5)
    neighbors = g.get_neighbors(apple)
    assert len(neighbors) == 1
    assert neighbors[0].vertex.value == "banana"
    assert neighbors[0].weight == 5


# @pytest.mark.skip("TODO")
def test_bouquet():
    g = Graph()
    apple = g.add_node("apple")
    g.add_edge(apple, apple, 10)
    neighbors = g.get_neighbors(apple)
    assert len(neighbors) == 1
    assert neighbors[0].vertex.value == "apple"
    assert neighbors[0].weight == 10


# @pytest.mark.skip("TODO")
def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex("start")

    end = graph.add_node("end")

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


# @pytest.mark.skip("TODO")
def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex("end")

    start = graph.add_node("start")

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


# @pytest.mark.skip("TODO")
def test_get_nodes():
    graph = Graph()
    banana = graph.add_node("banana")
    apple = graph.add_node("apple")
    loner = Vertex("loner")
    expected = 2
    actual = len(graph.get_vertices())  # Fixed: Use get_vertices() instead of get_nodes()
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == "banana"

    assert neighbor_edge.weight == 44


# @pytest.mark.skip("TODO")
def test_happy_path():
    g = Graph()
    apple = g.add_vertex("apple")
    banana = g.add_vertex("banana")
    cherry = g.add_vertex("cherry")
    date = g.add_vertex("date")
    g.add_edge(apple, banana, 5)
    g.add_edge(apple, cherry, 7)
    g.add_edge(cherry, banana, 9)
    g.add_edge(cherry, date, 11)
    actual = g.get_vertices()
    assert len(actual) == 4
    assert apple in actual
    assert banana in actual
    assert cherry in actual
    assert date in actual
    neighbors = g.get_neighbors(cherry)
    assert len(neighbors) == 2
    assert neighbors[0].vertex.value == "banana"
    assert neighbors[0].weight == 9
    assert neighbors[1].vertex.value == "date"
    assert neighbors[1].weight == 11
    neighbors = g.get_neighbors(banana)
    assert len(neighbors) == 0
    neighbors = g.get_neighbors(date)
    assert len(neighbors) == 0
    neighbors = g.get_neighbors(apple)
    assert len(neighbors) == 2
    assert neighbors[0].vertex.value == "banana"
    assert neighbors[0].weight == 5
    assert neighbors[1].vertex.value == "cherry"
    assert neighbors[1].weight == 7
    assert g.size() == 4

def test_vertex_added_successfully():
    graph = Graph()
    vertex = graph.add_node("test_vertex")
    assert vertex in graph.get_vertices()


def test_edge_added_successfully():
    graph = Graph()
    vertex_a = graph.add_node("vertex_a")
    vertex_b = graph.add_node("vertex_b")
    graph.add_edge(vertex_a, vertex_b, weight=5)
    neighbors = graph.get_neighbors(vertex_a)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == vertex_b
    assert neighbors[0].weight == 5


def test_get_all_vertices():
    graph = Graph()
    vertex_a = graph.add_node("vertex_a")
    vertex_b = graph.add_node("vertex_b")
    vertex_c = graph.add_node("vertex_c")
    vertices = graph.get_vertices()
    assert len(vertices) == 3
    assert vertex_a in vertices
    assert vertex_b in vertices
    assert vertex_c in vertices


def test_get_neighbors_with_weight():
    graph = Graph()
    vertex_a = graph.add_node("vertex_a")
    vertex_b = graph.add_node("vertex_b")
    graph.add_edge(vertex_a, vertex_b, weight=7)
    neighbors = graph.get_neighbors(vertex_a)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == vertex_b
    assert neighbors[0].weight == 7


def test_proper_size():
    graph = Graph()
    vertex_a = graph.add_node("vertex_a")
    vertex_b = graph.add_node("vertex_b")
    vertex_c = graph.add_node("vertex_c")
    assert graph.size() == 3


def test_graph_with_single_vertex_and_edge():
    graph = Graph()
    vertex_a = graph.add_node("vertex_a")
    graph.add_edge(vertex_a, vertex_a, weight=10)
    assert graph.size() == 1
    neighbors = graph.get_neighbors(vertex_a)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == vertex_a
    assert neighbors[0].weight == 10
