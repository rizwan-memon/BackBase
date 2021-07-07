# BackBase

Preconditions to run test:

1. You would need to install Chrome Webdriver(or any webdriver).

2. You also need to update executable path(line 76), where your driver is stored.

3. You need to install latest version of python(this code with only work on python 3.7 or higher)

4. Following packages also need to be installed: Selenium, Pandas, unittest, HtmlTestRunner

5. You would need pass the following line on your terminal to run the test: python test_sightly.py.

6. I put the downloaded report on the root file, you can post it from anywhere. The file needs to be csv and path needs to be updated(line 158)

7. I have added sleep time to generate reports only because webdriver wait was not working. I had to slow down the execution in order to run the test.