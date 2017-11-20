import mock
import unittest

from modular import Count

# test Count class
class TestCount(unittest.TestCase):

    def test_add(self):
        count = Count()
        count.add = mock.Mock(return_value=7)
        result = count.add(2,5)
        self.assertEqual(result,7)


if __name__ == '__main__':
    unittest.main()