Three commands are used to execute categories of tests within this module.
.\coverage_report.sh , python -m unittest , and behave [featurename].feature where featurename is one of 'properties', 'AllDAQs', 'AllDatatypes', 'ScaleAllDAQs', or 'size'.

Execution of these scripts was possible under a venv environment versioned Python 3.12.10. 
Dependencies are present in tests/requirements.txt and may be downloaded to the environment via 'pip install -r requirements.txt'.

Note that saboteur tests use LabVIEW 2026 runtime for executables it calls. LabVIEW runtime is available for free at https://www.ni.com/en/support/downloads/software-products/download.labview-runtime.html and enables these tests run by python -m unittest. A successful run of that test is best done manually, but with waits in place and os control of the executables, an initialized runtime will properly open the executable program and run it concurrently with the npTDMS read.

