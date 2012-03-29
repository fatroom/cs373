import unittest
from math import *
import random
import task

# -----------
# Test Case 1

testdata1          = [[[[1, 21.796713239511305, 25.32184135169971], [2, 15.067410969755826, -27.599928007267906]], [16.4522379034509, -11.372065246394495]],
                      [[[1, 6.1286996178786755, 35.70844618389858], [2, -0.7470113490937167, -17.709326161950294]], [16.4522379034509, -11.372065246394495]],
                      [[[0, 16.305692184072235, -11.72765549112342], [2, -17.49244296888888, -5.371360408288514]], [16.4522379034509, -11.372065246394495]],
                      [[[0, -0.6443452578030207, -2.542378369361001], [2, -32.17857547483552, 6.778675958806988]], [-16.66697847355152, 11.054945886894709]]]

answer_mu1         = task.matrix([[81.63549976607898],
                             [27.175270706192254],
                             [98.09737507003692],
                             [14.556272940621195],
                             [71.97926631050574],
                             [75.07644206765099],
                             [65.30397603859097],
                             [22.150809430682695]])

answer_omega1      = task.matrix([[0.36603773584905663, 0.0, -0.169811320754717, 0.0, -0.011320754716981133, 0.0, -0.1811320754716981, 0.0],
                             [0.0, 0.36603773584905663, 0.0, -0.169811320754717, 0.0, -0.011320754716981133, 0.0, -0.1811320754716981],
                             [-0.169811320754717, 0.0, 0.6509433962264151, 0.0, -0.05660377358490567, 0.0, -0.40566037735849064, 0.0],
                             [0.0, -0.169811320754717, 0.0, 0.6509433962264151, 0.0, -0.05660377358490567, 0.0, -0.40566037735849064],
                             [-0.011320754716981133, 0.0, -0.05660377358490567, 0.0, 0.6962264150943396, 0.0, -0.360377358490566, 0.0],
                             [0.0, -0.011320754716981133, 0.0, -0.05660377358490567, 0.0, 0.6962264150943396, 0.0, -0.360377358490566],
                             [-0.1811320754716981, 0.0, -0.4056603773584906, 0.0, -0.360377358490566, 0.0, 1.2339622641509433, 0.0],
                             [0.0, -0.1811320754716981, 0.0, -0.4056603773584906, 0.0, -0.360377358490566, 0.0, 1.2339622641509433]])

# -----------
# Test Case 2

testdata2          = [[[[0, 12.637647070797396, 17.45189715769647], [1, 10.432982633935133, -25.49437383412288]], [17.232472057089492, 10.150955955063045]],
                      [[[0, -4.104607680013634, 11.41471295488775], [1, -2.6421937245699176, -30.500310738397154]], [17.232472057089492, 10.150955955063045]],
                      [[[0, -27.157759429499166, -1.9907376178358271], [1, -23.19841267128686, -43.2248146183254]], [-17.10510363812527, 10.364141523975523]],
                      [[[0, -2.7880265859173763, -16.41914969572965], [1, -3.6771540967943794, -54.29943770172535]], [-17.10510363812527, 10.364141523975523]],
                      [[[0, 10.844236516370763, -27.19190207903398], [1, 14.728670653019343, -63.53743222490458]], [14.192077112147086, -14.09201714598981]]]

answer_mu2         = task.matrix([[63.37479912250136],
                             [78.17644539069596],
                             [61.33207502170053],
                             [67.10699675357239],
                             [62.57455560221361],
                             [27.042758786080363]])

answer_omega2      = task.matrix([[0.22871751620895048, 0.0, -0.11351536555795691, 0.0, -0.11351536555795691, 0.0],
                             [0.0, 0.22871751620895048, 0.0, -0.11351536555795691, 0.0, -0.11351536555795691],
                             [-0.11351536555795691, 0.0, 0.7867205207948973, 0.0, -0.46327947920510265, 0.0],
                             [0.0, -0.11351536555795691, 0.0, 0.7867205207948973, 0.0, -0.46327947920510265],
                             [-0.11351536555795691, 0.0, -0.46327947920510265, 0.0, 0.7867205207948973, 0.0],
                             [0.0, -0.11351536555795691, 0.0, -0.46327947920510265, 0.0, 0.7867205207948973]])


##########################################################

class SLAMTest(unittest.TestCase):

    def compare_matrices(self, expected, got, name, precision = 3):
        x = expected
        y = got
        for i, (xrow, yrow) in enumerate(zip(x.value, y.value)):
            for j, (xel, yel) in enumerate(zip(xrow, yrow)):
                self.assertAlmostEqual(xel, yel, precision,
                                       "The element at (%d, %d) in %s matrix differs: expected %.3f, got %.3f" % (i, j, name, xel, yel))

    def solution_check(self, result, answer_mu, answer_omega):
        self.assertTrue(len(result) == 2,
                        "Your function doesn't return both matrices mu and Omega")

        user_mu = result[0]
        user_omega = result[1]

        self.assertFalse(user_mu.dimx == answer_omega.dimx and user_mu.dimy == answer_omega.dimy,
                         "It looks like you returned your results in the wrong order. Make sure to return mu then Omega.")

        self.assertFalse(user_mu.dimx != answer_mu.dimx or user_mu.dimy != answer_mu.dimy,
                        "Your mu matrix doesn't have the correct dimensions. Mu should be a %dx%d matrix." % (answer_mu.dimx, answer_mu.dimy))

        self.assertFalse(user_omega.dimx != answer_omega.dimx or user_omega.dimy != answer_omega.dimy,
                        "Your Omega matrix doesn't have the correct dimensions. Mu should be a %dx%d matrix." % (answer_omega.dimx, answer_omega.dimy))

        self.compare_matrices(answer_omega, user_omega, "Omega")
        self.compare_matrices(answer_mu, user_mu, "mu")

    def test_provided1(self):
        result = task.online_slam(testdata1, 5, 3, 2.0, 2.0)
        self.solution_check(result, answer_mu1, answer_omega1)

    def test_provided2(self):
        result = task.online_slam(testdata2, 6, 2, 3.0, 4.0)
        self.solution_check(result, answer_mu2, answer_omega2)

    def test_random(self):
        data = task.make_data(task.N, task.num_landmarks, task.world_size, task.measurement_range, task.motion_noise, task.measurement_noise, task.distance)
        result = task.slam(data, task.N, task.num_landmarks, task.motion_noise, task.measurement_noise)
        online_result = task.online_slam(data, task.N, task.num_landmarks, task.motion_noise, task.measurement_noise)
        mapping = [i - 2 + task.N*2 for i in range(2 * task.num_landmarks)]
        e_result = result.take(mapping, [0])
        self.compare_matrices(e_result, online_result[0], "mu", 2)

if __name__ == "__main__":
    unittest.main()
