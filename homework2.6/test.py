import unittest
import task

class TestSequenceFunctions(unittest.TestCase):
    def failUnlessArraysAlmostEqual(self, first, second, places=7, msg=None):
        """Fail if the two arrays are unequal as determined by their
           difference rounded to the given number of decimal places
           (default 7) and comparing to zero.

           Note that decimal places (from zero) are usually not the same
           as significant digits (measured from the most signficant digit).
        """
        if (len(first) != len(second)):
            raise self.failureException, \
              (msg or '%r != %r because they have unequal lengths %d & %d', \
                  (first, second, len(first), len(second)))

        for i in range(len(first)):
            if isinstance(first[i], list):
                self.failUnlessArraysAlmostEqual(first[i], second[i], places, msg)
            elif round(abs(second[i]-first[i]), places) != 0:
                raise self.failureException, \
                (msg or '%r != %r within %r places' % (first, second, places))

    # Synonym methods
    assertArrayAlmostEqual = assertArrayAlmostEquals = failUnlessArraysAlmostEqual

    def test_dataset1(self):
        # ARRANGE
        expected_x = [[9.99934], [0.00131], [9.99890], [-19.9978]]
        expected_P = [[0.03955, 0.0, 0.06592, 0.0],
                      [0.0, 0.03955, 0.0, 0.06592],
                      [0.06592, 0.0, 0.10987, 0.0],
                      [0.0, 0.06592, 0.0, 0.10987]]


        task.measurements = [[5., 10.], [6., 8.], [7., 6.], [8., 4.], [9., 2.], [10., 0.]]
	task.initial_xy = [4., 12.]

        # ACT
        x, P = task.calculate()
        # ASSERT
	#self.assertArrayAlmostEquals(expected_x, actual_result)
	#self.assertArrayAlmostEquals(expected_P, actual_result)

    def test_dataset2(self):
        # ARRANGE
        expected_x = [[15.99333], [-7.99466], [49.98333], [-39.98667]]
#        expected_P = [[0.03955, 0.0, 0.06592, 0.0],
#                      [0.0, 0.03955, 0.0, 0.06592],
#                      [0.06592, 0.0, 0.10987, 0.0],
#                      [0.0, 0.06592, 0.0, 0.10987]]


        task.measurements = [[1., 4.], [6., 0.], [11., -4.], [16., -8.]]
	task.initial_xy = [-4., 8.]

        # ACT
        x, P = task.calculate()
        # ASSERT
	#self.assertArrayAlmostEquals(expected_x, actual_result)
	#self.assertArrayAlmostEquals(expected_P, actual_result)

    def test_dataset3(self):
        # ARRANGE
        expected_x = [[1.0], [11.00266], [0.0], [-19.99333]]
        expected_P = [[0.05331, 0.0, 0.13328, 0.0],
                      [0.0, 0.05331, 0.0, 0.13328],
                      [0.13328, 0.0, 0.33322, 0.0],
                      [0.0, 0.13328, 0.0, 0.33322]]


        task.measurements = [[1., 17.], [1., 15.], [1., 13.], [1., 11.]]
	task.initial_xy = [1., 19.]

        # ACT
        x, P = task.calculate()
        # ASSERT
	#self.assertArrayAlmostEquals(expected_x, actual_result)
	#self.assertArrayAlmostEquals(expected_P, actual_result)


    def test_dataset4(self):
        # ARRANGE
        expected_x = [[0.73342], [11.00266], [-0.66644], [-19.99333]]
        expected_P = [[0.05331, 0.0, 0.13328, 0.0],
                      [0.0, 0.05331, 0.0, 0.13328],
                      [0.13328, 0.0, 0.33322, 0.0],
                      [0.0, 0.13328, 0.0, 0.33322]]


        task.measurements = [[2., 17.], [0., 15.], [2., 13.], [0., 11.]]
	task.initial_xy = [1., 19.]

        # ACT
        x, P = task.calculate()
        # ASSERT
	#self.assertArrayAlmostEquals(expected_x, actual_result)
	#self.assertArrayAlmostEquals(expected_P, actual_result)

if __name__ == '__main__':
    unittest.main()
