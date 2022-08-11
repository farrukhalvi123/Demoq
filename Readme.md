For this Test I have used Page Object Model framework Along with BDD. 

There are 4 feature files in total with 14 Scenarios. 

There are three set of Directories.
Features: Containing all the test scenarios in Gherkin 

Steps: Containing all the Steps to run those scenarios in feature files

Pages: Contains files with all the elements and their methods. 

To run this test. Following steps are mandatory.
Download Pycharm with Python 3.9 Interpreter
Selenium 4.1 (Go to terminal at the bottom and type in command pip install ./ requirements.txt)

requirements.txt file contains all the packages needed to run these tests.

To run all the test and generate report on behave you can use the following command
** behave features **
"Will run all the tests sequentially"

To run individual feature file.
** behave "file_name".features 

or you can directly run individual tests or individual file from the file itself by click on Play button.