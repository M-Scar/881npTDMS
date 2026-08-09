Feature: tdms large file  memory usage
Scenario: Read a tdms file of 60mb in size and achieve memory utilization below 240 Mb
    Given A TDMS of 60 Mb
    When The tdms is read
    Then The tdms file read is successful and memory utilization found by trace malloc is less than 4 times the size of the input