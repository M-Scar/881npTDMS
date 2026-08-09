from behave import given, when, then
import unittest as ut
import nptdms
import tempfile
import os
import tracemalloc
import numpy as np


@given("A TDMS with a file with all datatypes")
def step_v_tdms(context):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   context.compareDex = 0
   context.tdmsFilePath = os.path.join(script_dir, "../tests/tdms_files/DAQmxTypeTDMS", "TDMSAllData.tdms")
   print(context.tdmsFilePath)
   
@when("The all data type tdms is read using npTDMS")
def step_read_DAQTest_tdms(context):
    print("start the read")
    context.tdmsfile = nptdms.TdmsFile.read(context.tdmsFilePath)

@then("The tdms file ties integers to appropriate datatypes")
def step_Cmp_DaqVal_tdms(context):
    #compare against the assignments
   #  print(f"{type(context.tdmsfile.groups()[0].channels()[0][0])} is the value read")
    i8 = context.tdmsfile.groups()[0].channels()[1][1]
    i16 = context.tdmsfile.groups()[0].channels()[2][1]
    i32 = context.tdmsfile.groups()[0].channels()[3][1]
    i64 = context.tdmsfile.groups()[0].channels()[4][1]
   #  breakpoint()
    ut.TestCase().assertTrue(isinstance(i8,np.int8))
    ut.TestCase().assertTrue(isinstance(i16,np.int16))
    ut.TestCase().assertTrue(isinstance(i32,np.int32))
    ut.TestCase().assertTrue(isinstance(i64,np.int64))    
    print("DONE")
@then("The tdms file ties unsigned integers to appropriate datatypes")
def step_Cmp_DaqVal_tdms(context):
    #compare against the assignments
   #  print(f"{type(context.tdmsfile.groups()[0].channels()[0][0])} is the value read")
    ui8 = context.tdmsfile.groups()[0].channels()[5][1]
    ui16 = context.tdmsfile.groups()[0].channels()[6][1]
    ui32 = context.tdmsfile.groups()[0].channels()[7][1]
    ui64 = context.tdmsfile.groups()[0].channels()[8][1]
   #  breakpoint()
    ut.TestCase().assertTrue(isinstance(ui8,np.uint8))
    ut.TestCase().assertTrue(isinstance(ui16,np.uint16))
    ut.TestCase().assertTrue(isinstance(ui32,np.uint32))
    ut.TestCase().assertTrue(isinstance(ui64,np.uint64))    
    print("DONE")
@then("The tdms file ties floats to appropriate datatypes")
def step_Cmp_DaqVal_tdms(context):
    #compare against the assignments
   #  print(f"{type(context.tdmsfile.groups()[0].channels()[0][0])} is the value read")
    singleF = context.tdmsfile.groups()[0].channels()[9][1]
    doubleF = context.tdmsfile.groups()[0].channels()[10][1]
   #  breakpoint()
    ut.TestCase().assertTrue(isinstance(singleF,np.single))
    ut.TestCase().assertTrue(isinstance(doubleF,np.double))
    print("DONE")
@then("The tdms file ties void, string, booleans, and timestamps to appropriate datatypes")
def step_Cmp_DaqVal_tdms(context):
    #compare against the assignments
   #  print(f"{type(context.tdmsfile.groups()[0].channels()[0][0])} is the value read")
    voidVal = context.tdmsfile.groups()[0].channels()[0]    
    stringVal = context.tdmsfile.groups()[0].channels()[11][0]
    boolVal = context.tdmsfile.groups()[0].channels()[12][0]
    timeVal = context.tdmsfile.groups()[0].channels()[13][0]
   #  breakpoint()
    ut.TestCase().assertTrue(context.tdmsfile.groups()[0].channels()[0].dtype == 'V8') #no values
    ut.TestCase().assertTrue(isinstance(stringVal,str))
    ut.TestCase().assertTrue(isinstance(boolVal,np.uint8)) #np.bool could be expected
    ut.TestCase().assertTrue(isinstance(timeVal,np.datetime64)) 
    print("DONE")
@then("The tdms file ties complexes to appropriate datatypes")
def step_Cmp_DaqVal_tdms(context):
    #compare against the assignments
   #  print(f"{type(context.tdmsfile.groups()[0].channels()[0][0])} is the value read")
    comSingle = context.tdmsfile.groups()[0].channels()[14][0]    
    comDouble = context.tdmsfile.groups()[0].channels()[15][0]    
   #  breakpoint()    
    ut.TestCase().assertTrue(isinstance(comSingle,np.complex64))
    ut.TestCase().assertTrue(isinstance(comDouble,np.complex128)) #np.bool could be expected
    print("DONE")    
# if __name__ == "__main__":
#     main(context)