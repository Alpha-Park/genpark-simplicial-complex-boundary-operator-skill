from client import SimplicialComplex
import collections

def main():
    print("=== Testing Simplicial Complex & Boundary Operator ===")
    sc = SimplicialComplex()

    triangle = (0, 1, 2)
    faces = sc.boundary_k(triangle)
    print("Boundary faces of 2-simplex (triangle):", faces)
    assert len(faces) == 3

    # Verify d(d(triangle)) == 0
    bb_sum = collections.defaultdict(int)
    for sign, face in faces:
        for s2, edge in sc.boundary_k(face):
            bb_sum[edge] += sign * s2

    assert all(v == 0 for v in bb_sum.values())
    print("Verified fundamental theorem of topology: d^2 == 0!")
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
