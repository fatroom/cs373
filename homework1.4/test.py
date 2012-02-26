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
        expected_result = [[0, 0, 0],
                           [0, 1, 0],
                           [0, 0, 0]]

        task.colors = [['green', 'green', 'green'],
                       ['green', 'red', 'green'],
                       ['green', 'green', 'green']]
        task.measurements = ['red']
        task.motions = [[0, 0]]
        task.sensor_right = 1.0
        task.p_move = 1.0

        # ACT
        actual_result = task.calculate()

        # ASSERT
        self.assertArrayAlmostEquals(expected_result, actual_result)

    def test_dataset2(self):
      # ARRANGE
        expected_result = [[0, 0, 0],
                           [0, 0.5, 0.5],
                           [0, 0, 0]]

        task.colors = [['green', 'green', 'green'],
                       ['green', 'red', 'red'],
                       ['green', 'green', 'green']]
        task.measurements = ['red']
        task.motions = [[0, 0]]
        task.sensor_right = 1.0
        task.p_move = 1.0

        # ACT
        actual_result = task.calculate()

        # ASSERT
        self.assertArrayAlmostEquals(expected_result, actual_result)

    def test_dataset3(self):
        # ARRANGE
        expected_result = [[0.06666, 0.06666, 0.06666],
                           [0.06666, 0.26666, 0.26666],
                           [0.06666, 0.06666, 0.06666]]

        task.colors = [['green', 'green', 'green'],
                       ['green', 'red', 'red'],
                       ['green', 'green', 'green']]
        task.measurements = ['red']
        task.motions = [[0, 0]]
        task.sensor_right = 0.8
        task.p_move = 1.0

        # ACT
        actual_result = task.calculate()

        # ASSERT
        self.assertArrayAlmostEquals(expected_result, actual_result, 4)

    def test_dataset4(self):
        # ARRANGE
        expected_result = [[0.03333, 0.03333, 0.03333],
                           [0.13333, 0.13333, 0.53333],
                           [0.03333, 0.03333, 0.03333]]

        task.colors = [['green', 'green', 'green'],
                       ['green', 'red', 'red'],
                       ['green', 'green', 'green']]
        task.measurements = ['red', 'red']
        task.motions = [[0, 0], [0, 1]]
        task.sensor_right = 0.8
        task.p_move = 1.0

        # ACT
        actual_result = task.calculate()

        # ASSERT
        self.assertArrayAlmostEquals(expected_result, actual_result, 4)

    def test_dataset5(self):
        # ARRANGE
        expected_result = [[0.0, 0.0, 0.0],
                           [0.0, 0.0, 1.0],
                           [0.0, 0.0, 0.0]]

        task.colors = [['green', 'green', 'green'],
                       ['green', 'red', 'red'],
                       ['green', 'green', 'green']]
        task.measurements = ['red', 'red']
        task.motions = [[0, 0], [0, 1]]
        task.sensor_right = 1.0
        task.p_move = 1.0

        # ACT
        actual_result = task.calculate()

        # ASSERT
        self.assertArrayAlmostEquals(expected_result, actual_result, 4)

    def test_dataset6(self):
        # ARRANGE
        expected_result = [[0.02898, 0.02898, 0.02898],
                           [0.07246, 0.28985, 0.46376],
                           [0.02898, 0.02898, 0.02898]]

        task.colors = [['green', 'green', 'green'],
                       ['green', 'red', 'red'],
                       ['green', 'green', 'green']]
        task.measurements = ['red', 'red']
        task.motions = [[0, 0], [0, 1]]
        task.sensor_right = 0.8
        task.p_move = 0.5

        # ACT
        actual_result = task.calculate()

        # ASSERT
        self.assertArrayAlmostEquals(expected_result, actual_result, 4)

    def test_dataset7(self):
        # ARRANGE
        expected_result = [[0.0, 0.0, 0.0],
                           [0.0, 0.33333, 0.66666],
                           [0.0, 0.0, 0.0]]

        task.colors = [['green', 'green', 'green'],
                       ['green', 'red', 'red'],
                       ['green', 'green', 'green']]
        task.measurements = ['red', 'red']
        task.motions = [[0, 0], [0, 1]]
        task.sensor_right = 1.0
        task.p_move = 0.5

        # ACT
        actual_result = task.calculate()

        # ASSERT
        self.assertArrayAlmostEquals(expected_result, actual_result, 4)


    def test_dataset8(self):
        # ARRANGE
        expected_result = [[0.01105, 0.02464, 0.06799, 0.04472, 0.024651],
                           [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
                           [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
                           [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]

        task.colors = [['red', 'green', 'green', 'red','red'],
                       ['red', 'red', 'green', 'red', 'red'],
                       ['red', 'red', 'green', 'green', 'red'],
                       ['red', 'red', 'red', 'red', 'red']]
        task.measurements = ['green', 'green', 'green', 'green', 'green']
        task.motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]
        task.sensor_right = 0.7
        task.p_move = 0.8

        # ACT
        actual_result = task.calculate()

        # ASSERT
        self.assertArrayAlmostEquals(expected_result, actual_result, 4)

    def test_dataset9(self):
        # ARRANGE
        expected_result = [[0.0, 0.0, 0.0],
                           [1.0, 0.0, 0.0],
                           [0.0, 0.0, 0.0]]

        task.colors = [['green', 'green', 'green'],
                       ['red', 'red', 'green'],
                       ['green', 'green', 'green']]
        task.measurements = ['red', 'red']
        task.motions = [[0, 0], [0, -1]]
        task.sensor_right = 1.0
        task.p_move = 1.0

        # ACT
        actual_result = task.calculate()

        # ASSERT
        self.assertArrayAlmostEquals(expected_result, actual_result, 4)

    def test_dataset10(self):
        # ARRANGE
        expected_result = [[0.0, 1.0, 0.0],
                           [0.0, 0.0, 0.0],
                           [0.0, 0.0, 0.0]]

        task.colors = [['green', 'red', 'green'],
                       ['green', 'red', 'green'],
                       ['green', 'green', 'green']]
        task.measurements = ['red', 'red']
        task.motions = [[0, 0], [-1, 0]]
        task.sensor_right = 1.0
        task.p_move = 1.0

        # ACT
        actual_result = task.calculate()

        # ASSERT
        self.assertArrayAlmostEquals(expected_result, actual_result, 4)

if __name__ == '__main__':
    unittest.main()
