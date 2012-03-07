import unittest
from math import pi
import task

class TestMoveFunction(unittest.TestCase):
    """ This test works using representation of robots by its __repr__
        function
    """

    def test_case1(self):
        length = 20.0
        bearing_noise = 0.0
        steering_noise = 0.0
        distance_noise = 0.0

        myrobot = task.robot(length)
        myrobot.set(0.0, 0.0, 0.0)
        myrobot.set_noise(bearing_noise, steering_noise, distance_noise)

        motions = [[0.0, 10.0], [pi / 6.0, 10], [0.0, 20.0]]

        expected_repr = ["[x=0.0 y=0.0 orient=0.0]",
                         "[x=10.0 y=0.0 orient=0.0]",
                         "[x=19.861 y=1.4333 orient=0.2886]",
                         "[x=39.034 y=7.1270 orient=0.2886]"]

        self.assertEquals(
            expected_repr[0], 
            repr(myrobot),
            "On initialization step: expected %s got %s" % (expected_repr[0],
                                                            repr(myrobot)))
        for m in range(len(motions)):
            myrobot = myrobot.move(motions[m])
            self.assertEquals(
                expected_repr[m+1], 
                repr(myrobot),
                "On step %d: expected %s got %s" % (m,
                                                    expected_repr[m+1],
                                                    repr(myrobot)))


    def test_case2(self):
        length = 20.0
        bearing_noise = 0.0
        steering_noise = 0.0
        distance_noise = 0.0

        myrobot = task.robot(length)
        myrobot.set(0.0, 0.0, 0.0)
        myrobot.set_noise(bearing_noise, steering_noise, distance_noise)

        motions = [[0.2, 10.] for row in range(10)]

        expected_repr = ["[x=0.0 y=0.0 orient=0.0]",
                         "[x=9.9828 y=0.5063 orient=0.1013]",
                         "[x=19.863 y=2.0201 orient=0.2027]",
                         "[x=29.539 y=4.5259 orient=0.3040]",
                         "[x=38.913 y=7.9979 orient=0.4054]",
                         "[x=47.887 y=12.400 orient=0.5067]",
                         "[x=56.369 y=17.688 orient=0.6081]",
                         "[x=64.273 y=23.807 orient=0.7094]",
                         "[x=71.517 y=30.695 orient=0.8108]",
                         "[x=78.027 y=38.280 orient=0.9121]",
                         "[x=83.736 y=46.485 orient=1.0135]"]
        self.assertEquals(
            expected_repr[0], 
            repr(myrobot),
            "On initialization step: expected %s got %s" % (expected_repr[0],
                                                            repr(myrobot)))
        for m in range(len(motions)):
            myrobot = myrobot.move(motions[m])
            self.assertEquals(
                expected_repr[m+1], 
                repr(myrobot),
                "On step %d: expected %s got %s" % (m,
                                                    expected_repr[m+1],
                                                    repr(myrobot)))

if __name__ == "__main__":
    unittest.main()
