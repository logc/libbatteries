import ctypes
import unittest

class TestDict(unittest.TestCase):

    def setUp(self):
        libbatteries = ctypes.CDLL('libbatteries.dylib')
        pystrings = ["key", "value"]
        cstrings = [ctypes.c_char_p(s) for s in pystrings]
        carr = (ctypes.c_char_p * len(cstrings))(*cstrings)
        self.dict = libbatteries.dict_new(carr)

    def test_get(self):
        expected = "value"
        actual = self.dict.get("key")
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
