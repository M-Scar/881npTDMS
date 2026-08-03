from behave import given, when, then
from nptdms import TdmsFile
import tempfile
import os

@given("A TDMS with a file property")
def step_create_tdms(context):
   context.tdms_file = TdmsFile.read("propertyLadenTDMS.tdms")

@when("The tdms is read using npTDMS")
def step_read_tdms(context):
    #loop through for value printouts. from there, assertions are made based on datatype and value comapred to original.
    context.fileProps = dict()
    context.groupProps = dict()
    context.channelProps = dict()
    #file level properties
    for name, value in context.tdms_file.properties.items():
        print("{0}: {1}".format(name, value))
        context.fileProps[name] = value
     # group level properties. duplicate properties overwrite, they are written to be the same. testing name:value only
    for group in context.tdms_file.groups():
        context.groupProps[group.name] = {}

        for name, value in group.properties.items():
            print(f"Group '{group.name}': {name} = {value}")
            context.groupProps[name] = value
    # Channel properties. duplicate properties overwrite, they are written to be the same. testing name:value only
    for group in context.tdms_file.groups():
        for channel in group.channels():
            key = f"{group.name}/{channel.name}"
            context.channelProps[key] = {}

            for name, value in channel.properties.items():
                print(f"Channel '{key}': {name} = {value}")
                context.channelProps[name] = value

@then("The tdms file level property or properties are read with original datatypes")
def step_check_metadata_file(context):
    print("fileStringProp"+(str)(type(context.fileProps["fileStringProp"])))    
    assert (type(context.fileProps["fileStringProp"])) is str
    print("fileIntProp"+(str)(type(context.fileProps["fileIntProp"])))
    assert (type(context.fileProps["fileIntProp"])) is int

@then("The file property contains the proper value set in creation")
def step_check_metadata_file_val(context):
    print("fileStringProp is "+(str)((context.fileProps["fileStringProp"])))    
    assert ((context.fileProps["fileStringProp"])) == "string value"
      
@then("The tdms group level property or properties are read with original datatypes")
def step_check_metadata_group(context):
    print("boolGroupProp"+(str)(type(context.groupProps["boolGroupProp"])))    
    assert (type(context.groupProps["boolGroupProp"])) is bool

@then("The group property contains the proper value set in creation")
def step_check_metadata_group_val(context):
    print("boolGroupProp"+(str)((context.groupProps["boolGroupProp"])))    
    assert ((context.groupProps["boolGroupProp"])) is True

#numpydatetime and its value are compared to the string output and its value as a special case
@then("The tdms channel level property or properties are read with original datatypes")
def step_check_metadata_channel(context):
    print("wf_start_time"+(str)(type(context.channelProps["wf_start_time"])))    
    assert (str)(type(context.channelProps["wf_start_time"])) == "<class 'numpy.datetime64'>"

@then("The channel property contains the proper value set in creation")
def step_check_metadata_channel_val(context):
    print("wf_start_time"+(str)((context.channelProps["wf_start_time"])))    
    assert (str)((context.channelProps["wf_start_time"])) == "2026-08-02T19:13:57.189018"