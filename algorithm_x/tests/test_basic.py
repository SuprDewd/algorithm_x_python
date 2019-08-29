from unittest import TestCase
import random
from algorithm_x import AlgorithmX

def normalize(sol):
    return list(sorted([ list(sorted(s)) for s in sol ]))

class TestBasic(TestCase):

    def test_knuth(self):
        solver = AlgorithmX(7)
        solver.appendRow([2, 4, 5], 'A')
        solver.appendRow([0, 3, 6], 'B')
        solver.appendRow([1, 2, 5], 'C')
        solver.appendRow([0, 3], 'D')
        solver.appendRow([1, 6], 'E')
        solver.appendRow([3, 4, 6], 'F')
        self.assertEqual(normalize(solver.solve()), [['A','D','E']])

    def test_knuth2(self):
        solver = AlgorithmX(7)
        solver.appendRow([2, 4, 5])
        solver.appendRow([0, 3, 6])
        solver.appendRow([1, 2, 5])
        solver.appendRow([0, 3])
        solver.appendRow([1, 6])
        solver.appendRow([3, 4, 6])
        self.assertEqual(normalize(solver.solve()), [[0,3,4]])

    def test_nocol(self):
        solver = AlgorithmX(0)
        solver.appendRow([])
        solver.appendRow([])
        self.assertEqual(normalize(solver.solve()), [[]])

    def test_nocol_empty(self):
        solver = AlgorithmX(0)
        self.assertEqual(normalize(solver.solve()), [[]])

    def test_onecol(self):
        solver = AlgorithmX(1)
        solver.appendRow([0])
        self.assertEqual(normalize(solver.solve()), [[0]])

    def test_onecol2(self):
        solver = AlgorithmX(1)
        solver.appendRow([0])
        solver.appendRow([0])
        self.assertEqual(normalize(solver.solve()), [[0],[1]])

    def test_random_all(self):
        for it in range(100):
            n = 10
            rem = [True]*n
            solver = AlgorithmX(n)

            cnt = 0
            while any(rem):
                left = [ i for i in range(n) if rem[i] ]
                random.shuffle(left)
                take = left[:random.randint(1,len(left))]
                cnt += 1
                solver.appendRow(take)
                for i in take:
                    rem[i] = False

            self.assertEqual(normalize(solver.solve()), [list(range(cnt))])

    def test_random_all_plus_trash(self):
        for it in range(100):
            n = 10
            rem = [True]*n
            solver = AlgorithmX(n)

            cnt = 0
            rows = []
            while any(rem):
                left = [ i for i in range(n) if rem[i] ]
                random.shuffle(left)
                take = left[:random.randint(1,len(left))]
                cnt += 1
                rows.append((take, True))
                for i in take:
                    rem[i] = False

            for add in range(20):
                cur = list(range(n))
                random.shuffle(cur)
                cur = cur[:random.randint(0,len(cur))]
                rows.append((cur, False))

            random.shuffle(rows)
            base = []
            for i, (row, is_base) in enumerate(rows):
                if is_base:
                    base.append(i)
                solver.appendRow(row)

            found = False
            for sol in solver.solve():
                if sorted(sol) == base:
                    found = True

                cnt = [0]*n
                for i in sol:
                    for j in rows[i][0]:
                        cnt[j] += 1

                for c in cnt:
                    self.assertEqual(c, 1)

            self.assertTrue(found)


