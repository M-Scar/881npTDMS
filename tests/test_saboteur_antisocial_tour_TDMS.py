import unittest
import nptdms
import os
import subprocess
import time
import logging
from nptdms.tdms import TdmsReader

#https://www.ni.com/docs/en-US/bundle/labview-api-ref/page/errors/storage-dataplugin-and-tdm-streaming-error-codes.html?srsltid=AfmBOooR9aEDq0p1blO_pn5yGJqrzJ8EXQMjxBmevfM5hC3AZbtWRbsd
#2 hour saboteur and antisocial tour
class TestTDMS(unittest.TestCase):
    def init_LabVIEWRuntime(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        exe_path = os.path.join(script_dir, "helperPrograms", "advancedOpenNoClose.exe")
        tdmsFilePath = os.path.join(script_dir, "helperPrograms", "advancedOpen.tdms")
        print(exe_path)
        pro = subprocess.Popen([exe_path], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        pro.wait(timeout=15)

    def test_Case68004(self):
        #-68004 from https://labviewwiki.org/wiki/LabVIEW_Error_Code_Family
        script_dir = os.path.dirname(os.path.abspath(__file__))
        exe_path = os.path.join(script_dir, "helperPrograms", "advancedOpenNoClose.exe")
        tdmsFilePath = os.path.join(script_dir, "helperPrograms", "advancedOpen.tdms")
        print(exe_path)
        # pro = subprocess.Popen([exe_path], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
        #                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5) #possible to get a signal from labview that the file is indeed open?
        print("starting a read attempt")
        tdmsfile = nptdms.TdmsFile(tdmsFilePath, read_metadata_only=False, keep_open=False)
        print("finished a read attempt")
        for name, value in tdmsfile.properties.items():
                print("{0}: {1}".format(name, value))
        for group in tdmsfile.groups():
                for channel in group.channels():
                    key = f"{group.name}/{channel.name}"
                    for name, value in channel.properties.items():
                        print(f"Channel '{key}': {name} = {value}")
        #pro.wait(timeout=10)
    def test_Case68007(self):
        #value error for extended precision. this test does not map specifically to LabVIEW but is epxlicitly
        #mentioned as an invalid case in the github README
        script_dir = os.path.dirname(os.path.abspath(__file__))
        tdmsFilePath = os.path.join(script_dir, r"tdms_files\\specialCases\\" r"\\extendedTDMS.tdms")
        with self.assertRaises(ValueError):
            tdmsfile = nptdms.TdmsFile(tdmsFilePath, read_metadata_only=False, keep_open=False)
    def test_Case68013(self):
        print("")
        #-68004 from https://labviewwiki.org/wiki/LabVIEW_Error_Code_Family
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Combine it with your relative path
        exe_path = os.path.join(script_dir, "helperPrograms", "liveTDMSStream.exe")
        tdmsFilePath = os.path.join(script_dir, "helperPrograms", "liveDAQMXRun.tdms")
        print(exe_path)
        pro = subprocess.Popen([exe_path], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5) #possible to get a signal from labview that the file is indeed open?
        print("starting a stream")
        tdmsfile = nptdms.TdmsFile(tdmsFilePath, read_metadata_only=False, keep_open=False)
        print("finished a read attempt")
        for name, value in tdmsfile.properties.items():
                print("{0}: {1}".format(name, value))
        for group in tdmsfile.groups():
                for channel in group.channels():
                    key = f"{group.name}/{channel.name}"
                    for name, value in channel.properties.items():
                        print(f"Channel '{key}': {name} = {value}")
        #pro.wait(timeout=5)
        pro.kill()
    def test_Case68010(self):
        #not one to one, but a similar approach to the error of 68010
        script_dir = os.path.dirname(os.path.abspath(__file__))
        tdmsFilePath = os.path.join(script_dir, "tdms_files", "1p0_big_end_Index_y_double.tdms")
        tdmsfile = nptdms.TdmsFile(tdmsFilePath, read_metadata_only=False, keep_open=True)
        tdmsfile = nptdms.TdmsFile(tdmsFilePath, read_metadata_only=False, keep_open=True)
        print(tdmsfile.groups()[0].channels()[0][:])
    def test_Case2503(self):
        #tdms try passing in pictures
        script_dir = os.path.dirname(os.path.abspath(__file__))
        tdmsFilePath = os.path.join(script_dir, "tdms_files/specialCases", "APeppersPNGSavedAsTDMS.tdms")
        with self.assertRaises(ValueError):
            tdmsfile = nptdms.TdmsFile(tdmsFilePath, read_metadata_only=False, keep_open=False)
        #b'Tdsm' expected
        tdmsFilePath = os.path.join(script_dir, "tdms_files/specialCases", "peppers.png")
        with self.assertRaises(ValueError):
            tdmsfile = nptdms.TdmsFile(tdmsFilePath, read_metadata_only=False, keep_open=False)
        #the same check
        tdmsFilePath = os.path.join(script_dir, "tdms_files/specialCases", "peppersTricky.tdms")
        with self.assertLogs("nptdms.reader", level=logging.WARNING) as logs:
            tdmsfile = nptdms.TdmsFile(tdmsFilePath, read_metadata_only=False, keep_open=False)
            self.assertTrue(any("Unrecognised version number" in msg for msg in logs.output))
            #while the first byte matches, the tdms could still be in this invalid state and be "recoverable"
            # [nptdms.reader WARNING] Unrecognised version number: 16795209
            # [nptdms.reader WARNING] Last segment metadata is incomplete
            #edge case but arguable


if __name__ == "__main__":
    unittest.main()