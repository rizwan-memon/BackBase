import unittest
from backbase import BackBaseTest
import HtmlTestRunner
import os

back_base_test = unittest.TestLoader().loadTestsFromTestCase(BackBaseTest)

test_suite = unittest.TestSuite([back_base_test])

result_dir = os.getcwd()

outfile = open(result_dir + "\BackbaseAutomation.html", "w")

runner = HtmlTestRunner.HTMLTestRunner(stream=outfile)

runner.run(test_suite)