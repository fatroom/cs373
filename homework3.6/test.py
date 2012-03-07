import unittest
from math import pi
import task
import random

class TestRobot(unittest.TestCase):

    def test_case1(self):
        motions = [[2. * pi / 10, 20.] for row in range(8)]
        measurements = [[4.746936, 3.859782, 3.045217, 2.045506],
                        [3.510067, 2.916300, 2.146394, 1.598332],
                        [2.972469, 2.407489, 1.588474, 1.611094],
                        [1.906178, 1.193329, 0.619356, 0.807930],
                        [1.352825, 0.662233, 0.144927, 0.799090],
                        [0.856150, 0.214590, 5.651497, 1.062401],
                        [0.194460, 5.660382, 4.761072, 2.471682],
                        [5.717342, 4.736780, 3.909599, 2.342536]]
        
        expected = [93.476, 75.186, 5.2664]

        result = task.particle_filter(motions, measurements)

        self.assertTrue(abs(result[0] - expected[0]) < task.tolerance_xy,
            "predicted X=%f is far away from expected %f" % (result[0],
                                                             expected[0]))
        self.assertTrue(abs(result[1] - expected[1]) < task.tolerance_xy,
            "predicted Y=%f is far away from expected %f" % (result[1],
                                                             expected[1]))
        self.assertTrue(abs(result[2] - expected[2]) < task.tolerance_orientation,
            "predicted orientation=%f is far away from expected %f" % (result[2],
                                                                       expected[2]))

    def test_case2(self):
        number_of_cycles = 50
        number_to_success = 45
        number_succeeded = 0
        for cycle in range(number_of_cycles):
            number_of_iterations = random.randint(2, 100)
            motions = [[2. * pi / 20, 12.] for row in range(number_of_iterations)]
            
            x = task.generate_ground_truth(motions)
            final_robot = x[0]
            measurements = x[1]
            estimated_position = task.particle_filter(motions, measurements)

            if task.check_output(final_robot, estimated_position):
                number_succeeded += 1
        
        print "TEST: Succeeded %d runs of %d" % (number_succeeded,
                                                 number_of_cycles)
        if number_succeeded < number_to_success:
            self.assertTrue(False, "Too small succes ratio")


if __name__ == "__main__":
    unittest.main()
