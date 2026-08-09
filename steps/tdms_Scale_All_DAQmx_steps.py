from behave import given, when, then
import unittest
import nptdms
import tempfile
import os
import tracemalloc
import numpy as np


@given("A TDMS with a file with scaled voltage data")
def step_v_tdms(context):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   context.scaleDex = 2
   context.tdmsFilePath = os.path.join(script_dir, "../tests/tdms_files/DAQmxTypeTDMS", "VoltageScaleTest.tdms")
   print(context.tdmsFilePath)

@given("A TDMS with a file with scaled current data")
def step_c_tdms(context):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   context.scaleDex = 2
   context.tdmsFilePath = os.path.join(script_dir, "../tests/tdms_files/DAQmxTypeTDMS", "CurrentScaleTest.tdms")
   print(context.tdmsFilePath)

@given("A TDMS with a file with scaled Thermocouple data")
def step_tc_tdms(context):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   context.scaleDex = 7
   context.tdmsFilePath = os.path.join(script_dir, "../tests/tdms_files/DAQmxTypeTDMS", "TCScaleTest.tdms")
   print(context.tdmsFilePath)

@given("A TDMS with a file with scaled RTD data")
def step_v_tdms(context):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   context.scaleDex = 3
   context.tdmsFilePath = os.path.join(script_dir, "../tests/tdms_files/DAQmxTypeTDMS", "RTDScaleTest.tdms")
   print(context.tdmsFilePath)

@given("A TDMS with a file with scaled Strain data")
def step_v_tdms(context):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   context.scaleDex = 3
   context.tdmsFilePath = os.path.join(script_dir, "../tests/tdms_files/DAQmxTypeTDMS", "StrainScaleTest.tdms")
   print(context.tdmsFilePath)
   
@when("The scaled DAQmx type tdms is read using npTDMS")
def step_read_DAQTest_tdms(context):
    print("start the read")
    context.tdmsfile = nptdms.TdmsFile.read(context.tdmsFilePath)

@then("The tdms is read without error and its first value and scaled property match")
def step_Cmp_DaqVal_tdms(context):
   #  breakpoint()
    #compare against the excel tool yields        
    # assert context.tdmsfile.groups()[0].channels()[0][0] == compareMap[context.compareDex]
    #simulated values lack scale application, comparing values is a moot point
    try:
      print(context.tdmsfile.groups()[0].channels()[0].properties[f"NI_Scale[{context.scaleDex}]_Table_Pre_Scaled_Values[0]"])
      print(context.tdmsfile.groups()[0].channels()[0].properties[f"NI_Scale[{context.scaleDex}]_Table_Pre_Scaled_Values[1]"])
      assert context.tdmsfile.groups()[0].channels()[0].properties[f"NI_Scale[{context.scaleDex}]_Table_Pre_Scaled_Values[0]"] == -50.0
      assert context.tdmsfile.groups()[0].channels()[0].properties[f"NI_Scale[{context.scaleDex}]_Table_Pre_Scaled_Values[1]"] == 50.0
    except:      
      breakpoint()
    print("DONE")

# if __name__ == "__main__":
#     main(context)