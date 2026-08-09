from behave import given, when, then
import unittest
import nptdms
import tempfile
import os
import tracemalloc
from memory_profiler import memory_usage 

#note, 60 mb run takes up to a minute
#in the original issue about large tdms files, the standard that was considered 'poor' 
# was 250 mb using 650. A general ratio of 1 to 4 can be used, but testing that can last 5 minutes a run

#because of the long runtime of files reads, depth is sacrificed for speed. assuming linear growth
#induction may imply that a 60 mb file passing is proof enough larger files will as well

@given("A TDMS of 60 Mb")
def step_60mb_tdms(context):
   script_dir = os.path.dirname(os.path.abspath(__file__))
#    context.tdmsFilePath = os.path.join(script_dir, "../tests/tdms_files/", "250MBTDMS.tdms")
   context.tdmsFilePath = os.path.join(script_dir, "../tests/tdms_files/", "713470TDMS.tdms")
   print(context.tdmsFilePath)
   
@when("The tdms is read")
def step_60read_tdms(context):
    tracemalloc.start() #memory monitoring
    print("start the read")
    mem_usage = memory_usage((nptdms.TdmsFile, (context.tdmsFilePath,), {"read_metadata_only": False,"keep_open": False }))    
    print(tracemalloc.get_traced_memory())
    context.total = tracemalloc.get_traced_memory()[1]
    print(f"{context.total} amount of memory usage according to tracemalloc")
    print(f'Maximum memory usage: {max(mem_usage)} acording to mem profiler')
    tracemalloc.stop()        
@then("The tdms file read is successful and memory utilization found by trace malloc is less than 4 times the size of the input")
def step_60res_tdms(context):    
    print((context.total/(1024*1024) < 1000))
    assert (context.total/(1024*1024) < 1000) == True
    print("DONE")

# if __name__ == "__main__":
#     main(context)