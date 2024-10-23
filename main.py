from medicalTest import MedicalTest
from patient import Patient
from medicalRecord import MedicalRecord
from datetime import datetime, timedelta
import copy
patients = {}  # dictionary to store patients with patient_id as the key
medicalTestList = []  # list to store medical tests


def print_all_patients():
    if not patients:
        print("No patients found.")
        return

    for patient_id, tests in patients.items():
        print(f"Patient ID: {patient_id}")
        if not patients.values():
            print("  No tests found for this patient.")
        else:
            print("Tests:")
            for test in tests:
                print(f"  Test Name: {test.get('test_name', 'N/A')}")
                print(f"  Test Date: {test.get('test_date', 'N/A')}")
                print(f"  Result Value: {test.get('result_value', 'N/A')}")
                print(f"  Result Unit: {test.get('result_unit', 'N/A')}")
                print(f"  Result Status: {test.get('result_status', 'N/A')}")
                print(f"  Result Date/Time: {test.get('result_date_time', 'N/A')}")
                print("-" * 30)
            print("=" * 50)


def DateExpired(uyear, umonth, uday, uhour, umin, tday, thour, tminute):
    flag = 0
    user_time = datetime(uyear, umonth, uday, uhour, umin)

    time_delta = timedelta(days=tday, hours=thour, minutes=tminute)

    expiration_time = user_time + time_delta

    if expiration_time <= datetime.now():
        return ["completed", expiration_time]
    else:
        return ["pending", expiration_time]


def load_medical_tests():
    with open("medicalTest.txt", "r+") as medicalTest:
        lines = medicalTest.readlines()  # This returns a list of strings
        for line in lines:

            part1 = line.strip().split("(")  # Apply split() to each line (split by whitespace)
            temp = part1[1].split(")")
            name = str(temp[0])

            part2 = line.strip().split()
            if part2[len(part2) - 5] == "<" and part2[len(part2) - 7] == ">":
                fRange = line.strip().split(">")
                ffRange = fRange[1].split(",")
                range1 = float(ffRange[0])

                sRange = line.strip().split("<")
                ssRange = sRange[1].split(";")
                range2 = float(ssRange[0])

            elif part2[len(part2) - 5] == "<":
                fRange = line.strip().split("<")
                ffRange = fRange[1].split(";")
                range1 = float(ffRange[0])
                range2 = 0

            part3 = line.strip().split()
            funit = part3[len(part3) - 2].split(",")
            unit = str(funit[0])

            part4 = line.strip().split()
            dateInfo = part4[len(part4) - 1].split("-")
            day = int(dateInfo[0])
            hour = int(dateInfo[1])
            minute = int(dateInfo[2])
            medicalTestList.append(MedicalTest(name, range1, range2, unit, day, hour, minute))
        return medicalTestList


def addNewMedicalTest():  # this function to add a new medical test
    days = 0
    hours = 0
    minutes = 0
    range1 = 0
    range2 = 0
    fo = open("medicalTest.txt", "r+")
    fo.read()
    newMedicalTest = []

    # input for medical test name
    while True:
        name = input("please enter a medical test name: ")
        try:
            float(name)
            print("please enter a non numeric value.")
        except ValueError:
            # print("you entered a non numeric value: " + name)
            break

    # input for medical test symbol
    while True:
        symbol = input("please enter a medical test symbol: ")
        try:
            float(symbol)
            print("please enter a non numeric value.")
        except ValueError:
            # print("you entered a non numeric value: " + symbol)
            break

    # choose the type of range for the medical test
    print("please enter a medical test range.")
    print("1- the medical test range will be between two values.")
    print("2- the medical test range will be more than value.")
    print("3- the medical test range will be less than value.")
    choice = int(input())

    if choice == 1:  # range between two values
        while True:
            try:
                range1 = int(input("please enter the first range value: "))
                while range1 < 0:
                    print("please enter a positive number.")
                    range1 = int(input("please enter the first range value: "))
                range2 = int(input("please enter the second range value: "))
                while range2 < 0:
                    print("please enter a positive number.")
                    range2 = int(input("please enter the second range value: "))
                days = int(input("please enter the number of days: "))
                while days < 0:
                    print("please enter a positive number.")
                    days = int(input("please enter the number of days: "))
                hours = int(input("please enter the number of hours: "))
                while hours < 0:
                    print("please enter a positive number.")
                    hours = int(input("please enter the number of hours: "))
                minutes = int(input("please enter the number of minutes: "))
                while minutes < 0:
                    print("please enter a positive number.")
                    minutes = int(input("please enter the number of minutes: "))
                break
            except ValueError:
                print("invalid input! please enter a valid integer.")

        while True:
            try:
                unit = input("please enter the unit: ")
                float(unit)
                print("please enter a non numeric value.")
            except ValueError:
                print("")
                break

        # create and configure new MedicalTest object
        test = MedicalTest(symbol, range1, range2, unit, days, hours, minutes)
        test.rangeOrder()

        # format new test details and add to list
        newMedicalTest.append(
            f"Name: {name} ({test.testName}); Range: > {test.range}, < {test.range2}; Unit: {test.unit}, ")
        if days < 10:
            newMedicalTest.append("0" + str(days) + "-")
        else:
            newMedicalTest.append(str(days) + "-")
        if hours < 10:
            newMedicalTest.append("0" + str(hours) + "-")
        else:
            newMedicalTest.append(str(hours) + "-")
        if minutes < 10:
            newMedicalTest.append("0" + str(minutes))
        else:
            newMedicalTest.append(str(minutes))
    elif choice == 2 or choice == 3:  # range more than or less than value
        range2 = 0
        while True:
            try:
                range = int(input("please enter the first range value: "))
                while range < 0:
                    print("please enter a positive number.")
                    range = int(input("please enter the first range value: "))

                days = int(input("please enter the number of days: "))
                while days < 0:
                    print("please enter a positive number.")
                    days = int(input("please enter the number of days: "))
                hours = int(input("please enter the number of hours: "))
                while hours < 0:
                    print("please enter a positive number.")
                    hours = int(input("please enter the number of hours: "))
                minutes = int(input("please enter the number of minutes: "))
                while minutes < 0:
                    print("please enter a positive number.")
                    minutes = int(input("please enter the number of minutes: "))
                break
            except ValueError:
                print("invalid input! please enter a valid integer.")

        while True:
            unit = input("please enter the unit: ")
            try:
                float(unit)
                print("please enter a non numeric value.")
            except ValueError:
                print("")
                break

        # create new MedicalTest obj
        test = MedicalTest(symbol, range, range2, unit, days, hours, minutes)
        #print("test .range is ", test.range)
        test.rangeOrder()
        if choice == 2:
            newMedicalTest.append(f"Name: {name} ({symbol}); Range: > {test.range}; Unit: {test.unit}, ")
        elif choice == 3:
            newMedicalTest.append(f"Name: {name} ({symbol}); Range: < {test.range}; Unit: {test.unit}, ")
        if days < 10:
            newMedicalTest.append("0" + str(days) + "-")
        else:
            newMedicalTest.append(str(days) + "-")
        if hours < 10:
            newMedicalTest.append("0" + str(hours) + "-")
        else:
            newMedicalTest.append(str(hours) + "-")
        if minutes < 10:
            newMedicalTest.append("0" + str(minutes))
        else:
            newMedicalTest.append(str(minutes))

    newMedicalTest.append("\n")  # append newline to separate entries
    fo.writelines(newMedicalTest)  # write new test details to file
    fo.close()  # close the file
    medicalTestList.append(MedicalTest(symbol, range1, range2, unit, days, hours, minutes))  # add to list


def addNewMedicalRecord():
    # initialize new_record with a default value to avoid UnboundLocalError
    new_record = {}

    # input validation for patient ID, test result, and time data
    while True:
        try:
            # input and validate patient ID
            patient_id = input("please enter the patient ID: ")
            while len(patient_id) != 7 or not patient_id.isdigit():
                print("please enter a valid patient ID (7 digits).")
                patient_id = input("please enter the patient ID: ")

            patient_id=int(patient_id)

            # input and validate test result
            result = float(input("please enter the test result: "))
            while result < 0:
                print("please enter a positive number.")
                result = float(input("please enter the test result: "))

            # input and validate year
            year = int(input("please enter the year: "))
            while len(str(year)) != 4:
                print("please enter a valid year (4 digits).")
                year = int(input("please enter the year: "))

            # input and validate month
            month = int(input("please enter the month: "))
            while month < 1 or month > 12:
                print("please enter a valid month (1-12).")
                month = int(input("please enter the month: "))

            # input and validate day
            day = int(input("please enter the day: "))
            while day < 1 or day > 31:
                print("please enter a valid day (1-31).")
                day = int(input("please enter the day: "))

            # input and validate hour
            hour = int(input("please enter the hour: "))
            while hour < 0 or hour > 23:
                print("please enter a valid hour (0-23).")
                hour = int(input("please enter the hour: "))

            # input and validate minute
            minute = int(input("please enter the minute: "))
            while minute < 0 or minute > 59:
                print("please enter a valid minute (0-59).")
                minute = int(input("please enter the minute: "))

            break
        except ValueError:
            print("invalid input! please enter valid integers.")

    # format date and time correctly
    formatted_date = datetime(year, month, day, hour, minute)
    formatted_date = formatted_date.strftime('%Y-%m-%d %H:%M')

    # ask for the test name and validate it
    while True:
        test_name = input("please enter a valid test name: ").strip()
        valid_test = False
        for test in medicalTestList:
            if test_name == test.get_testName():
                valid_test = True
                unit = test.get_unit()
                tday = int(test.get_day())
                thour = int(test.get_hour())
                tminute = int(test.get_minute())
                break
        if valid_test:
            break
        else:
            print("test name not found. please enter a valid test name.")

    # input for status and its validation
    while True:
        status = input("enter the medical record status (pending|reviewed): ").strip()
        if status in ["pending", "reviewed"]:
            break
        else:
            print("please enter a valid status: reviewed or pending.")

    # calculate the expiration date and status
    listTime = DateExpired(year, month, day, hour, minute, tday, thour, tminute)
    expiration_status, expiration_time = listTime
    print(expiration_time)

    # create the new record entry based on expiration status
    if expiration_status == "completed":
        new_record = {
            'test_name': test_name,
            'test_date': formatted_date,
            'result_value': result,
            'result_unit': unit,
            'result_status': "completed",
            'result_date_time': expiration_time.strftime('%Y-%m-%d %H:%M')
        }
    else:
        new_record = {
            'test_name': test_name,
            'test_date': formatted_date,
            'result_value': result,
            'result_unit': unit,
            'result_status': status
        }

    # print the dictionary contents correctly
    print(new_record.items())

    # add new record to the dictionary under the corresponding ID
    if patient_id in patients:
        patients[patient_id].append(new_record)
    else:
        patients[patient_id] = [new_record]

    # write to file
    fo = open("medicalRecord.txt", "r+")
    fo.read()
    fo.write(write_record(new_record, patient_id))
    fo.close()


def write_record(new_record, patient_id):
    if new_record["result_status"] == "completed":
        return f"{patient_id}: {new_record['test_name']}, {new_record['test_date']}, {new_record['result_value']}, {new_record['result_unit']}, {new_record['result_status']}, {new_record['result_date_time']}\n"

    return f"{patient_id}: {new_record['test_name']}, {new_record['test_date']}, {new_record['result_value']}, {new_record['result_unit']}, {new_record['result_status']}\n"


filtered_records = []
testList = load_medical_tests()

def filters():
    status = ""
    patient_id = ""
    idflag = 0
    nameflag = 0
    abnormalflag = 0
    specficflag = 0
    statusflag = 0
    turnaroundflag = 0
    filtered_id = []
    record = ""

    # input validation for filtering options
    while True:
        try:
            print("choose 1 if you want to do it and 0 if you don't:")
            idflag = int(input("filter by id (1/0): "))
            while idflag not in [0, 1]:
                print("please enter a valid value (1/0).")
                idflag = int(input("filter by id (1/0): "))
            break
        except ValueError:
            print("invalid input! please enter a valid integer.")

    while True:
        try:
            print("choose 1 if you want to do it and 0 if you don't:")
            nameflag = int(input("filter by name (1/0): "))
            while nameflag not in [0, 1]:
                print("please enter a valid value (1/0).")
                nameflag = int(input("filter by name (1/0): "))
            break
        except ValueError:
            print("invalid input! please enter a valid integer.")

    while True:
        try:
            print("choose 1 if you want to do it and 0 if you don't:")
            abnormalflag = int(input("filter by abnormal (1/0): "))
            while abnormalflag not in [0, 1]:
                print("please enter a valid value (1/0).")
                abnormalflag = int(input("filter by abnormal (1/0): "))
            break
        except ValueError:
            print("invalid input! please enter a valid integer.")

    while True:
        try:
            print("choose 1 if you want to do it and 0 if you don't:")
            specficflag = int(input("filter by specific period (1/0): "))
            while specficflag not in [0, 1]:
                print("please enter a valid value (1/0).")
                specficflag = int(input("filter by specific period (1/0): "))
            break
        except ValueError:
            print("invalid input! please enter a valid integer.")

    while True:
        try:
            print("choose 1 if you want to do it and 0 if you don't:")
            statusflag = int(input("filter by status (1/0): "))
            while statusflag not in [0, 1]:
                print("please enter a valid value (1/0).")
                statusflag = int(input("filter by status (1/0): "))

            break
        except ValueError:
            print("invalid input! please enter a valid integer.")

    if statusflag == 1:
        status = input("please enter the medical record status (completed|pending|reviewed): ")
        while status not in ["completed", "pending", "reviewed"]:
            status = input("please enter a valid medical record status (completed|pending|reviewed): ")

    while True:
        try:
            print("choose 1 if you want to do it and 0 if you don't:")
            turnaroundflag = int(input("filter by turnaround (1/0): "))
            while turnaroundflag not in [0, 1]:
                print("please enter a valid value (1/0).")
                turnaroundflag = int(input("filter by turnaround (1/0): "))
            break
        except ValueError:
            print("invalid input! please enter a valid integer.")

    filtered_records.clear()
    for record in patients.items():
        filtered_records.append(copy.deepcopy(record))

    if idflag == 1 or nameflag == 1 or abnormalflag == 1 or specficflag == 1 or statusflag == 1 or turnaroundflag == 1:
        if idflag == 1:
            while True:
                try:
                    patient_id = input("enter id value: ")
                    if len(patient_id) == 7 and patient_id.isdigit():
                        break
                    else:
                        print("please enter a 7-digit id.")
                except ValueError:
                    print("invalid input! please enter a valid id.")
            i = 0
            while i < len(filtered_records):
                if filtered_records[i][0] != patient_id:
                    filtered_records.pop(i)

                else:
                    i = i + 1

        if nameflag == 1:
            while True:
                name = input("please enter a valid test name: ").strip()
                valid_test = False
                for test in medicalTestList:
                    if name == test.get_testName():
                        valid_test = True
                        break
                if valid_test:
                    break
                else:
                    print("test name not found. please enter a valid test name.")
            i = 0
            while i < len(filtered_records):
                record = filtered_records[i][1]
                j = 0
                while j < len(record):
                    if (record[j]['test_name'] != name):
                        record.pop(j)
                    else:
                        j = j + 1
                    if len(record) == 0:
                        filtered_records.pop(i)
                        i -= 1
                i += 1

        if abnormalflag == 1:
            i = 0
            while i in range(0, len(filtered_records)):
                record = filtered_records[i][1]
                j = 0
                while j < len(record):
                    for test in medicalTestList:
                        if record[j]['test_name'] == test.get_testName():
                            if test.get_range2() == 0:

                                if float(record[j]['result_value']) < test.get_range():
                                    record.pop(j)
                                else:
                                    j += 1
                                if len(record) == 0:
                                    filtered_records.pop(i)
                                    i -= 1
                                    break
                                if j > len(record) - 1:
                                    break
                            else:
                                if float(record[j]['result_value']) > (test.get_range()) and float(
                                        record[j]['result_value']) < (test.get_range2()):
                                    record.pop(j)
                                else:
                                    j += 1
                                if len(record) == 0:
                                    filtered_records.pop(i)
                                    i -= 1
                                    break
                                if j > len(record) - 1:
                                    break

                i += 1

        if specficflag == 1:

            while True:
                firstDate = input("Please enter a valid test date and time (yyyy-mm-dd HH:MM): ")
                try:
                    valid_first_date = datetime.strptime(firstDate, "%Y-%m-%d %H:%M")
                    print("Valid date and time entered:", valid_first_date)
                    break
                except ValueError:
                    print("Invalid format. Please enter the date and time in the format yyyy-mm-dd HH:MM.")

            # Get the second valid date and time
            while True:
                secondDate = input("Please enter a valid test date and time (yyyy-mm-dd HH:MM): ")
                try:
                    valid_second_date = datetime.strptime(secondDate, "%Y-%m-%d %H:%M")
                    print("Valid date and time entered:", valid_second_date)
                    break
                except ValueError:
                    print("Invalid format. Please enter the date and time in the format yyyy-mm-dd HH:MM.")

            if valid_first_date > valid_second_date:
                temp = valid_first_date
                valid_first_date = valid_second_date
                valid_second_date = temp
            i = 0
            while i in range(0, len(filtered_records)):
                record = filtered_records[i][1]
                j = 0
                while j in range(0, len(record)):
                    test_date = datetime.strptime(record[j]['test_date'], "%Y-%m-%d %H:%M")
                    if test_date < valid_first_date or test_date > valid_second_date:
                        record.pop(j)
                    else:
                        j = j + 1
                    if (len(record) == 0):
                        filtered_records.pop(i)
                        i -= 1

                i += 1

        if statusflag == 1:
            i = 0
            while i in range(0, len(filtered_records)):
                record = filtered_records[i][1]
                j = 0
                while j in range(0, len(record)):
                    if record[j]['result_status'] != status:
                        record.pop(j)
                    else:
                        j += 1

                    if (len(record) == 0):
                        filtered_records.pop(i)
                        i -= 1

                i += 1

        if turnaroundflag == 1:
            i = 0
            max = timedelta(days=0, hours=0, minutes=0)
            min = timedelta(days=medicalTestList[0].get_day(), hours=medicalTestList[0].get_hour(),
                            minutes=medicalTestList[0].get_minute())
            minTestName = medicalTestList[0].get_testName()

            maxTestName = ""
            for test in medicalTestList:
                tday = test.get_day()
                thour = test.get_hour()
                tminute = test.get_minute()
                test_time = timedelta(days=tday, hours=thour, minutes=tminute)
                if max < test_time:
                    max = test_time
                    maxTestName = test.get_testName()
                if min > test_time:
                    min = test_time
                    minTestName = test.get_testName()
            i = 0
            while i < len(filtered_records):
                record = filtered_records[i][1]

                j = 0
                while j < len(record):
                    if (record[j]['test_name'] != maxTestName and record[j]['test_name'] != minTestName) or record[j][
                        'result_status'] == "pending":
                        record.pop(j)
                    else:
                        j = j + 1
                    if len(record) == 0:
                        filtered_records.pop(i)
                        i -= 1

                i += 1

        for records in filtered_records:
            record_id = records[0]
            print(f"\nThe patient ID is: {record_id}")
            print("=" * 160)
            print("Patient Records Info")
            print("=" * 160)
            for record in records[1]:
                print(f"Test Name       : {record['test_name']}")
                print(f"Test Date       : {record['test_date']}")
                print(f"Result Value    : {record['result_value']} {record['result_unit']}")
                print(f"Result Status   : {record['result_status']}")
                if record['result_status'] == "completed":
                    print(f"Result Date Time: {record['result_date_time']}")
                print("-" * 160)


def export_medicalRecords():
    try:
        fo = open("medicalRecord.txt", "w")
        for patient_id, tests in patients.items():  # iterating over all patients and all their tests in patients dictionary
            for test in tests:  # iterating over every test in all the tests of one patient
                line = f"{patient_id}: {test['test_name']}, {test['test_date']}, {test['result_value']}, {test['result_unit']}, {test['result_status']}, {test.get('result_date_time', '')}\n"
                fo.write(line)
        fo.close()
    except IOError:
        print("Error: Not able to write to medicalRecord.txt.")


def update_patient_record():
    # prompt user for patient ID
    patient_id = input("Enter the patient ID: ").strip()

    # check if patient exists
    if patient_id not in patients:
        print(f"Patient with ID {patient_id} not found.")
        return

    test_name = input("Enter the test name to update: ").strip()
    # locate the patient
    patient_tests = patients[patient_id]

    # check if test record exists
    test_found = False
    for record in patient_tests:
        if record['test_name'] == test_name:
            test_found = True
            # prompt user for new details
            print("Please select which field you want to update.")
            print("1-Test Name.")
            print("2-Test Date.")
            print("3-Test Value.")
            print("4-Test Unit.")
            print("5-Test Status.")
            choice = input().strip()
            if choice == "1":
                new_test_name = input("Enter the new test name: ").strip()
                record['test_name'] = new_test_name
            elif choice == "2":
                new_test_date = input("Enter the new test date (YYYY-MM): ").strip()
                record['test_date'] = new_test_date
            elif choice == "3":
                new_value = input("Enter the new result value: ").strip()
                record['result_value'] = new_value
            elif choice == "4":
                new_unit = input("Enter the new result unit: ").strip()
                record['result_unit'] = new_unit
            elif choice == "5":
                new_status = input("Enter the new result status: ").strip()
                record['result_status'] = new_status
                if new_status.lower() == "completed":
                    new_result_time = input("Enter the new result date/time (YYYY-MM-DD HH:MM): ").strip()
                    record['result_time'] = new_result_time
            else:
                print("Invalid choice.")
                return

            print(f"Test {test_name} for patient {patient_id} was updated successfully!")
            break

    if not test_found:
        print(f"Test {test_name} not found for patient ID {patient_id}.")


def update_medical_test():
    #load medical tests from the file into a dictionary
    tests_dict = {}
    try:
        with open("medicalTest.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(";")

                #extract test details
                name_part = parts[0].split("(")
                test_name = name_part[0].strip().split(":")[1].strip()
                symbol = name_part[1].strip(")")

                range_part = parts[1].split(",")
                range_values = []

                #process the first range (e.g., "> 5")
                if len(range_part) > 0:
                    first_range_value = range_part[0].strip().split()[-1]
                    if first_range_value.replace(".", "", 1).isdigit():
                        range_values.append(float(first_range_value))

                #process the second range if it exists (e.g., "< 100")
                if len(range_part) > 1:
                    second_range_value = range_part[1].strip().split()[0]
                    if second_range_value.replace(".", "", 1).isdigit():
                        range_values.append(float(second_range_value))

                unit_part = parts[2].split(":")[1].strip()
                unit = unit_part.split(",")[0].strip()

                time_part = unit_part.split(",")[1].strip()
                time_values = time_part.split("-")

                day = int(time_values[0])
                hour = int(time_values[1])
                minute = int(time_values[2])

                #create a dictionary entry
                tests_dict[symbol] = {
                    "name": test_name,
                    "range1": range_values[0] if len(range_values) > 0 else None,
                    "range2": range_values[1] if len(range_values) > 1 else None,
                    "unit": unit,
                    "day": day,
                    "hour": hour,
                    "minute": minute
                }

    except Exception as e:
        print("error loading medical tests:", e)
        return

    #prompt user for the test symbol to update
    symbol_to_update = input("enter the symbol of the test to update: ").strip()

    if symbol_to_update not in tests_dict:
        print("test not found!")
        return

    #get the existing test details
    test = tests_dict[symbol_to_update]

    #prompt for updates or keep old values
    new_test_name = input(
        f"please insert the new test name (or press enter to keep current name: {test['name']}): ").strip() or test[
                        'name']
    new_range1 = input(
        f"please insert the new first range value (or press enter to keep current value: {test['range1']}): ").strip()
    new_range2 = input(
        f"please insert the new second range value (or press enter to keep current value: {test['range2']}): ").strip()
    new_unit = input(f"please insert the new unit (or press enter to keep current unit: {test['unit']}): ").strip() or \
               test['unit']

    new_day = input(f"please insert the new day (or press enter to keep current day: {test['day']}): ").strip()
    new_hour = input(f"please insert the new hour (or press enter to keep current hour: {test['hour']}): ").strip()
    new_minute = input(
        f"please insert the new minute (or press enter to keep current minute: {test['minute']}): ").strip()

    try:
        #update the dictionary with new values
        test['name'] = new_test_name
        test['range1'] = float(new_range1) if new_range1 else test['range1']
        test['range2'] = float(new_range2) if new_range2 else test['range2']
        test['unit'] = new_unit
        test['day'] = int(new_day) if new_day else test['day']
        test['hour'] = int(new_hour) if new_hour else test['hour']
        test['minute'] = int(new_minute) if new_minute else test['minute']

    except ValueError as e:
        print("invalid input:", e)
        return

    #write back to the file in correct format
    try:
        with open("medicalTest.txt", "w") as file:
            for symbol, details in tests_dict.items():
                range_part = ""
                if details['range1'] is not None and details['range2'] is None:
                    range_part = f"< {details['range1']}"
                if details['range1'] is not None and details['range2'] is not None:
                    range_part = f"> {details['range1']}"
                if details['range2'] is not None:
                    range_part += f", < {details['range2']}"
                time_part = f"{details['day']:02d}-{details['hour']:02d}-{details['minute']:02d}"
                file.write(
                    f"Name: {details['name']} ({symbol}); Range: {range_part}; Unit: {details['unit']}, {time_part}\n")

        print("medical test updated successfully!")

    except Exception as e:
        print("error updating file:", e)


def generate_summary_reports(filtered_records):
    if not filtered_records:
        print("no records to summarize!")  # notify if no records are available
        return

    # Initialize variables for calculations
    min_test_value = float('inf')  # Start with infinity to find minimum
    max_test_value = float('-inf')  # Start with negative infinity to find maximum
    total_test_value = 0
    test_count = 0

    min_turnaround_time = timedelta(days=0, hours=0, minutes=0)  # start with zero timedelta for minimum
    max_turnaround_time = timedelta(days=0, hours=0, minutes=0)  # start with zero timedelta for maximum
    total_turnaround_time = timedelta()  # initialize total turnaround time
    turnaround_count = 0

    # Calculate statistics
    for records in filtered_records:
        for record in records[1]:  # Access the list of records
            try:
                result_value = float(record["result_value"])  # Convert result value to float
                min_test_value = min(min_test_value, result_value)  # Update minimum test value
                max_test_value = max(max_test_value, result_value)  # Update maximum test value
                total_test_value += result_value  # Accumulate total test value
                test_count += 1  # Increment test count

                # Turnaround times
                result_date_time = datetime.strptime(record["result_date_time"], "%Y-%m-%d %H:%M")  # Parse result datetime
                test_date = datetime.strptime(record["test_date"], "%Y-%m-%d %H:%M")  # Parse test datetime
                turnaround_time = result_date_time - test_date  # Calculate turnaround time

                min_turnaround_time = min(min_turnaround_time, turnaround_time)  # Update minimum turnaround time
                max_turnaround_time = max(max_turnaround_time, turnaround_time)  # Update maximum turnaround time
                total_turnaround_time += turnaround_time  # Accumulate total turnaround time
                turnaround_count += 1  # Increment turnaround count

            except (KeyError, ValueError) as e:
                print(f"Error processing record: {e}")
                continue  # Skip records with errors

        # calculate average test value
        if test_count > 0:
            average_test_value = total_test_value / test_count
        else:
            average_test_value = 0

        # calculate average turnaround time
        if turnaround_count > 0:
            average_turnaround_time = total_turnaround_time / turnaround_count
        else:
            average_turnaround_time = timedelta()

    # Print summary
    print("Test Value Statistics:")
    print(f"Minimum Test Value: {min_test_value}")
    print(f"Maximum Test Value: {max_test_value}")
    print(f"Average Test Value: {average_test_value:.2f}")

    print("\nTurnaround Time Statistics:")
    print(f"Minimum Turnaround Time: {min_turnaround_time}")
    print(f"Maximum Turnaround Time: {max_turnaround_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")


def import_medicalRecords():
    try:
        fo = open("medicalRecord.txt", "r")  # open the file for reading
        for line in fo:
            line = line.strip()  # clean the line before splitting (before and after line)
            seperateID = line.split(":", 1)  # split by the first colon to separate ID from record
            patientID = seperateID[0]
            splits = seperateID[1].split(",")  # split the record part by commas

            # check if there are enough fields in the line
            if len(splits) < 5:
                continue  # skip invalid lines

            testName = splits[0].strip()  # extract and clean the test name
            testDate = splits[1].strip()  # extract and clean the test date
            value = splits[2].strip()  # extract and clean the result value
            unit = splits[3].strip()  # extract and clean the result unit
            status = splits[4].strip()  # extract and clean the result status

            # check if there is an optional result time field
            if len(splits) > 5:
                resultTime = splits[5].strip()  # extract and clean the result time
            else:
                resultTime = ""  # set to an empty string if not present

            # create a dictionary for the record details
            if status == "completed":
             recordDetails = {
                'test_name': testName,
                'test_date': testDate,
                'result_value': value,
                'result_unit': unit,
                'result_status': status,
                'result_date_time': resultTime
             }
            if status == "pending" or status == "reviewed":
                recordDetails = {
                    'test_name': testName,
                    'test_date': testDate,
                    'result_value': value,
                    'result_unit': unit,
                    'result_status': status,
                }

            # add the record to the dictionary under the patient_id
            if patientID in patients:
                patients[patientID].append(recordDetails)

            else:
                patients[patientID] = [recordDetails]

        fo.close()  # close the file

    except FileNotFoundError:  # handle file not found error
        print("file medicalRecord.txt was not found.")

    return recordDetails  # return the last record details (this may not be necessary)

import_medicalRecords()


def import_medicalRecords_csv():
    patients.clear()
    try:
        fo = open("medicalRecord.csv", "r")  # open the file for reading
        for line in fo:
            line = line.strip()  # clean the line before splitting (before and after line)
            seperateID = line.split(":", 1)  # split by the first colon to separate ID from record
            patientID = seperateID[0]
            splits = seperateID[1].split(",")  # split the record part by commas

            # check if there are enough fields in the line
            if len(splits) < 5:
                continue  # skip invalid lines

            testName = splits[0].strip()  # extract and clean the test name
            testDate = splits[1].strip()  # extract and clean the test date
            value = splits[2].strip()  # extract and clean the result value
            unit = splits[3].strip()  # extract and clean the result unit
            status = splits[4].strip()  # extract and clean the result status

            # check if there is an optional result time field
            if len(splits) > 5:
                resultTime = splits[5].strip()  # extract and clean the result time
            else:
                resultTime = ""  # set to an empty string if not present

            # create a dictionary for the record details
            if status == "completed":
             recordDetails = {
                'test_name': testName,
                'test_date': testDate,
                'result_value': value,
                'result_unit': unit,
                'result_status': status,
                'result_date_time': resultTime
             }
            if status == "pending" or status == "reviewed":
                recordDetails = {
                    'test_name': testName,
                    'test_date': testDate,
                    'result_value': value,
                    'result_unit': unit,
                    'result_status': status,
                }

            # add the record to the dictionary under the patient_id
            if patientID in patients:
                patients[patientID].append(recordDetails)

            else:
                patients[patientID] = [recordDetails]

        fo.close()  # close the file

    except FileNotFoundError:  # handle file not found error
        print("file medicalRecord.txt was not found.")


def Export_medicalRecords_csv():
    try:
        with open("medicalRecord.csv", "w") as fo:
            for patient_id, tests in patients.items():  # Iterating over all patients and their tests in patients dictionary
                for test in tests:  # Iterating over every test of each patient
                    line = (f"{patient_id}, {test['test_name']}, {test['test_date']}, "
                            f"{test['result_value']}, {test['result_unit']}, "
                            f"{test['result_status']}, {test.get('result_date_time', '')}\n")
                    fo.write(line)
    except IOError:
        print("Error: Not able to write to medicalRecord.csv.")





def update_date():
    # Read the file and get all the lines
    with open("medicalRecord.txt", 'r') as file:
        lines = file.readlines()

    # Iterate over each line in the file
    for i, line in enumerate(lines):
        tday = 0
        thour = 0
        tmin = 0

        part1 = line.strip().split(",")

        # Ensure the first part has at least 2 elements
        if len(part1) < 2:
            print(f"Skipping line due to insufficient data: {line.strip()}")
            continue

        id_part = part1[0].split(":")
        if len(id_part) < 2:
            print(f"Skipping line due to missing ID or name: {line.strip()}")
            continue

        id = int(id_part[0].strip())
        name = id_part[1].strip().split()[0]

        # Ensure the date part has both date and time
        date_time_part = part1[1].strip().split()
        if len(date_time_part) < 2:
            print(f"Skipping line due to missing date or time: {line.strip()}")
            continue

        date_part = date_time_part[0].split("-")
        if len(date_part) < 2:
            print(f"Skipping line due to incomplete date: {line.strip()}")
            continue

        year = int(date_part[0])
        month = int(date_part[1])
        day = int(date_part[2]) if len(date_part) > 2 else 1  # Default day to 1 if missing

        time_part = date_time_part[1].split(":")
        if len(time_part) < 2:
            print(f"Skipping line due to incomplete time: {line.strip()}")
            continue

        hour = int(time_part[0])
        minute = int(time_part[1])

        testVal = float(part1[2].strip())
        unit = part1[3].strip().split()[0]
        status = part1[4].strip().split()[0]

        for test in medicalTestList:
            if name == test.testName:
                tday = test.day
                thour = test.hour
                tmin = test.minute
                break

        listUpdate = DateExpired(year, month, day, hour, minute, tday, thour, tmin)

        if listUpdate[0] == "completed" and (status == "pending" or status == "reviewed"):
            lines[i] = f"{id}: {name}, {year}-{month}-{day} {hour}:{minute}, {testVal}, {unit}, completed, {listUpdate[1]}\n"

    with open("medicalRecord.txt", "w") as file:
        file.writelines(lines)

update_date()


def menu():  # this is menu display the choices
    print("\nPlease choose an option.")
    print("1. Add a new medical test.")
    print("2. Add a new medical Record.")
    print("3. Update medical tests in the medicalTest file.")
    print("4. Update patient records.")
    print("5. Filter medical tests.")
    print("6. Generate textual summary reports.")
    print("7. Export medical records to a comma separated file.")
    print("8. Import medical records from a comma separated file.")
    print("9. Exit menu\n")


medicalRecordList = []
i = 0
importflag = 0
print("Welcome to Our Medical Test Management System!")
while i != -1:
    menu()
    try:
        choice = int(input("Select an option (1-7): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 7.")  # catches if user enters a char
        continue
    if choice == 1:
        addNewMedicalTest()
    elif choice == 2:
        addNewMedicalRecord()
    elif choice == 3:
        update_medical_test()
    elif choice == 4:
        update_patient_record()
    elif choice == 5:
        filters()
    elif choice == 6:
        generate_summary_reports(filtered_records)
        pass
    elif choice == 7:
        Export_medicalRecords_csv()
        print("Exporting of file was successful!")
    elif choice == 8:
        import_medicalRecords_csv()
        print_all_patients()
        print("Importing of file was successful!")
        importflag = 1
        pass
    elif choice == 9:
        i = -1
        print("Thank you for using our system! Goodbye.")
    else:
        print("Invalid number! Please select a valid option (1-7).")

