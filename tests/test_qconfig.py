from queens.qconfig import QConfig
import unittest


class TestQConfig(unittest.TestCase):

    def test_total_num_valid_configs(self):
        calct = [QConfig(n).num_nonattacking_configs()
                 for n in range(10)]
        # See https://oeis.org/A000170
        expct = [1, 1, 0, 0, 2, 10, 4, 40, 92, 352]
        self.assertEqual(calct, expct)
