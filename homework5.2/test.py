import unittest
import task
from math import *

class TestSmoothing(unittest.TestCase):

    def assertSmoothingValid(self, path, newpath_expected):
        path_persistent = [pair[:] for pair in path]

        newpath = task.smooth(path)

        self.assertTrue(type(newpath) == type(newpath_expected),
                        "Function doesn't return a list")
        self.assertTrue(len(newpath) == len(newpath_expected),
                        "Newpath has the wrong length")
        self.assertEqual(path, path_persistent,
                         "Original path variable was modified by your code")
        for index, got, expected in zip(range(len(newpath_expected)), newpath, newpath_expected):
            self.assertTrue(type(got) == type(expected),
                            "Returned list doesn't contain a point at position %d" % index)
            self.assertTrue(len(got) == len(expected),
                            "Returned list doesn't contain a list of two coordinates "
                            "at position %d" % index)
            self.assertAlmostEqual(got[0], expected[0], 3,
                                   "X coordinate differs for point %d: "
                                   "expected %.3f, got %.3f" % (index, expected[0], got[0]))
            self.assertAlmostEqual(got[1], expected[1], 3,
                                   "Y coordinate differs for point %d: "
                                   "expected %.3f, got %.3f" % (index, expected[1], got[1]))
    
    def test_videoPath(self):
        path = [[0, 0],
                [1, 0],
                [2, 0],
                [3, 0],
                [4, 0],
                [5, 0],
                [6, 0],
                [6, 1],
                [6, 2],
                [6, 3],
                [5, 3],
                [4, 3],
                [3, 3],
                [2, 3],
                [1, 3],
                [0, 3],
                [0, 2],
                [0, 1]]
        newpath_expected = [[0.5449300156668018, 0.47485226780102946],
                            [1.2230705677535505, 0.2046277687200752],
                            [2.079668890615267, 0.09810778721159963],
                            [3.0000020176660755, 0.07007646364781912],
                            [3.9203348821839112, 0.09810853832382399],
                            [4.7769324511170455, 0.20462917195702085],
                            [5.455071854686622, 0.4748541381544533],
                            [5.697264197153936, 1.1249625336275617],
                            [5.697263485026567, 1.8750401628534337],
                            [5.455069810373743, 2.5251482916876378],
                            [4.776929339068159, 2.795372759575895],
                            [3.92033110541304, 2.9018927284871063],
                            [2.999998066091118, 2.929924058932193],
                            [2.0796652780381826, 2.90189200881968],
                            [1.2230677654766597, 2.7953714133566603],
                            [0.544928391271399, 2.5251464933327794],
                            [0.3027360471605494, 1.875038145804603],
                            [0.302736726373967, 1.1249605602741133]]
        self.assertSmoothingValid(path, newpath_expected)

    def test_secondPath(self):
        path = [[1, 0], # Move in the shape of a plus sign
                [2, 0],
                [2, 1],
                [3, 1],
                [3, 2],
                [2, 2],
                [2, 3],
                [1, 3],
                [1, 2],
                [0, 2], 
                [0, 1],
                [1, 1]]

        answer = [[1.239080543767428, 0.5047204351187283],
                  [1.7609243903912781, 0.5047216452560908],
                  [2.0915039821562416, 0.9085017167753027],
                  [2.495281862032503, 1.2390825203587184],
                  [2.4952805300504783, 1.7609262468826048],
                  [2.0915003641706296, 2.0915058211575475],
                  [1.7609195135622062, 2.4952837841027695],
                  [1.2390757942466555, 2.4952826072236918],
                  [0.9084962737918979, 2.091502621431358],
                  [0.5047183914625598, 1.7609219230352355],
                  [0.504719649257698, 1.2390782835562297],
                  [0.9084996902674257, 0.9084987462432871]]

        self.assertSmoothingValid(path, answer)


if __name__ == "__main__":
    unittest.main()



