import unittest
import nptdms
import struct
from nptdms.reader import TdmsReader

class TestGraphTDMS(unittest.TestCase):

    parentFolder = "./tests/tdms_files/"

    def testCase1(self):
        file = open(self.parentFolder + "1p0_big_end_Index_y_double.tdms" , "r")
        with self.assertRaises(ValueError) as error:
            nptdms.TdmsFile(file, raw_timestamps=False, read_metadata_only=False, keep_open=True)
        self.assertEqual(str(error.exception), "File should either start with 'b`TDSh`' or 'b`TDSm`', submitted starts with 'TDSm'.")
        file.close()

    def testCase2(self):
        file = open(self.parentFolder + "1p0_big_end_Index_y_double_broken.tdms_index" , "rb")
        tdmsFile = None
        with self.assertRaises(struct.error) as error:
            tdmsFile = nptdms.TdmsFile(file, raw_timestamps=False, read_metadata_only=False, keep_open=False)
        self.assertEqual(str(error.exception), "unpack requires a buffer of 4 bytes")
        file.close()

    def test_edge_c_d_df(self):
        with open(self.parentFolder + "1p0_big_end_Index_y_double_broken.tdms_index") as file:
            with self.assertRaises(ValueError) as error:
                reader = TdmsReader(file)
            self.assertEqual(str(error.exception),"File should either start with 'b`TDSh`' or 'b`TDSm`', submitted starts with 'TDSh'.")

    def test_edge_c_d_di(self):
        with open(self.parentFolder + "1p0_big_end_Index_y_double.tdms_index", "rb") as file:
            reader = TdmsReader(file)
            self.assertTrue  (reader.is_index_file_only())
            self.assertIsNone(reader._data_file_size)

    def test_edge_c_d_dt(self):
        with open(self.parentFolder + "1p0_big_end_Index_y_double.tdms", "rb") as file:
            reader = TdmsReader(file)
            self.assertFalse (reader.is_index_file_only())
            self.assertTrue  (reader._data_file_size, 4042)

    def test_edge_c_e_g_i_k(self):
        reader = TdmsReader(self.parentFolder + "1p0_little_end_Index_n_single.tdms")
        self.assertFalse (reader.is_index_file_only())
        self.assertTrue  (reader._data_file_size, 4096)
        self.assertIsNone(reader._index_file_path)
        self.assertTrue  (reader._file_path, self.parentFolder + "1p0_little_end_Index_n_single.tdms")
        reader.close()

    def test_edge_c_e_g_i_j(self):
        """
        Test Path is infeasable.
        Cannot have an open file descriptor within TDMS that is not an index file without
        updating the _file_path variable. Thus testing if a tdms file or data file that calls open
        leads to a file path. If the file does not exist, an exception is thown.
        """
        pass
    def test_edge_c_e_f_i_k(self):
        """"
        Test Path is infeasable.
        Cannot open a TDMS index file while having _file_path variable update to the path.
        Index files update a seperate variable, thus _file_path never becomes a non none value.
        """

    def test_edge_c_e_g_h_i_k(self):
        reader = TdmsReader(self.parentFolder + "1p0_big_end_Index_y_double.tdms")
        self.assertFalse (reader.is_index_file_only())
        self.assertTrue  (reader._data_file_size, 4096)
        self.assertTrue  (reader._index_file_path, self.parentFolder + "1p0_big_end_Index_y_double.tdms_tdms")
        self.assertTrue  (reader._file_path, self.parentFolder + "1p0_little_end_Index_n_single.tdms")
        reader.close()

if __name__ == "__main__":
    unittest.main()