import unittest

from oving9.RLEString import RLEString

uncompressed = ["AAA", "AABB", "ABAB", "AAAAAAAAAA"]
compressed = ['3A', "2A2B", "1A1B1A1B", "10A"]
nonalphabetic = [123, "AAA BBB", "ABC!", "3A"]


class Assignment8Tests(unittest.TestCase):
    def test_compress_correctly(self):
        i = 0
        for s in uncompressed:
            rle = RLEString(s)
            rle.compress()
            self.assertEqual(compressed[i], str(rle))
            i += 1

    def test_decompress_correctly(self):
        for s in uncompressed:
            rle = RLEString(s)
            rle.compress()
            rle.decompress()
            self.assertEqual(s, str(rle))

    def test_exception_nonalphabetic(self):
        for s in nonalphabetic:
            with self.assertRaises(Exception):
                RLEString(s)

    def test_exception_compress(self):
        rle = RLEString("AAA")
        rle.compress()
        with self.assertRaises(Exception):
            rle.compress()

    def test_exception_decompress(self):
        rle = RLEString("AAA")
        with self.assertRaises(Exception):
            rle.decompress()

    def test_exception_emptystring(self):
        with self.assertRaises(Exception):
            RLEString("")

    def test_return_string(self):
        rle = RLEString("AAA")
        self.assertIsInstance(str(rle), str)

    def test_return_compressed(self):
        rle = RLEString("AAA")
        rle.compress()
        self.assertTrue(rle.iscompressed())

    def test_multiple_compress(self):
        rle = RLEString("AAA")
        rle.compress()
        rle.decompress()
        try:
            rle.compress()
        except Exception:
            self.fail('Cannot compress after a successful compress-decompress')


if __name__ == '__main__':
    # Start the unit test
    unittest.main(verbosity=2)
