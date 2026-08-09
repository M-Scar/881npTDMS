from behave import given, when, then
import unittest
import nptdms
import tempfile
import os
import tracemalloc
import numpy as np


@given("A TDMS with a file with voltage data")
def step_v_tdms(context):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   context.compareDex = 0
   context.tdmsFilePath = os.path.join(script_dir, "../tests/tdms_files/DAQmxTypeTDMS", "VoltageTest.tdms")
   print(context.tdmsFilePath)

@given("A TDMS with a file with current data")
def step_c_tdms(context):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   context.compareDex = 1
   context.tdmsFilePath = os.path.join(script_dir, "../tests/tdms_files/DAQmxTypeTDMS", "CurrentTest.tdms")
   print(context.tdmsFilePath)

@given("A TDMS with a file with Thermocouple data")
def step_tc_tdms(context):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   context.compareDex = 2
   context.tdmsFilePath = os.path.join(script_dir, "../tests/tdms_files/DAQmxTypeTDMS", "ThermocoupleTest.tdms")
   print(context.tdmsFilePath)

@given("A TDMS with a file with RTD data")
def step_v_tdms(context):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   context.compareDex = 3
   context.tdmsFilePath = os.path.join(script_dir, "../tests/tdms_files/DAQmxTypeTDMS", "RTDTest.tdms")
   print(context.tdmsFilePath)

@given("A TDMS with a file with Strain data")
def step_v_tdms(context):
   script_dir = os.path.dirname(os.path.abspath(__file__))
   context.compareDex = 4
   context.tdmsFilePath = os.path.join(script_dir, "../tests/tdms_files/DAQmxTypeTDMS", "StrainTest.tdms")
   print(context.tdmsFilePath)
   
@when("The DAQmx type tdms is read using npTDMS")
def step_read_DAQTest_tdms(context):
    print("start the read")
    context.tdmsfile = nptdms.TdmsFile.read(context.tdmsFilePath)

@then("The tdms file is read without error and can see the first value matches")
def step_Cmp_DaqVal_tdms(context):
    # breakpoint()
    #compare against the excel tool yields
    compareMap = [-0.09201190203707943, -0.000299811381090366, -3.27551426381284,
    48.1027481241774, 0.0000299260038093331]
    print(f"{context.tdmsfile.groups()[0].channels()[0][0]} is the value read")
    # assert context.tdmsfile.groups()[0].channels()[0][0] == compareMap[context.compareDex]
    #because of escel precision, np isclose with tight tolerance is better
    assert np.isclose(context.tdmsfile.groups()[0].channels()[0][0], compareMap[context.compareDex], rtol=1e-14, atol=1e-14)
    print("DONE")

# if __name__ == "__main__":
#     main(context)