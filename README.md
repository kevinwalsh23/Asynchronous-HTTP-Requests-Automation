# HTTP-Requests-Automation

This program automates the process of testing the http status of each tactics' json pixel url. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

In order to run this program, you must download a version of python. After installing python, you must also install the dependent libraries that are imported.

```
Python
Libraries:
requests
pandas
re
time
csv
```
Install python from python.org.
For Libraries, go to terminal, and type the following in the command line:
pip install {library}

If permissions issue exists, add --user to end of command.


## Running the tests

Unittest.py is the unit test for this program. This is testing whether the program can recognize parts of the json url
to ensure that we are parsing the data correctly. The second function tested tests for status codes, and returns correct and intentionally incorrect status codes for different examples.

To run the unittest, from the command line run python unittest.py.


### And coding style tests

Python used for the build.

## Deployment

To deploy this program, you must have the tactic_id csv saved to the same folder that you have triplelift.py saved to. 

Once confirmed, change to this directory from the command line (cd ~/path/to/folder/).

Next, run 'python triplelift.py' from the command line.

The result of this program will print in the terminal the number of fails, successes, blanks, and exceptions that are returned. Additionally, this file also write the failures and excemptions to a csv file, and also writes the number of success to a csv file.

## Authors

* **Kevin Walsh** - *Initial work* -(https://github.com/kevinwalsh23)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.
