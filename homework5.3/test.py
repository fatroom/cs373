import unittest
import task
from math import *

class TestSmoothing(unittest.TestCase):

    def assertSmoothingValid(self, path, fix, newpath_expected):
        path_persistent = [pair[:] for pair in path]
        fix_persistent = fix[:]

        newpath = task.smooth(path, fix)

        self.assertTrue(type(newpath) == type(newpath_expected),
                        "Function doesn't return a list")
        self.assertTrue(len(newpath) == len(newpath_expected),
                        "Newpath has the wrong length")
        self.assertEqual(path, path_persistent,
                         "Original path variable was modified by your code")
        self.assertEqual(fix, fix_persistent,
                         "Original fix variable was modified by your code")
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
        fix = [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
        newpath_expected = [[0, 0],
                            [0.7938620981547201, -0.8311168821106101],
                            [1.8579052986461084, -1.3834788165869276],
                            [3.053905318597796, -1.5745863173084],
                            [4.23141390533387, -1.3784271816058231],
                            [5.250184859723701, -0.8264215958231558],
                            [6, 0],
                            [6.415150091996651, 0.9836951698796843],
                            [6.41942442687092, 2.019512290770163],
                            [6, 3],
                            [5.206131365604606, 3.831104483245191],
                            [4.142082497497067, 4.383455704596517],
                            [2.9460804122779813, 4.5745592975708105],
                            [1.768574219397359, 4.378404668718541],
                            [0.7498089205417316, 3.826409771585794],
                            [0, 3],
                            [-0.4151464728194156, 2.016311854977891],
                            [-0.4194207879552198, 0.9804948340550833]]
        self.assertSmoothingValid(path, fix, newpath_expected)

    def test_secondPath(self):
        path = [[0, 0], # fix
                [2, 0],
                [4, 0], # fix
                [4, 2],
                [4, 4], # fix
                [2, 4],
                [0, 4], # fix
                [0, 2]]
        fix = [1, 0, 1, 0, 1, 0, 1, 0]
        answer = [[0, 0],
                  [2.0116767115496095, -0.7015439080661671],
                  [4, 0],
                  [4.701543905420104, 2.0116768147460418],
                  [4, 4],
                  [1.9883231877640861, 4.701543807525115],
                  [0, 4],
                  [-0.7015438099112995, 1.9883232808252207]]

        self.assertSmoothingValid(path, fix, answer)


if __name__ == "__main__":
    unittest.main()



