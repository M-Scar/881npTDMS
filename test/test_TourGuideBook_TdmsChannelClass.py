import unittest
import numpy
import pandas
from nptdms import TdmsFile, TdmsChannel


class TestGuidBookTourTdmsChannel(unittest.TestCase):
    parentFolder = "./test/tdms_files/"

    """Set Up to create tdms file to access a real and controlled TdmsChannel"""
    def setUp(self):
        with open(self.parentFolder + "customers.tdms", "rb") as file:
            self.tdmsFile = TdmsFile(file)
            self.channels = self.tdmsFile["Customers"].channels()
            self.testChannel : TdmsChannel = self.channels[0]
            assert (len(self.channels) == 12) # Cols of Customer file

    """Tear Down Method to free tdmsFile and channels object after each test"""
    def tearDown(self):
        del self.tdmsFile
        del self.channels

    """Tests that each channel contains the data provided via input file"""
    def test_Channel_Data_Array(self):
        for chan in self.channels:
            assert len(chan) == 1000
        assert isinstance(self.channels[0][:], numpy.ndarray)

    """Test provided subset function outlined in the documentation"""
    def test_Channel_Data_Subset_Data(self):
        subset = self.channels[0][500:1000]
        for i in range (len(subset)):
            assert int(subset[i]) == i+501
        assert len(subset) == 500

    """Test Given Properites of the Tdms Channel Object"""
    def test_Channel_properties(self):
        assert self.testChannel.path == "/'Customers'/'Index'"
        assert self.testChannel.name == "Index"
        assert self.testChannel.group_name == "Customers"
        assert isinstance(self.testChannel.dtype, numpy.dtype)

    """Tests the non-recommended use of .data propery is equivalent to the index slice"""
    def test_Channel_data_property(self):
        for chan in self.channels:
            assert chan.data.all() == chan[:].all()

    """Tests the raw data attribute, input test does not contain scaled data"""
    def test_Raw_data(self):
        assert self.testChannel.raw_data.all() == self.testChannel.data.all()
        assert not self.testChannel.raw_scaler_data

    """Tests the re-read function of channel class. Uses Offset to get specific sections of data"""
    def test_read_data(self):
        data = self.testChannel.read_data(20,10,False)
        for i in range(10):
            assert int(data[i]) == i+21

    """Checks that channel not containing time properites throws KeyError as defined in Documentation"""
    def test_time_track_no_time(self):
        with self.assertRaises(KeyError):
            self.testChannel.time_track()

    """Test Given Channel with time properites is created with correct type and length matches the controlled length of data"""
    def test_time_track(self):
        timeFile = TdmsFile(self.parentFolder + "1p0_big_end_Index_y_double.tdms",True)["Group0"]["Untitled"].time_track()
        assert len(timeFile) == 99
        assert isinstance(timeFile, numpy.ndarray)

    """Tests as DataFrame function. Asserts returned object is dataframe and data length matches sample input file"""
    def test_to_dataframe(self):
        dataFrame = self.testChannel.as_dataframe()
        assert isinstance(dataFrame, pandas.DataFrame)
        assert len(dataFrame) == 1000

if __name__ == "__main__":
    unittest.main()