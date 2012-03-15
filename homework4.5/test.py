import unittest
import task

class TestMotion(unittest.TestCase):
    def compare_values(self, expected, got):
        self.assertEqual(len(expected), len(got),
            "Value lists have different size: expected %d, got %d" % (len(expected), len(got)))
        for i, row in enumerate(expected):
            self.assertEqual(len(expected[i]), len(got[i]),
                "Value lists have different size: expected %d, got %d in line %d" % (len(expected[i]), len(got[i]), i))
            for j, _ in enumerate(row):
                self.assertAlmostEqual(expected[i][j], got[i][j], 3,
                    "Values differ: expected %.3f got %.3f at [%d][%d]" % (expected[i][j], got[i][j], i, j))

    def compare_policies(self, expected, got):
        self.assertEqual(len(expected), len(got),
            "Policy lists have different size: expected %d, got %d" % (len(expected), len(got)))
        for i, row in enumerate(expected):
            self.assertEqual(len(expected[i]), len(got[i]),
                "Policy lists have different size: expected %d, got %d in line %d" % (len(expected[i]), len(got[i]), i))
            for j, _ in enumerate(row):
                self.assertTrue(got[i][j] in expected[i][j],
                                 "Policies differ: expected %s, got %s at [%d][%d]" % (expected[i][j], got[i][j], i, j))
        #self.assertEqual(expected, got)

    def test_small_1(self):
        exp_value = [[60.472, 37.193, 0.000],
                     [63.503, 44.770, 37.193]]
        exp_policy = [['>', '>', '*'],
                      ['>', '^', '^']]
        task.grid = [[0, 0, 0],
                     [0, 0, 0]]
        task.goal = [0, len(task.grid[0])-1] # Goal is in top right corner
        task.success_prob = 0.5
        task.failure_prob = (1.0 - task.success_prob)/2.0 
        value, policy = task.stochastic_value()
        self.compare_values(exp_value, value)
        self.compare_policies(exp_policy, policy)

    def test_small_2(self):
        exp_value = [[94.041, 1000.000, 0.000],
                     [86.082, 73.143, 44.286]]
        exp_policy = [['v', ' ', '*'],
                      ['>', '>', '^']]
        task.grid = [[0, 1, 0],
                     [0, 0, 0]]
        task.goal = [0, len(task.grid[0])-1] # Goal is in top right corner
        task.success_prob = 0.5
        task.failure_prob = (1.0 - task.success_prob)/2.0 
        value, policy = task.stochastic_value()
        self.compare_values(exp_value, value)
        self.compare_policies(exp_policy, policy)

    def test_big(self):
        exp_value = [[57.903, 40.278, 26.066, 0.000],
                     [47.055, 36.572, 29.994, 27.270],
                     [53.172, 42.023, 37.775, 45.092],
                     [77.586, 1000.000, 1000.000, 73.546]]
        exp_policy = [['>', 'v', 'v', '*'],
                      ['>', '>', '^', '<'],
                      ['>', '^', '^', '<'],
                      ['^', ' ', ' ', '^']]
        task.grid = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 1, 1, 0]]
        task.goal = [0, len(task.grid[0])-1] # Goal is in top right corner
        task.success_prob = 0.5
        task.failure_prob = (1.0 - task.success_prob)/2.0 
        value, policy = task.stochastic_value()
        self.compare_values(exp_value, value)
        self.compare_policies(exp_policy, policy)

    def test_big_nofail(self):
        exp_value = [[3.000, 2.000, 1.000, 0.000],
                     [4.000, 3.000, 2.000, 1.000],
                     [5.000, 4.000, 3.000, 2.000],
                     [6.000, 1000.000, 1000.000, 3.000]]
        exp_policy = [['>',  '>',  '>',  '*'],
                      ['^>', '^>', '^>', '^'],
                      ['^>', '^>', '^>', '^'],
                      ['^',  ' ',  ' ',  '^']]
        task.grid = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 1, 1, 0]]
        task.goal = [0, len(task.grid[0])-1] # Goal is in top right corner
        task.success_prob = 1.0
        task.failure_prob = (1.0 - task.success_prob)/2.0 
        value, policy = task.stochastic_value()
        self.compare_values(exp_value, value)
        self.compare_policies(exp_policy, policy)
        
if __name__ == "__main__":
    unittest.main()

