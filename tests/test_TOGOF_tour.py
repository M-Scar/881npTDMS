import unittest
from nptdms import TdmsFile, TdmsWriter
from multiprocessing import Process, Queue
from tests.TdmsBuilder import TdmsBuilder
import os
import numpy as np

def multiRead(filePath, queue):
    try:
        tdmsFile = TdmsFile(filePath)
        data = tdmsFile["Customers"]["Index"][:]
        queue.put(("pass",data))
    except Exception as e:
        queue.put(("fail",str(e)))

def multiMemMap(filePath, queue):
    try:
        tdmsFile = TdmsFile(filePath, memmap_dir="./tmp",keep_open=True)
        data = tdmsFile["Customers"]["Index"][:]
        queue.put(("pass", data))
    except Exception as e:
        queue.put(("fail",str(e)))

def multiWrite(filePath, queue):
    passFail = False
    try:
        builder = TdmsBuilder()
        builder.addChannel(group="Group1", channel="C1", data=[1,2,3,4,5])
        with TdmsWriter(filePath) as writer:
            writer.write_segment(builder.getChannels())
        passFail = True
    except Exception as e:
        pass
    queue.put(passFail)

def multiWriteAppend(filePath, paramList, queue):
    passFail = False
    try:
        builder = TdmsBuilder()
        builder.addChannel(group=paramList[0], channel=paramList[1], data=[1,2,3,4,5])
        with TdmsWriter(filePath, "a") as writer:
            writer.write_segment(builder.getChannels())
        passFail = True
    except Exception as e:
        pass
    queue.put(passFail)

class TestTdmsTOGOF(unittest.TestCase):

    parentDir = "./tests/tdms_files/"

    def test_Togof_01(self):
        filePath = self.parentDir + "customers.tdms"
        processCount = 3
        processArr = []
        queue = Queue()

        for _ in range(processCount):
            p = Process(target=multiRead, args=(filePath, queue))
            processArr.append(p)
        for p in processArr:
            p.start()
        returns = [queue.get() for _ in range(processCount)]

        for p in processArr:
            p.join()

        passFail = True
        for key, data in returns:
            if key == "fail":
                passFail = False
            else:
                for i in range(len(data)):
                    data[i] = i+1

        assert passFail == True

    def test_Togof_02(self):
        filePath = self.parentDir + "customers.tdms"
        processCount = 3
        processArr = []
        queue = Queue()

        for _ in range(processCount):
            p = Process(target=multiMemMap, args=(filePath, queue))
            processArr.append(p)
        for p in processArr:
            p.start()
        returns = [queue.get() for _ in range(processCount)]

        for p in processArr:
            p.join()

        tdmsFile = TdmsFile(filePath)
        check = tdmsFile["Customers"]["Index"][:]

        passFail = True
        for key, _ in returns:
            if key == "fail":
                passFail = False
        self.assertTrue(passFail)
        for result in returns:
            self.assertTrue (result[1].all() == check.all())

    def test_Togof_03(self):
        os.makedirs("./tmp", exist_ok=True)
        processCount = 3
        processArr = []
        queue = Queue()

        for _ in range(processCount):
            p = Process(target=multiWrite, args=("./tmp/mutliWrite.tdms", queue))
            processArr.append(p)
        for p in processArr:
            p.start()
        returns = [queue.get() for _ in range(processCount)]
        if False in returns:
            self.assertTrue(False)
        for p in processArr:
            p.join()
        inFile = TdmsFile("./tmp/mutliWrite.tdms")
        self.assertTrue(len(inFile["Group1"]["C1"][:]) == 5)
        self.assertTrue(np.array_equal(inFile["Group1"]["C1"][:], np.array([1,2,3,4,5])))

        if os.path.exists("./tmp/mutliWrite.tdms"):
            os.remove("./tmp/mutliWrite.tdms")
            self.assertFalse(os.path.exists("./tmp/mutliWrite.tdms"))

    def test_Togof_04(self):
        os.makedirs("./tmp", exist_ok=True)
        processCount = 3
        processArr = []
        queue = Queue()

        for i in range(processCount):
            p = Process(target=multiWriteAppend, args=("./tmp/mutliWriteAppend.tdms", ["Group" + str(i), "C" + str(i)], queue))
            processArr.append(p)
        for p in processArr:
            p.start()
        returns = [queue.get() for _ in range(processCount)]
        if False in returns:
            self.assertTrue(False)
        for p in processArr:
            p.join()

        inFile = TdmsFile("./tmp/mutliWriteAppend.tdms")
        self.assertTrue(len(inFile["Group0"]["C0"][:]) == 5)
        self.assertTrue(len(inFile["Group1"]["C1"][:]) == 5)
        self.assertTrue(len(inFile["Group2"]["C2"][:]) == 5)
        self.assertTrue(np.array_equal(inFile["Group0"]["C0"][:], np.array([1,2,3,4,5])))
        self.assertTrue(np.array_equal(inFile["Group1"]["C1"][:], np.array([1,2,3,4,5])))
        self.assertTrue(np.array_equal(inFile["Group2"]["C2"][:], np.array([1,2,3,4,5])))
        if os.path.exists("./tmp/mutliWriteAppend.tdms"):
            os.remove("./tmp/mutliWriteAppend.tdms")
            self.assertFalse(os.path.exists("./tmp/mutliWriteAppend.tdms"))

if __name__ == "__main__":
    unittest.main()