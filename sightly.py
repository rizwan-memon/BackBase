from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

class SightlyTest(unittest.TestCase):

    selectors = {
        "main": {
            "path": "#__layout > div > div > div.login-area",
        },
        "users": {
            "path": "[class='row']",
        },
        "email": {
            "path": "input[type=text]",
            "text": "nick@sightly.com",
        },
        "password": {
            "path": "input[type=password]",
            "text": "a",
        },
        "login_button": {
            "path": "#__layout > div > div > div.login-area > div.login-box-right > button",
        },
        "reports": {
            "button": "#header-reports",
            "order_name": "#reports-list-main-content > div.table > div.table-header > div.order-name-col.th",
            "first_report": "#reports-list-main-content > div.table > div.table-body > div:nth-child(2) > div.td.checkbox-col > input",
            "create_report_button": "#reports-list-main-content > div.search-container > div:nth-child(4) > button",
        },
        "report_generator": {
            "main_page": "#reports-list-main-content > div.reports-overlay",
            "performance_detailed_report": "#performanceDetailReportOption > div > div:nth-child(1) > input[type=radio]",
            "grouping_path": "#inputGroupSummaryContainer > div > div:nth-child(1) > div.input-container > select",
            "grouping_text": "campaign",
            "cost_basis_path": "#inputGroupSummaryContainer > div > div:nth-child(2) > div.input-container > select",
            "cost_basis_text": "all",
            "granularity_path": "#inputGroupSummaryContainer > div > div:nth-child(3) > div.input-container > select",
            "granularity_text": "summary",
            "additional_columns_path": "#inputGroupSummaryContainer > div > div:nth-child(4) > div.input-container > select",
            "additional_columns_text": "none",
            "time_period_path": "#inputGroupSummaryContainer > div > div:nth-child(5) > div.input-container > select",
            "time_period_text": "all time",
            "run_report_button": "#modal-container > div.modal-body > div.buttons-container > button",
        },
        "report_results": {
            'start_date': '5/7/20',
            'end_date': '6/1/20',
            'cid': [9613603164],
            'campaign_name': 'Chmura Orthodontics',
            'placement_name': 'AMG - Chmura Ortho May 2020',
            'placement_id': 'B524B795-8FD8-4F41-A916-F0C7A51D4A4A',
            'impressions': '42,973',
            'views': '21,338',
            'view_rate': '49.65%',
            'clicks': [45],
            'ctr': '0.10%',
            'cpv': '$0.03 ',
            'cpm': '$14.84 ',
            'cost': '$637.76 ',
            'video_played_to_25%': '33,569',
            'video_played_to_50%': '26,354',
            'video_played_to_75%': '23,089',
            'video_played_to_100%': '20,858',
        }
    }

    @classmethod
    def setUpClass(cls):
        main_path = cls.selectors['main']['path']

        cls.driver = webdriver.Chrome(executable_path="/Users/rizwan.memon/Documents/driver/chromedriver 3")

        url = 'https://staging-newtargetview.sightly.com/'

        cls.driver.get(f"{url}")

        timeout = 5
        try:
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, f'{main_path}'))
            WebDriverWait(cls.driver, timeout).until(element_present)
        except TimeoutError:
            print('Page timed out trying to load')

    def test_01_verify_user_can_login_and_run_reports(self):
        email_path = self.selectors['email']['path']
        email_text = self.selectors['email']['text']
        password_path = self.selectors['password']['path']
        password_text = self.selectors['password']['text']
        login_button = self.selectors['login_button']['path']

        reports_path = self.selectors['reports']['button']
        order_name_path = self.selectors['reports']['order_name']
        first_report = self.selectors['reports']['first_report']
        create_report_button = self.selectors['reports']['create_report_button']

        report_generator_page = self.selectors['report_generator']['main_page']
        performance_detailed_report_button = self.selectors['report_generator']['performance_detailed_report']

        grouping_path = self.selectors['report_generator']['grouping_path']
        grouping_text = self.selectors['report_generator']['grouping_text']
        cost_basis_path = self.selectors['report_generator']['cost_basis_path']
        cost_basis_text = self.selectors['report_generator']['cost_basis_text']
        granularity_path = self.selectors['report_generator']['granularity_path']
        granularity_text = self.selectors['report_generator']['granularity_text']
        additional_columns_path = self.selectors['report_generator']['additional_columns_path']
        additional_columns_text = self.selectors['report_generator']['additional_columns_text']
        time_period_path = self.selectors['report_generator']['time_period_path']
        time_period_text = self.selectors['report_generator']['time_period_text']
        run_report_button = self.selectors['report_generator']['run_report_button']

        timeout = 5

        self.driver.find_element_by_css_selector(f'{email_path}').send_keys(f'{email_text}')
        self.driver.find_element_by_css_selector(f'{password_path}').send_keys(f'{password_text}')
        self.driver.find_element_by_css_selector(f'{login_button}').click()

        try:
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, f'{reports_path}'))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutError:
            print('Page timed out trying to load')

        time.sleep(1)
        self.driver.find_element_by_css_selector(f'{reports_path}').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(f'{order_name_path}').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(f'{first_report}').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(f'{create_report_button}').click()
        time.sleep(2)

        try:
            element_present = EC.presence_of_element_located((By.CSS_SELECTOR, f'{report_generator_page}'))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutError:
            print('Page timed out trying to load')

        self.driver.find_element_by_css_selector(f'{performance_detailed_report_button}').click()
        self.driver.find_element_by_css_selector(f'{grouping_path}').send_keys(f'{grouping_text}')
        time.sleep(1)
        self.driver.find_element_by_css_selector(f'{cost_basis_path}').send_keys(f'{cost_basis_text}')
        time.sleep(1)
        self.driver.find_element_by_css_selector(f'{granularity_path}').send_keys(f'{granularity_text}')
        time.sleep(1)
        self.driver.find_element_by_css_selector(f'{additional_columns_path}').send_keys(f'{additional_columns_text}')
        time.sleep(1)
        self.driver.find_element_by_css_selector(f'{time_period_path}').send_keys(f'{time_period_text}')
        time.sleep(1)
        self.driver.find_element_by_css_selector(f'{run_report_button}').click()

    def test_02_verify_reports_values(self):
        location = ('downloaded_reports.csv')

        data = pd.read_csv(location)
        data_dict = {col: list(data[col]) for col in data.columns}

        start_date = ''.join(data_dict['Start Date'])
        end_date = ''.join(data_dict['End Date'])
        cid = list(map(int, (data_dict['CID'])))
        campaign_name = ''.join(data_dict['Campaign Name'])
        placement_name = ''.join(data_dict['Placement Name'])
        placement_id = ''.join(data_dict['Placement ID'])
        impressions = ''.join(data_dict['Impressions'])
        views = ''.join(data_dict['Views'])
        view_rate = ''.join(data_dict['View Rate'])
        clicks = list(map(int, (data_dict['Clicks'])))
        ctr = ''.join(data_dict['CTR'])
        cpv = ''.join(data_dict['CPV'])
        cmp = ''.join(data_dict['CPM'])
        cost = ''.join(data_dict['Cost'])
        video_played_to_25 = ''.join(data_dict['Video Played To 25%'])
        video_played_to_50 = ''.join(data_dict['Video Played To 50%'])
        video_played_to_75 = ''.join(data_dict['Video Played To 75%'])
        video_played_to_100 = ''.join(data_dict['Video Played To 100%'])

        assert start_date == self.selectors['report_results']['start_date']
        assert end_date == self.selectors['report_results']['end_date']
        assert cid == self.selectors['report_results']['cid']
        assert campaign_name == self.selectors['report_results']['campaign_name']
        assert placement_name == self.selectors['report_results']['placement_name']
        assert placement_id == self.selectors['report_results']['placement_id']
        assert impressions == self.selectors['report_results']['impressions']
        assert views == self.selectors['report_results']['views']
        assert view_rate == self.selectors['report_results']['view_rate']
        assert clicks == self.selectors['report_results']['clicks']
        assert ctr == self.selectors['report_results']['ctr']
        assert cpv == self.selectors['report_results']['cpv']
        assert cmp == self.selectors['report_results']['cpm']
        assert cost == self.selectors['report_results']['cost']
        assert video_played_to_25 == self.selectors['report_results']['video_played_to_25%']
        assert video_played_to_50 == self.selectors['report_results']['video_played_to_50%']
        assert video_played_to_75 == self.selectors['report_results']['video_played_to_75%']
        assert video_played_to_100 == self.selectors['report_results']['video_played_to_100%']

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == 'main':
    unittest.main()