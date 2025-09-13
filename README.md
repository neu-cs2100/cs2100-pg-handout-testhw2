> [!CAUTION]
> This repository is for viewing only. Do not work on the assignment using this repository -- the actual course assignments will be provided to you via Pawtograder.

# Homework 2: Testing 311 Service Request Processing

## Learning Outcomes

- Debug existing code
- Write tests to catch bugs in unseen code
- Practice adhering to the level of visibility set in existing code for attributes and properties
- Use Generic type annotations
- Consider the privacy of people in a dataset

## Overview

Homework 2 is to write tests for two of the classes that you will implement in Homework 3.
We have (hidden) implementations of the classes in the autograder for Homework 2, but there are bugs in them.
Your task is to write tests that catch those bugs.

Homework 3 will involve analyzing a dataset of 311 service request data to explore how municipal services are distributed across different neighborhoods and demographics. 311 systems allow residents to report non-emergency issues like potholes, broken streetlights, noise complaints, and other quality-of-life concerns.
You will analyze one of these two datasets:
- Oakland/San Francisco: https://data.sfgov.org/City-Infrastructure/311-Cases/vw6y-z8j6/data_preview
- Boston: https://data.boston.gov/dataset/311-service-requests

You will write tests for two classes: `DataLoader` and `Sorting`.

These classes are designed to analyze large datasets. It is impractical for tests to also involve large datasets, so there are sample datasets in `example_CSVs`. You should use these smaller datasets to implement your tests.

## Your Tasks

### Part 1: Look at the classes

You will write tests for two classes: `DataLoader` and `Sorting`. The stub implementations for these classes are provided in `data_loader.py` and `sorting.py`, respectively.
Look at these two classes and take note of cases that would be good to test.

Remember: when testing, we want to consider:
- the "happy path" with valid input
- any invalid inputs
- any edge cases (almost invalid but still valid)


You may ignore any linting errors in the src files for this assignment: the autograder will only check for linting errors in your test files, as you will only be writing tests in this assignment, and the (unimplemented) src files are provided only as a specification to write tests. 


### Part 2: Test DataLoader

There are some test method stubs provided in `test_data_loader.py`. Implement all of the required tests.
Remember: you are expected to use the sample datasets in `example_CSVs`. Do not rename/change any of the CSVs 
in this folder, as the autograder will only work with these particular CSVs. These should be sufficient to test all edge cases required for this assignment.

### Part 3: Test CaseSorter

Unlike `TestDataLoader`, `TestCaseSorter` does not contain test method stubs. Your task is to come up with the test cases.

The autograder contains a few implementations of `CaseSorter`, each with a different bug. It will run your tests on our buggy implementations, and calculate how many of the bugs are caught by your tests.

Note: You should also write tests to catch the correct exception type for each method for invalid inputs. For some bugs, since DataLoader already ensures the required columns are present, you may have to manually drop columns after loading the dataframe to test that the CaseSorter module is indeed raising errors as expected for missing columns, or else you will just be catching the exceptions raised in DataLoader, not in CaseSorter.

Also, for testing handling of non-numeric values, you may use 311_Cases_non_numeric.csv, which has a non-numeric value in one of the cases for the days_open column. 

### Part 4: Summary.md

Answer all of the questions in `Summary.md`.

## Running Tests
In this assignment, you will not be provided or required to complete implementations, so you will not be required to run tests locally.

You may however run `python3 test_runner.py` to make sure your tests are being detected correctly (even though they will all fail due to unimplemented classes/methods)


## Generating Coverage reports
Again, as with testing, you will not have the src code, so there isn't really any point in generating/checking the coverage reports, you may ignore them for this assignment.

## Grading Rubric
- Implementing the test stubs in `TestDataLoader` (30%)
- Catching our hidden bugs using `TestCaseSorter` (35%)
- Summary.md (35%)

Good luck!
