import unittest
import nptdms
import struct
from nptdms.reader import TdmsReader
import os
class TestGraphTDMS(unittest.TestCase):

    parentFolder = "./tests/tdms_files/"

    #
    # Init Graph
    #

    def test_EdgeCov_01(self):
        file = open(self.parentFolder + "1p0_big_end_Index_y_double.tdms" , "r")
        with self.assertRaises(ValueError) as error:
            nptdms.TdmsFile(file, raw_timestamps=False, read_metadata_only=False, keep_open=True)
        self.assertEqual(str(error.exception), "File should either start with 'b`TDSh`' or 'b`TDSm`', submitted starts with 'TDSm'.")
        file.close()

    def test_EdgeCov_02(self):
        file = open(self.parentFolder + "1p0_big_end_Index_y_double_broken.tdms_index" , "rb")
        tdmsFile = None
        with self.assertRaises(struct.error) as error:
            tdmsFile = nptdms.TdmsFile(file, raw_timestamps=False, read_metadata_only=False, keep_open=False)
        self.assertEqual(str(error.exception), "unpack requires a buffer of 4 bytes")
        file.close()

    #
    # Graph C
    #

    def test_EdgeCovC_01(self):
        print("Testing Path Graph C: c_d_df")
        with open(self.parentFolder + "1p0_big_end_Index_y_double_broken.tdms_index") as file:
            with self.assertRaises(ValueError) as error:
                reader = TdmsReader(file)
            self.assertEqual(str(error.exception),"File should either start with 'b`TDSh`' or 'b`TDSm`', submitted starts with 'TDSh'.")

    def test_EdgeCovC_02(self):
        print("Testing Path Graph C: c_d_di")
        with open(self.parentFolder + "1p0_big_end_Index_y_double.tdms_index", "rb") as file:
            reader = TdmsReader(file)
            self.assertTrue  (reader.is_index_file_only())
            self.assertIsNone(reader._data_file_size)

    def test_EdgeCovC_03(self):
        print("Testing Path Graph C: c_d_dt")
        with open(self.parentFolder + "1p0_big_end_Index_y_double.tdms", "rb") as file:
            reader = TdmsReader(file)
            self.assertFalse (reader.is_index_file_only())
            self.assertTrue  (reader._data_file_size, 4042)

    def test_EdgeCovC_04(self):
        print("Testing Path Graph C: c_e_g_i_k")
        reader = TdmsReader(self.parentFolder + "1p0_little_end_Index_n_single.tdms")
        self.assertFalse (reader.is_index_file_only())
        self.assertTrue  (reader._data_file_size, 4096)
        self.assertIsNone(reader._index_file_path)
        self.assertTrue  (reader._file_path, self.parentFolder + "1p0_little_end_Index_n_single.tdms")
        reader.close()

    # def test_edge_c_e_g_i_j(self):
    #     """
    #     Test Path is infeasable.
    #     Cannot have an open file descriptor within TDMS that is not an index file without
    #     updating the _file_path variable. Thus testing if a tdms file or data file that calls open
    #     leads to a file path. If the file does not exist, an exception is thown.
    #     """
    #     pass
    # def test_edge_c_e_f_i_k(self):
    #     """"
    #     Test Path is infeasable.
    #     Cannot open a TDMS index file while having _file_path variable update to the path.
    #     Index files update a seperate variable, thus _file_path never becomes a non none value.
    #     """

    def test_EdgeCovC_05(self):
        print("Testing Path Graph C: c_e_g_h_i_k")
        reader = TdmsReader(self.parentFolder + "1p0_big_end_Index_y_double.tdms")
        self.assertFalse (reader.is_index_file_only())
        self.assertTrue  (reader._data_file_size, 4096)
        self.assertTrue  (reader._index_file_path, self.parentFolder + "1p0_big_end_Index_y_double.tdms_tdms")
        self.assertTrue  (reader._file_path, self.parentFolder + "1p0_little_end_Index_n_single.tdms")
        reader.close()

#
# Graph S
#
#graph edge based coverage based upon a feasible set of coverage paths for the coverage of Graph S

# [S, Sn, S, T,U,Um,V,VC]: TDMS with a named group, metadata only to be closed
# [S,Snn, S, Sn, S, T,T,Tg,T,U,Ud,UdAI,UdAI, UdRd,UdRd,UdRG,UdRG,V,VO]:  TDMS with an unnamed group and a named group to
#  be read both data and metadata and kept open
# [S,Snn,S,T,U,Um,V,VC]: TDMS with an unnamed group metadata only to be closed

    def test_EdgeCovS_01(self):
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


    def test_EdgeCovS_02(self):
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

    def test_EdgeCovS_03(self):
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


    #
    # Graph Test: Read
    #

    def test_Node_01(self):
        print("Testing Path: a_b_c_d_m_q_r_t")
        file = nptdms.TdmsFile(self.parentFolder + "tdsmByteOnly.tdms")
        self.assertTrue   (file.data_read)
        self.assertTrue   (len(file._channel_data) == 0)
        self.assertTrue   (len(file._properties) == 0)
        self.assertIsNone (file.tdms_version)

    def test_Node_02(self):
        print("Testing Path: a_b_d_m_q_q_s_q_r_t")
        file = nptdms.TdmsFile(self.parentFolder + "tdmsNoGroupNoDataNoChannel.tdms")
        self.assertTrue   (file.data_read)
        self.assertTrue   (len(file._channel_data) == 0)
        self.assertTrue   (len(file._properties) == 1)
        self.assertTrue   (file.tdms_version == 4713)

    def test_Node_main_path(self):
        print("Testing Path: Main Path Nodes")
        file = nptdms.TdmsFile(self.parentFolder + "2p0_big_end_Index_n_double.tdms")
        self.assertTrue   (len(file.groups()) == 3)
        self.assertTrue   (len(file.groups()[0]) == 1)
        self.assertTrue   (file.tdms_version == 4713)
        self.assertTrue   (len(file._properties) == 1)

if __name__ == "__main__":
    unittest.main()