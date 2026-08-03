Feature: tdms file level tdms property 
Scenario: Read a tdms file's file level property and identify proper datatype and value
    Given A TDMS with a file property
    When The tdms is read using npTDMS 
    Then The tdms file level property or properties are read with original datatypes
    Then The file property contains the proper value set in creation
 
Scenario: Read a tdms file's group level property and identify proper datatype and value
    Given A TDMS with a file property
    When The tdms is read using npTDMS 
    Then The tdms group level property or properties are read with original datatypes
    Then The group property contains the proper value set in creation    

Scenario: Read a tdms file's channel level property and identify proper datatype and value
    Given A TDMS with a file property
    When The tdms is read using npTDMS 
    Then The tdms channel level property or properties are read with original datatypes
    Then The channel property contains the proper value set in creation
