# Medical Test Management System

## Objective
The Medical Test Management System is designed to efficiently store, manage, and retrieve medical test data for individual patients. This system functions as a basic patient record management system, focusing on test results. Key features include:

- Adding new test results
- Updating existing records
- Deleting outdated or incorrect entries
- Retrieving specific test results based on patient ID or test type

This project is built using object-oriented Python code, defining a class for patients with appropriate attributes and methods, and storing all patients in a dictionary indexed by patient ID.

## File Format
Medical test records are stored in a text file named `medicalRecord.txt`. Each line in this file represents a single medical test and includes the following fields:

- **Patient ID** (integer: 7 digits)
- **Test name** (string - consider a fixed length)
- **Test date and time** (format: YYYY-MM-DD hh:mm)
- **Numeric result value**
- **Results unit**
- **Status** (string - fixed length, e.g., "Pending", "Completed", "Reviewed")
- **Results date and time** (format: YYYY-MM-DD hh:mm) only if the status is "Completed"

## System Functionality
The system provides a text-based menu allowing users to:

- Add a new medical test type and save it in `medicalTest.txt`.
- Add a new medical test record with validation for input data.
- Update patient records, including all fields.
- Update medical tests in the `medicalTest.txt` file.
- Filter medical tests based on:
  - Patient ID
  - Test Name
  - Abnormal tests
  - Test added within a specific date range
  - Test status
  - Turnaround time within a specified range
- Generate textual summary reports with:
  - Minimum, maximum, and average test values
  - Minimum, maximum, and average turnaround times
- Export and import medical records to/from a comma-separated file.

## Error Handling and Data Validation
The system includes:

- Error handling for invalid file names and searches for non-existent tests or patients.
- Data validation to ensure proper data types (e.g., integers for IDs, valid dates) and to handle potential errors.
