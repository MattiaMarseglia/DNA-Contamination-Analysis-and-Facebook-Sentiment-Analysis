from graph import Graph


class MaxFlowGraph(Graph):

    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x.
        if exists update its value."""
        if self.get_edge(u, v) is not None:      # includes error checking
            self._outgoing[u][v]._element = x
            self._incoming[v][u]._element = x
        else:
            e = self.Edge(u, v, x)
            self._outgoing[u][v] = e
            self._incoming[v][u] = e


    def remove_edge(self, u, v):
        """remove an Edge from u to v with auxiliary element x if exists.
        Raise a ValueError if u and v are not vertices of the graph."""
        self._validate_vertex(u)
        self._validate_vertex(v)
        if v in self._outgoing[u]:
            del self._outgoing[u][v]
        if u in self._incoming[v]:
            del self._incoming[v][u]
