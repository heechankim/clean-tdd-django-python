from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(service=Service('./chromedriver'), options=options)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # chan는 멋진 작업 목록 온라인 앱이 나왔다는 소식을 듣고
        # 해당 웹 사이트를 확인하러 간다
        self.browser.get('http://localhost:8000')

        # 웹 페이지 타이틀과 헤더가 'To-DO'를 표시하고 있다.
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # 그는 바로 작업을 추가하기로 한다.
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
        )

        # "공작깃털 사기"라고 텍스트 상자에 입력한다.
        # (찬의 취미는 날치 잡이용 그물을 만드는 것이다)
        inputbox.send_keys('공작깃털 사기')

        # 엔터키를 치면 페이지가 갱신되고 작업 목록에
        # "1: 공작깃털 사기" 아이템이 추가된다.
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        # self.assertTrue(
        #     any(row.text == '1: 공작깃털 사기' for row in rows),
        #     "신규 작업 아이템이 테이블에 표시되지 않는다. -- 해당 텍스트:\n$s" % (
        #         table.text
        #     ),
        # )
        # 위의 assertTrue 를 한 줄의 assertIn 으로 리팩터링
        self.assertIn('1: 공작깃털 사기', [row.text for row in rows])

        # 추가 아이템을 입력할 수 있는 여분의 텍스트 상자가 존재한다.
        # 다시 "공작깃털을 이용해서 그물 만들기"라고 입력한다 (찬은 매우 체계적인 사람이다)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('공작깃털을 이용해서 그물 만들기')
        inputbox.send_keys(Keys.ENTER)

        # 페이지는 다시 갱신되고, 두 개 아이템이 목록에 보인다.
        self.check_for_row_in_list_table('2: 공작깃털을 이용해서 그물 만들기')
        self.check_for_row_in_list_table('1: 공작깃털 사기')

        # 찬은 사이트가 입력한 목록을 저장하고 있는지 궁금하다.
        # 사이트는 그를 위한 특적 URL을 생성해준다.
        # 이때 URL에 대한 설명도 함께 제공된다.
        self.fail('Finish the test!')

        # 해당 URL에 접속하면 그가 만든 작업목록이 그대로 있는 것을 확인할 수 있다.

        # 만족하고 잠자리에 든다.

if __name__ == '__main__':
    unittest.main(warnings='ignore')