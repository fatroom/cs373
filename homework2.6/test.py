
import unittest
import task
from task import matrix

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
    measurements = [[5., 10.], [6., 8.], [7., 6.], [8., 4.], [9., 2.], [10., 0.]]
    initial_xy = [4., 12.]
    expected_x = matrix([[9.9993407317877168],[0.001318536424568617],[9.9989012196461928],[-19.997802439292386]])
    expected_P = matrix([[0.039556092737061982, 0.0, 0.06592682122843721, 0.0], [0.0, 0.039556092737061982, 0.0, 0.06592682122843721], [0.065926821228437182, 0.0, 0.10987803538073201, 0.0], [0.0, 0.065926821228437182, 0.0, 0.10987803538073201]])

    # ACT
    x, P = task.calculate(measurements, initial_xy)

    # ASSERT
    self.assertArrayAlmostEquals(expected_x.value, x.value)
    self.assertArrayAlmostEquals(expected_P.value, P.value)
    
  def test_dataset2(self):
    # ARRANGE
    measurements = [[1., 4.], [6., 0.], [11., -4.], [16., -8.]]
    initial_xy = [-4., 8.]
    expected_x = matrix([[15.993335554815062], [-7.9946684438520501], [49.983338887037647], [-39.986671109630123]])

    # ACT
    x, P = task.calculate(measurements, initial_xy)

    # ASSERT
    self.assertArrayAlmostEquals(expected_x.value, x.value)
    
  def test_dataset3(self):
    # ARRANGE
    measurements = [[1., 17.], [1., 15.], [1., 13.], [1., 11.]]
    initial_xy = [1., 19.]
    expected_x = matrix([[1.0], [11.002665778073975], [0.0], [-19.993335554815054]])
    expected_P = matrix([[0.053315561479506911, 0.0, 0.13328890369876803, 0.0], [0.0, 0.053315561479506911, 0.0, 0.13328890369876803], [0.13328890369876789, 0.0, 0.33322225924692717, 0.0], [0.0, 0.13328890369876789, 0.0, 0.333222259246027171]])

    # ACT
    x, P = task.calculate(measurements, initial_xy)

    # ASSERT
    self.assertArrayAlmostEquals(expected_x.value, x.value)
    self.assertArrayAlmostEquals(expected_P.value, P.value)
    
  def test_dataset4(self):
    # ARRANGE
    measurements = [[2., 17.], [0., 15.], [2., 13.], [0., 11.]]
    initial_xy = [1., 19.]
    expected_x = matrix([[0.73342219260246477], [11.002665778073975], [-0.66644451849384057], [-19.993335554815054]])
    expected_P = matrix([[0.053315561479506911, 0.0, 0.13328890369876803, 0.0], [0.0, 0.053315561479506911, 0.0, 0.13328890369876803], [0.13328890369876789, 0.0, 0.33322225924692717, 0.0], [0.0, 0.13328890369876789, 0.0, 0.333222259246027171]])

    # ACT
    x, P = task.calculate(measurements, initial_xy)

    # ASSERT
    self.assertArrayAlmostEquals(expected_x.value, x.value)
    self.assertArrayAlmostEquals(expected_P.value, P.value)

if __name__ == '__main__':
  unittest.main()
