import os
import import_data

i = 1
print("number of test " + str(import_data.num_test))
if import_data.num_test == 0:
    print("there's no Test cases")
else:
    while int(i) <= import_data.num_test:
        print("\nnumer of test cases: " + str(import_data.num_test))

        if str(import_data.arrListTest[i - 1][0]) == "Login users registered":
            # print("\nName of the test case:" + import_data.arrListTest[i - 1][0] + " Login users registered")
            os.system('python -m pytest --durations=1 -v -s testLoginUserRegistered.py')
        elif str(import_data.arrListTest[i - 1][0]) == "unauthorized user":
            os.system('python -m pytest --durations=1 -v -s testUnregisteredUser.py')
            print("\nName of the test case:" + import_data.arrListTest[i - 1][0] + " unauthorized user")
        elif str(import_data.arrListTest[i - 1][0]) == "Password Required":
            os.system('python -m pytest --durations=1 -v -s testPasswordRequired.py')
            print("\nName of the test case:" + import_data.arrListTest[i - 1][0] + " Password Required")
        elif str(import_data.arrListTest[i - 1][0]) == "Username Required":
            os.system('python -m pytest --durations=1 -v -s tesUsernameRequired.py')
            print("\nName of the test case:" + import_data.arrListTest[i - 1][0] + " Username Required")
        elif str(import_data.arrListTest[i - 1][0]) == "locked out user":
            os.system('python -m pytest --durations=1 -v -s testLockedoutUser.py')
            print("\nName of the test case:" + import_data.arrListTest[i - 1][0] + " locked out user")
        elif str(import_data.arrListTest[i - 1][0]) == "performance user":
            os.system('python -m pytest --durations=1 -v -s testPerformanceUser.py')
            print("\nName of the test case:" + import_data.arrListTest[i - 1][0] + " performance user")
        elif str(import_data.arrListTest[i - 1][0]) == "unregistered User":
            os.system('python -m pytest --durations=1 -v -s testUnregisteredUser.py')
            print("\nName of the test case:" + import_data.arrListTest[i - 1][0] + " unregistered User")
        else:
            print("\ntest case not supported")
        print("\n Test Case Number= " + str(i))
        i += 1
