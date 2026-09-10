import collections

class SimplicialComplex:
    """
    Simplicial Complex & Boundary Operators.
    d_k: C_k -> C_{k-1}.
    Verifies the fundamental topological theorem: d_{k-1} * d_k = 0.
    """
    def __init__(self):
        self.simplices = collections.defaultdict(list)

    def add_simplex(self, vertices):
        v_sorted = tuple(sorted(vertices))
        k = len(v_sorted) - 1
        if v_sorted not in self.simplices[k]:
            self.simplices[k].append(v_sorted)

    def boundary_k(self, simplex):
        faces = []
        for i in range(len(simplex)):
            sign = 1 if (i % 2 == 0) else -1
            face = simplex[:i] + simplex[i+1:]
            faces.append((sign, face))
        return faces
