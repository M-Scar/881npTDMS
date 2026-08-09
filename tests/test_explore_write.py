import unittest
from numpy import array
from nptdms import ChannelObject
from nptdms.writer import *
import os
import shutil
from TdmsBuilder import TdmsBuilder

class TestExploreWrite(unittest.TestCase):

    outdir = "./writtenTdms/"

    def setUp(self):
        os.makedirs(self.outdir, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.outdir)

    def test_Exp_01(self):
        builder = TdmsBuilder()
        builder.addChannel(group="G1", channel="C1", data=[1,2,3,4,5,6,100,99,98,97,58])
        builder.addChannel(group="G1", channel="Bands", data=["Sleep", "Electric Wizzard", "Supersonic Dragon Wagon"])
        builder.addChannel(group="G2", channel="Temps", data=[72.8,42.8,3.50])
        builder.addChannel(group="G3", channel="Temps", data=["72.8","42.8","3.50"])
        builder.addChannel(group="G4", channel="Random", data=[])
        builder.addChannel(group="G4", channel="Empty", data=[""])

        with TdmsWriter(self.outdir + "Test1.tdms") as writer:
            writer.write_segment(builder.getChannels())

        fileIn = TdmsFile(self.outdir + "Test1.tdms")
        returnVal = builder.compare(fileIn)
        self.assertTrue (returnVal)

    def test_Exp_02(self):
        shutil.copy("./tests/tdms_files/1p0_little_end_Index_y_double.tdms", self.outdir + "1p0_little_end_Index_y_double.tdms")
        self.assertTrue (os.path.isfile(self.outdir + "1p0_little_end_Index_y_double.tdms"))
        tdmsFile = TdmsFile(self.outdir + "1p0_little_end_Index_y_double.tdms")

        with TdmsWriter(self.outdir + "1p0_little_end_Index_y_double.tdms", "a") as writer:
            writer.write_segment([ChannelObject(group="Group3", channel="Untitled", data=array(["Test Channel Data"], dtype=str))])
            writer.write_segment([ChannelObject(group="Group2", channel="Untitled2", data=array(["Test Channel Data"], dtype=str))])

        tdmsFile = TdmsFile(self.outdir + "1p0_little_end_Index_y_double.tdms")
        self.assertTrue(tdmsFile["Group3"]["Untitled"][0] == "Test Channel Data")
        self.assertTrue(tdmsFile["Group2"]["Untitled2"][0] == "Test Channel Data")

    def test_Exp_03(self):
        builder = TdmsBuilder()
        builder.addChannel(group="G1", channel="C1", data=[10,9,8,7,6,5,4,3,2,1])
        with TdmsWriter(self.outdir + "Test3.tdms") as writer:
            writer.write_segment(builder.getChannels())

        builder.addChannel(group="G1", channel="C1", data=[1,2,3,4,5,6,7,8,9,10])
        with TdmsWriter(self.outdir + "Test3.tdms", "a") as writer:
                    writer.write_segment(builder.getChannels())

        fileIn = TdmsFile(self.outdir + "Test3.tdms")

        returnVal = builder.compare(fileIn) #Appends to the actual channel data
        self.assertFalse(returnVal)
        self.assertTrue (len(fileIn["G1"]["C1"][:]) == 20)

if __name__ == "__main__":
    unittest.main()