Feature: tdms file reading of different scaled DAQmx driver options for data
Scenario: Read a tdms file's data for scaled voltage
    Given A TDMS with a file with scaled voltage data
    When The scaled DAQmx type tdms is read using npTDMS 
    Then The tdms is read without error and its first value and scaled property match 
Scenario: Read a tdms file's data for scaled current
    Given A TDMS with a file with scaled current data
    When The scaled DAQmx type tdms is read using npTDMS 
    Then The tdms is read without error and its first value and scaled property match 
Scenario: Read a tdms file's data for scaled Thermocouple
    Given A TDMS with a file with scaled Thermocouple data
    When The scaled DAQmx type tdms is read using npTDMS 
    Then The tdms is read without error and its first value and scaled property match     
Scenario: Read a tdms file's data for scaled RTD
    Given A TDMS with a file with scaled RTD data
    When The scaled DAQmx type tdms is read using npTDMS 
    Then The tdms is read without error and its first value and scaled property match 
Scenario: Read a tdms file's data for scaled Strain
    Given A TDMS with a file with scaled Strain data
    When The scaled DAQmx type tdms is read using npTDMS 
    Then The tdms is read without error and its first value and scaled property match     