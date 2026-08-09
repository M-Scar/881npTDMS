Feature: tdms file reading of all data types
Scenario: Read a tdms file's data for all types
    Given A TDMS with a file with all datatypes
    When The all data type tdms is read using npTDMS 
    Then The tdms file ties integers to appropriate datatypes
    Then The tdms file ties unsigned integers to appropriate datatypes
    Then The tdms file ties floats to appropriate datatypes 
    Then The tdms file ties void, string, booleans, and timestamps to appropriate datatypes
    Then The tdms file ties complexes to appropriate datatypes 
       