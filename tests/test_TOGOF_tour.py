import unittest
from nptdms import TdmsFile
from multiprocessing import Process, Queue

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

class TestTdmsTOGOF(unittest.TestCase):

    parentDir = "./tests/tdms_files/"

    def test_parallel_read(self):
        filePath = self.parentDir + "customers.tdms"
        processCount = 10
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

    def test_parallel_memmap(self):
        filePath = self.parentDir + "customers.tdms"
        processCount = 10
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

if __name__ == "__main__":
    unittest.main()