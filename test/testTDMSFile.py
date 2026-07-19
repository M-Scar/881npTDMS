import unittest
import nptdms
from nptdms.tdms import TdmsReader

class TestTDMS(unittest.TestCase):

    parentFolder = "./test/tdms_files/"

    def testCase1(self):
        print("TESTCASE1: Testing: 1.0 - Big Endian - Index File: Yes - Type: Double - Read Metadata Only: False - TimeStamps: False - Memory Mapped Dir: False - Read Path - Keep Open: True")

        tdmsFileName = "1p0_big_end_Index_y_double.tdms"
        tdmsFilePath = self.parentFolder + tdmsFileName
        with self.assertRaises(FileNotFoundError):
            tdmsfile = nptdms.TdmsFile(tdmsFilePath, raw_timestamps=False, memmap_dir="not a path", read_metadata_only=False, keep_open=True)

    def testCase2(self):
        print("TESTCASE2: Testing: 1.0 - Little Endian - Index File: No - Type: Single - Read Metadata Only: True - TimeStamps: True - Memory Mapped Dir: Empty - rb File - Keep Open: False")
        tdmsFileName = "1p0_little_end_Index_n_single.tdms"
        tdmsFilePath = self.parentFolder + tdmsFileName

        file = open(tdmsFilePath, "rb")
        tdmsFile = nptdms.TdmsFile(file, raw_timestamps=True, read_metadata_only=True, keep_open=False)
        self.assertEqual(tdmsFile.tdms_version, 4712)
        self.assertTrue(tdmsFile._raw_timestamps)
        self.assertIsInstance(tdmsFile, nptdms.TdmsFile)
        self.assertIsNone(tdmsFile._reader._index_file_path)
        self.assertEqual(tdmsFile.data_read, False)
        self.assertIsNone(tdmsFile._memmap_dir)
        tdmsFile.close()
        file.close()

    def testCase3(self):
        print("TESTCASE3: Testing: 2.0 - Big Endian - Index File: Yes - Type: Single - Read Metadata Only: True - TimeStamps: True - Memory Mapped Dir: String - Read Path - Keep Open: False")
        tdmsFileName = "2p0_big_end_Index_y_single.tdms"
        tdmsFilePath = self.parentFolder + tdmsFileName

        tdmsFile = nptdms.TdmsFile(tdmsFilePath, raw_timestamps=True, read_metadata_only=True, keep_open=False, memmap_dir="./tmp/")
        self.assertEqual(tdmsFile.tdms_version, 4713)
        self.assertTrue(tdmsFile._raw_timestamps)
        self.assertIsInstance(tdmsFile, nptdms.TdmsFile)
        self.assertEqual(tdmsFile.data_read, False)
        self.assertEqual(tdmsFile._reader._index_file_path, tdmsFilePath + "_index")
        self.assertEqual(tdmsFile._memmap_dir, "./tmp/")
        tdmsFile.close()

    def testCase4(self):
        print("TESTCASE4: Testing: 2.0 - Little Endian - Index File: No - Type: Double - Read Metadata Only: True - TimeStamps: False - Memory Mapped Dir: non valid string - rb File - Keep Open: true")
        tdmsFileName = "2p0_little_end_Index_n_double.tdms"
        tdmsFilePath = self.parentFolder + tdmsFileName

        file = open(tdmsFilePath, "rb")
        tdmsFile = nptdms.TdmsFile(file, raw_timestamps=False, memmap_dir="A Bad Path", read_metadata_only=True, keep_open=True)
        self.assertEqual(tdmsFile.tdms_version, 4713)
        self.assertFalse(tdmsFile._raw_timestamps)
        self.assertEqual(tdmsFile.data_read, False)
        self.assertIsNone(tdmsFile._reader._index_file_path)
        self.assertIsNotNone(tdmsFile._reader._file)
        self.assertEqual(tdmsFile._memmap_dir, "A Bad Path")
        tdmsFile.close()

    def testCase5(self):
        print("TESTCASE5: Testing: 2.0 - Big Endian - Index File: Yes - Type: Single - Read Metadata Only: false - TimeStamps: False - Memory Mapped Dir: Empty - rb File - Keep Open: False")

        tdmsFileName = "2p0_big_end_Index_y_single.tdms"
        tdmsFilePath = self.parentFolder + tdmsFileName

        file = open(tdmsFilePath, "rb")
        tdmsFile = nptdms.TdmsFile(file, raw_timestamps=False, read_metadata_only=False, keep_open=False)
        self.assertEqual(tdmsFile.tdms_version, 4713)
        self.assertFalse(tdmsFile._raw_timestamps)
        self.assertEqual(tdmsFile.data_read, True)
        self.assertIsNone(tdmsFile._memmap_dir)
        self.assertIsNone(tdmsFile._reader._file)
        self.assertIsNone(tdmsFile._reader._index_file_path)
        tdmsFile.close()
        file.close()

    def testCase6(self):
        print("TESTCASE6: Testing: 1.0 - Little Endian - Index File: No - Type: Double - Read Metadata Only: false - TimeStamps: True - Memory Mapped Dir: String - Read Path - Keep Open: true")

        tdmsFileName = "1p0_little_end_Index_n_double.tdms"
        tdmsFilePath = self.parentFolder + tdmsFileName

        tdmsFile = nptdms.TdmsFile(tdmsFilePath, raw_timestamps=True, read_metadata_only=False, keep_open=True, memmap_dir="./tmp/")
        self.assertEqual(tdmsFile.tdms_version, 4712)
        self.assertTrue(tdmsFile._raw_timestamps)
        self.assertEqual(tdmsFile.data_read, True)
        self.assertEqual(tdmsFile._memmap_dir, "./tmp/")
        self.assertIsNotNone(tdmsFile._reader._file)
        self.assertIsNone(tdmsFile._reader._index_file_path)
        tdmsFile.close()
    def testCase7(self):
        print("TESTCASE7: Testing: 2.0 - Big Endian - Index File: No - Type: Double - Read Metadata Only: false - TimeStamps: false - Memory Mapped Dir: Empty - Read Path - Keep Open: true")

        tdmsFileName = "2p0_big_end_Index_n_double.tdms"
        tdmsFilePath = self.parentFolder + tdmsFileName

        tdmsFile = nptdms.TdmsFile(tdmsFilePath, raw_timestamps=False, read_metadata_only=False, keep_open=True)
        self.assertEqual(tdmsFile.tdms_version, 4713)
        self.assertFalse(tdmsFile._raw_timestamps)
        self.assertEqual(tdmsFile.data_read, True)
        self.assertIsNone(tdmsFile._memmap_dir)
        self.assertIsNotNone(tdmsFile._reader._file)
        self.assertIsNone(tdmsFile._reader._index_file_path)
        tdmsFile.close()

    def testCase8(self):
        print("TESTCASE8: Testing: 1.0 - Little Endian - Index File: Yes - Type: Double - Read Metadata Only: false - TimeStamps: True - Memory Mapped Dir: non valid string - rb File - Keep Open: False")
        tdmsFileName = "1p0_little_end_Index_y_double.tdms"
        tdmsFilePath = self.parentFolder + tdmsFileName

        file = open(tdmsFilePath, "rb")
        with self.assertRaises(FileNotFoundError):
            tdmsFile = nptdms.TdmsFile(file, raw_timestamps=True, read_metadata_only=False, keep_open=False, memmap_dir="Wherever I May Roam")
            # self.assertTrue(tdmsFile._raw_timestamps)
            # self.assertEqual(tdmsFile.data_read, True)
            # self.assertEqual(tdmsFile._memmap_dir,"Wherever I May Roam")
            # self.assertIsNone(tdmsFile._reader._index_file)
            # self.assertIsNone(tdmsFile._reader._file)
            # self.assertEqual(tdmsFile._reader._index_file_path, tdmsFilePath)
            # self.assertEqual(tdmsFile._reader._index_file_path, tdmsFilePath + "_index")
        file.close()

    def testCase9(self):
        print("TESTCASE9: Testing: 2.0 - Big Endian - Index File: Yes - Type: Single - Read Metadata Only: false - TimeStamps: True - Memory Mapped Dir: non valid string - rb File - Keep Open: True")
        tdmsFileName = "2p0_big_end_Index_y_single.tdms"
        tdmsFilePath = self.parentFolder + tdmsFileName
        file = open(tdmsFilePath, "rb")
        with self.assertRaises(FileNotFoundError):
            tdmsFile = nptdms.TdmsFile(file, raw_timestamps=False, memmap_dir="A Bad Path", read_metadata_only=False, keep_open=True)
            # self.assertTrue(tdmsFile._raw_timestamps)
            # self.assertNotEqual(tdmsFile.data_read, False)
            # self.assertEqual(tdmsFile._memmap_dir, "A Bad Path")
            # self.assertIsNotNone(tdmsFile._reader._file)
            # self.assertIsEqual(tdmsFile._reader._index_file_path, tdmsFilePath+"_index")
            tdmsFile.close()
        file.close()
        print("")
    def testCase10(self):
        print("TESTCASE10: Testing: 1.0 - Little Endian - Index File: Yes - Type: Single - Read Metadata Only: True - TimeStamps: False - Memory Mapped Dir: String - rb File - Keep Open: True")
        tdmsFileName = "1p0_little_end_Index_y_single.tdms"
        tdmsFilePath = self.parentFolder + tdmsFileName

        file = open(tdmsFilePath, "rb")
        tdmsFile = nptdms.TdmsFile(file, raw_timestamps=False, read_metadata_only=True, keep_open=True, memmap_dir="./tmp/")
        self.assertEqual(tdmsFile.tdms_version, 4712)
        self.assertFalse(tdmsFile._raw_timestamps)
        self.assertEqual(tdmsFile.data_read, False)
        self.assertEqual(tdmsFile._memmap_dir, "./tmp/")
        self.assertIsNotNone(tdmsFile._reader._file)
        self.assertIsNone(tdmsFile._reader._index_file_path)
        tdmsFile.close()
        file.close()
        print("")

if __name__ == "__main__":
    unittest.main()