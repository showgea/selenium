import os
import time
import unittest
from HTMLTestRunner_cn import HTMLTestRunner

case_path = os.path.dirname(os.path.realpath(__file__))
current_date = time.strftime("%Y-%m-%d", time.localtime())
report_name = 'report-' + current_date + '.html'
report_path = os.path.dirname(os.path.realpath(__file__)) + '\\result\\' + report_name


discovery = unittest.defaultTestLoader.discover(start_dir=case_path,
                                                pattern="test*.py",
                                                top_level_dir=None)

runner = HTMLTestRunner(stream=open(report_path, 'wb'),
                        verbosity=2,
                        title="This is a AutoTest Title",
                        description="This is a AutoTest Description",
                        retry=0,
                        save_last_try=False)
runner.run(discovery)
