Project Name:
Test Login Page [IOET - QA - www.saucedemo.com] with Firefox Browser.

Description:


* This script for test following Scenarios: 
```sh
* Login users registered
* Unauthorized user
* Password Required
* Username Required
* Locked out user
* Performance user
* Unregistered User
```
* Before running the script, make sure the input file [input.xlsx] is in the same directory as the script.
* [input.xlsx] must be at the follwing format [Column 1: Case Name, Column 2: Website, Column 3: Username, Column 4: Password]
* The Script will use the data of the second row.
* When the test done, will be remove the row of test case from the input file, and will be generated or updated [output.xlsx], 
* [output.xlsx] Contain the following information of the last test [Column 1: Case Name, Column 2: Website, Column 3: Username, Column 4: Password, Column 5: Test date]

## Install prerequisite packages

```sh
pip install -U pytest
pip install -U openpyxl
pip install -U selenium
pip install -U pandas

```

## To run the test script

```sh
python -m pytest --durations=1 -v -s .\startTest.py
```
"import_data.py" For import the input data


## Author

Amjad AlMouayad

