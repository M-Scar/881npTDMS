import unittest
import nptdms
import os
import subprocess
import time
from nptdms.tdms import TdmsReader

class TestTDMS(unittest.TestCase):    
    def testCase68004(self):
        #-68004 from https://labviewwiki.org/wiki/LabVIEW_Error_Code_Family        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Combine it with your relative path
        exe_path = os.path.join(script_dir, "helperPrograms", "advancedOpenNoClose.exe")   
        tdmsFilePath = os.path.join(script_dir, "helperPrograms", "advancedOpen.tdms")  
        print(exe_path)     
        pro = subprocess.Popen([exe_path], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
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
        pro.wait(timeout=10)
if __name__ == "__main__":
    unittest.main()        