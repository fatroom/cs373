import unittest
import task

class TestSequenceFunctions(unittest.TestCase):

  def test_dataset1(self):
    expected_result=[[0,0,0],[0,1,0],[0,0,0]]

    task.colors = [['green','green','green'],
                   ['green','red','green'],
                   ['green','green','green']]	
    task.measurements=['red']
    task.motions=[[0,0]]
    task.sensor_right=1.0
    task.p_move=1.0

    p = task.calculate()

    self.assertEqual(expected_result, p)

if __name__ == '__main__':
  unittest.main()
