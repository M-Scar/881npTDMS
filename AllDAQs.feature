Feature: tdms file reading of different DAQmx driver options for data
Scenario: Read a tdms file's data for voltage
    Given A TDMS with a file with voltage data
    When The DAQmx type tdms is read using npTDMS 
    Then The tdms file is read without error and can see the first value matches    
Scenario: Read a tdms file's data for current
    Given A TDMS with a file with current data
    When The DAQmx type tdms is read using npTDMS 
    Then The tdms file is read without error and can see the first value matches 
Scenario: Read a tdms file's data for Thermocouple
    Given A TDMS with a file with Thermocouple data
    When The DAQmx type tdms is read using npTDMS 
    Then The tdms file is read without error and can see the first value matches
Scenario: Read a tdms file's data for RTD
    Given A TDMS with a file with RTD data
    When The DAQmx type tdms is read using npTDMS 
    Then The tdms file is read without error and can see the first value matches              
Scenario: Read a tdms file's data for Strain
    Given A TDMS with a file with Strain data
    When The DAQmx type tdms is read using npTDMS 
    Then The tdms file is read without error and can see the first value matches         