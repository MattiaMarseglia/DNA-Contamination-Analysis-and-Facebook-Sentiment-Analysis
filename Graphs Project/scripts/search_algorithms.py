# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def after_max_flow(g, s, discovered):
    """is a simple BFS called at the end of max flow process to find reachable path from the source"""
    level = [s]                        # first level includes only source
    while len(level) > 0:
      next_level = []                  # prepare to gather newly found vertices
      for u in level:
        for e in g.incident_edges(u):  # for every outgoing edge from u
          if e._element is not None and e._element > 0:
            v = e.opposite(u)
            if v not in discovered:      # v is an unvisited vertex
              discovered[v] = e          # e is the tree edge that discovered v
              next_level.append(v)       # v will be further considered in next pass
      level = next_level               # relabel 'next' level to become current


def search_if_path_exist(g, s, target, discovered):
    """Perform BFS of the undiscovered portion of Graph g starting at Vertex s.
    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the BFS (s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.
    this visited algorithm stop if it finds a vertex connected to the super target
    with an edge
    """
    level = [s]                        # first level includes only s
    while len(level) > 0:
      next_level = []                  # prepare to gather newly found vertices
      for u in level:
        for e in g.incident_edges(u):  # for every outgoing edge from u
          v = e.opposite(u)
          if v not in discovered:      # v is an unvisited vertex
            final_edge = g.get_edge(v, target)
            discovered[v] = e          # e is the tree edge that discovered v
            if final_edge is not None:
              discovered[target] = final_edge
              return
            next_level.append(v)       # v will be further considered in next pass
      level = next_level               # relabel 'next' level to become current


def construct_path_for_max_flow(path, u, v, discovered):
    """this function construct a path starting from discovered dict obtained in the previous BFS it finds also
    the bottleneck of the path (min) and return it"""
    min = None
    path.clear()
    if v in discovered:
        walk = v
        while walk is not u:
            e = discovered[walk]  # find edge leading to walk
            walk = e.opposite(walk)
            if min is None or min > e.element():
                min = e.element()
            path.append(e)
    return min


def find_a_path(graph, path, source, target, discovered):
    """this function find a path if exist call in sequence "search_if_path_exist" and "construct_path_for_max_flow" """
    discovered.clear()  # clear discovered for next path to find
    search_if_path_exist(graph, source, target, discovered)  # construct partial BFS algorithm useful for the particular path that it has to find
    return construct_path_for_max_flow(path, source, target, discovered)  # find the path from the super target to the super source if exist
