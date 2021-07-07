import unittest
from sightly import SightlyTest
import HtmlTestRunner
import os

sightly_test = unittest.TestLoader().loadTestsFromTestCase(SightlyTest)

test_suite = unittest.TestSuite([sightly_test])

result_dir = os.getcwd()

outfile = open(result_dir + "\SightlyAutomation.html", "w")

runner = HtmlTestRunner.HTMLTestRunner(stream=outfile)

runner.run(test_suite)