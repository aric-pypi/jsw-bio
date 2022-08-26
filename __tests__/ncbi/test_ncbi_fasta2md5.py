import unittest
import jsw_bio as bio


class MyTestCase(unittest.TestCase):
    def test_something(self):
        example_fasta2str = open('./__tests__/fixtures/test.fasta', 'r').read()
        md5_code = bio.ncbi_fasta2md5(example_fasta2str)
        self.assertEqual(md5_code, 'CCD30D35DEF426190203046E3E71F214')


if __name__ == '__main__':
    unittest.main()
