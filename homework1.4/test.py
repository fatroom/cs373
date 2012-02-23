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

  def test_dataset2(self):
    expected_result=[[0,0,0],[0,0.5,0.5],[0,0,0]]

    task.colors = [['green','green','green'],
                   ['green','red','red'],
                   ['green','green','green']]	
    task.measurements=['red']
    task.motions=[[0,0]]
    task.sensor_right=1.0
    task.p_move=1.0

    p = task.calculate()

    self.assertEqual(expected_result, p)

  def test_dataset3(self):
    expected_result=[[0.06666,0.06666, 0.06666],[0.06666,0.26666,0.26666],[0.06666,0.06666,0.06666]]

    task.colors = [['green','green','green'],
                   ['green','red','red'],
                   ['green','green','green']]	
    task.measurements=['red']
    task.motions=[[0,0]]
    task.sensor_right=0.8
    task.p_move=1.0

    p = task.calculate()

    for i in range(len(p)):
      for j in range(len(p[1])):
        p[i][j] = round(p[i][j],4)

    for i in range(len(expected_result)):
      for j in range(len(expected_result[1])):
        expected_result[i][j] = round(expected_result[i][j],4)

    self.assertEqual(expected_result, p)

  def test_dataset4(self):
    expected_result=[[0.03333, 0.03333, 0.03333],
                     [0.13333, 0.13333, 0.53333],
                     [0.03333, 0.03333, 0.03333]]

    task.colors = [['green', 'green', 'green'],
                   ['green', 'red', 'red'],
                   ['green', 'green', 'green']]	
    task.measurements=['red', 'red']
    task.motions=[[0,0], [0, 1]]
    task.sensor_right=0.8
    task.p_move=1.0

    p = task.calculate()

    for i in range(len(p)):
      for j in range(len(p[1])):
        p[i][j] = round(p[i][j],4)

    for i in range(len(expected_result)):
      for j in range(len(expected_result[1])):
        expected_result[i][j] = round(expected_result[i][j],4)

    self.assertEqual(expected_result, p)

  def test_dataset5(self):
    expected_result=[[0.0, 0.0, 0.0],
                     [0.0, 0.0, 1.0],
                     [0.0, 0.0, 0.0]]

    task.colors = [['green', 'green', 'green'],
                   ['green', 'red', 'red'],
                   ['green', 'green', 'green']]	
    task.measurements=['red', 'red']
    task.motions=[[0,0], [0, 1]]
    task.sensor_right=1.0
    task.p_move=1.0

    p = task.calculate()

    self.assertEqual(expected_result, p)

  def test_dataset6(self):
    expected_result=[[0.02898, 0.02898, 0.02898],
                     [0.07246, 0.28985, 0.46376],
                     [0.02898, 0.02898, 0.02898]]

    task.colors = [['green', 'green', 'green'],
                   ['green', 'red', 'red'],
                   ['green', 'green', 'green']]	
    task.measurements=['red', 'red']
    task.motions=[[0,0], [0, 1]]
    task.sensor_right=.8
    task.p_move=0.5

    p = task.calculate()

    for i in range(len(p)):
      for j in range(len(p[1])):
        p[i][j] = round(p[i][j],4)

    for i in range(len(expected_result)):
      for j in range(len(expected_result[1])):
        expected_result[i][j] = round(expected_result[i][j],4)

    self.assertEqual(expected_result, p)

  def test_dataset7(self):
    expected_result=[[0.0, 0.0, 0.0],
                     [0.0, 0.33333, 0.66666],
                     [0.0, 0.0, 0.0]]

    task.colors = [['green', 'green', 'green'],
                   ['green', 'red', 'red'],
                   ['green', 'green', 'green']]	
    task.measurements=['red', 'red']
    task.motions=[[0,0], [0, 1]]
    task.sensor_right=1.0
    task.p_move=0.5

    p = task.calculate()

    for i in range(len(p)):
      for j in range(len(p[1])):
        p[i][j] = round(p[i][j],4)

    for i in range(len(expected_result)):
      for j in range(len(expected_result[1])):
        expected_result[i][j] = round(expected_result[i][j],4)

    self.assertEqual(expected_result, p)

 
if __name__ == '__main__':
  unittest.main()
