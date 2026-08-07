import unittest
import nptdms
import struct
from nptdms.reader import TdmsReader
import os
#graph edge based coverage based upon a feasible set of coverage paths for the coverage of Graph S

# [S, Sn, S, T,U,Um,V,VC]: TDMS with a named group, metadata only to be closed
# [S,Snn, S, Sn, S, T,T,Tg,T,U,Ud,UdAI,UdAI, UdRd,UdRd,UdRG,UdRG,V,VO]:  TDMS with an unnamed group and a named group to
#    be read both data and metadata and kept open 
# [S,Snn,S,T,U,Um,V,VC]: TDMS with an unnamed group metadata only to be closed


class TestGraphTDMS(unittest.TestCase):

    parentFolder = "./tests/tdms_files/"

    def testEdgeCov1(self):
        print("Path test [S, Sn, S, T,U,Um,V,VC]:")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        tdmsFilePath = os.path.join(script_dir, "tdms_files", "TDMSNamedGroup.tdms")
        tdmsFile = nptdms.TdmsFile(tdmsFilePath, read_metadata_only=True, keep_open=False)
        self.assertEqual(tdmsFile.tdms_version, 4713)
        self.assertFalse(tdmsFile._raw_timestamps)
        self.assertIsInstance(tdmsFile, nptdms.TdmsFile)
        self.assertIsNotNone(tdmsFile._reader._index_file_path)
        self.assertEqual(tdmsFile.data_read, False)
        self.assertIsNone(tdmsFile._memmap_dir)
        tdmsFile.close()
        tdmsFile.close()


    def testEdgeCov2(self):
        print("[S,Snn, S, Sn, S, T,T,Tg,T,U,Ud,UdAI,UdAI, UdRd,UdRd,UdRG,UdRG,V,VO]")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        tdmsFilePath = os.path.join(script_dir, "tdms_files", "TDMS_Snn_Sn_Groups.tdms")
        tdmsFile = nptdms.TdmsFile(tdmsFilePath, read_metadata_only=False, keep_open=True)
        self.assertEqual(tdmsFile.tdms_version, 4713)
        self.assertFalse(tdmsFile._raw_timestamps)
        self.assertIsInstance(tdmsFile, nptdms.TdmsFile)
        self.assertIsNotNone(tdmsFile._reader._index_file_path)
        self.assertEqual(tdmsFile.data_read, True)
        self.assertIsNone(tdmsFile._memmap_dir)
        tdmsFile.close()
        tdmsFile.close()
    def testEdgeCov3(self):
        print("[S,Snn,S,T,U,Um,V,VC]")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        tdmsFilePath = os.path.join(script_dir, "tdms_files", "TDMSUnnamedGroup.tdms")
        tdmsFile = nptdms.TdmsFile(tdmsFilePath, read_metadata_only=False, keep_open=True)
        self.assertEqual(tdmsFile.tdms_version, 4713)
        self.assertFalse(tdmsFile._raw_timestamps)
        self.assertIsInstance(tdmsFile, nptdms.TdmsFile)
        self.assertIsNotNone(tdmsFile._reader._index_file_path)
        self.assertEqual(tdmsFile.data_read, True)
        self.assertIsNone(tdmsFile._memmap_dir)
        tdmsFile.close()
        tdmsFile.close()        

    # def testCase3(self):
    #     # print("Path Test: [A,B,C,E,F,I,K,L,M,V,VC]") path Not possible - Identified During Testing
    #     tdmsFile = None
    #     with self.assertRaises(struct.error) as error:
    #         tdmsFile = nptdms.TdmsFile(self.parentFolder + "1p0_big_end_Index_y_double_broken.tdms_index", raw_timestamps=False, read_metadata_only=False, keep_open=False)
    #     self.assertEqual(str(error.exception), "unpack requires a buffer of 4 bytes")



if __name__ == "__main__":
    unittest.main()