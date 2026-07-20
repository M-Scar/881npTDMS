import unittest
import nptdms
import struct
from nptdms.reader import TdmsReader

class TestGraphTDMS(unittest.TestCase):

    parentFolder = "./test/tdms_files/"

    def testCase1(self):
        print("Path Test: [A,B,C,D,Df]")
        file = open(self.parentFolder + "1p0_big_end_Index_y_double.tdms" , "r")
        with self.assertRaises(ValueError) as error:
            nptdms.TdmsFile(file, raw_timestamps=False, read_metadata_only=False, keep_open=True)
        self.assertEqual(str(error.exception), "File should either start with 'b`TDSh`' or 'b`TDSm`', submitted starts with 'TDSm'.")
        file.close()

    def testCase2(self):
        print("Path Test: [A,B,C,D,Di,M,V,VC]")
        file = open(self.parentFolder + "1p0_big_end_Index_y_double_broken.tdms_index" , "rb")
        tdmsFile = None
        with self.assertRaises(struct.error) as error:
            tdmsFile = nptdms.TdmsFile(file, raw_timestamps=False, read_metadata_only=False, keep_open=False)
        self.assertEqual(str(error.exception), "unpack requires a buffer of 4 bytes")
        file.close()

    # def testCase3(self):
    #     # print("Path Test: [A,B,C,E,F,I,K,L,M,V,VC]") path Not possible - Identified During Testing
    #     tdmsFile = None
    #     with self.assertRaises(struct.error) as error:
    #         tdmsFile = nptdms.TdmsFile(self.parentFolder + "1p0_big_end_Index_y_double_broken.tdms_index", raw_timestamps=False, read_metadata_only=False, keep_open=False)
    #     self.assertEqual(str(error.exception), "unpack requires a buffer of 4 bytes")



if __name__ == "__main__":
    unittest.main()