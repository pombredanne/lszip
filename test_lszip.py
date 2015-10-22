import unittest
import lszip

class HelpersTest(unittest.TestCase):
    def test_generate_range_header(self):
        header_range = lszip.generate_range_header()
        self.assertEqual(header_range, {'Range': 'bytes=0-'})

        header_range = lszip.generate_range_header(20, 40)
        self.assertEqual(header_range, {'Range': 'bytes=20-40'})

        header_range = lszip.generate_range_header(12)
        self.assertEqual(header_range, {'Range': 'bytes=12-'})

        header_range = lszip.generate_range_header(-20)
        self.assertEqual(header_range, {'Range': 'bytes=-20'})
    def test_index_in_sub_array(self):
        arr = [2, 3, 44, 55, 666]
        b = arr[2:]
        self.assertTrue(lszip.index_in_sub_array(2, len(b), len(arr)))
        self.assertTrue(lszip.index_in_sub_array(4, len(b), len(arr)))
        self.assertFalse(lszip.index_in_sub_array(1, len(b), len(arr)))
        self.assertFalse(lszip.index_in_sub_array(0, len(b), len(arr)))
class ZipTest(unittest.TestCase):
    def setUp(self):
        # test_file.zip contains 1 text file with no archive comment
        # test_file_comment.zip contains 1 text file with archive comment
        # Archive comment
        self.archive_comment = 'Hello THere\r\nI am fine.'
        self.bytes = open('test_file.zip').read()
        self.bytes_with_comment = open('test_file_comment.zip', 'rb').read()
    def test_zip_get_ecd(self):
        ecd = lszip.zip_get_ecd(self.bytes_with_comment)
        self.assertIsNotNone(ecd)
        
        ecd = lszip.zip_get_ecd(self.bytes)
        self.assertIsNotNone(ecd)

        # Test ecd's no of files
        self.assertEqual(ecd[lszip._ECD_ENTRIES_TOTAL], 1)


if __name__ == '__main__':
    unittest.main()
