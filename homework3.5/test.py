import unittest
from math import pi
import task

class TestSenseFunction(unittest.TestCase):

    def test_case1(self):
        length = 20.0
        bearing_noise  = 0.0
        steering_noise = 0.0
        distance_noise = 0.0
    		
        myrobot = task.robot(length)
        myrobot.set(30.0, 20.0, 0.0)
        myrobot.set_noise(bearing_noise, steering_noise, distance_noise)
    
        expected = [6.004885648174475, 3.7295952571373605, 1.9295669970654687, 0.8519663271732721]

        result = myrobot.sense()
        self.assertEquals(len(expected), len(result),
            "Measurement lengths differ: expected %d got %d" % (len(expected),
                                                                len(result)))
        for i, j in zip(expected, result):
            self.assertAlmostEquals(i, j, 7,
                "Measurements differ: expected %s, got %s" % (repr(expected), 
                                                              repr(result)))

    def test_case2(self):
        length = 20.0
        bearing_noise  = 0.0
        steering_noise = 0.0
        distance_noise = 0.0
    		
        myrobot = task.robot(length)
        myrobot.set(30.0, 20.0, pi / 5.0)
        myrobot.set_noise(bearing_noise, steering_noise, distance_noise)
        
        expected = [5.376567117456516, 3.101276726419402, 1.3012484663475101, 0.22364779645531352]

        result = myrobot.sense()
        self.assertEquals(len(expected), len(result),
            "Measurement lengths differ: expected %d got %d" % (len(expected),
                                                                len(result)))
        for i, j in zip(expected, result):
            self.assertAlmostEquals(i, j, 7,
                "Measurements differ: expected %s, got %s" % (repr(expected), 
                                                              repr(result)))


if __name__ == "__main__":
    unittest.main()
