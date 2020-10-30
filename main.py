from time import sleep
from selenium import webdriver
from creds import username, pw, baseurl

'''
Important classes - 
1. Like button - fr66n
2. Next post arrow - coreSpriteRightPaginationArrow
3. First post on the profile - _9AhH0
'''


class insta_bot:
    def __init__(self, username, password):
        self.username = username
        self.password = pw
        self.driver = webdriver.Chrome()

    def closeBrowser(self):
        self.driver.close()

    def maximizeBrowser(self):
        self.driver.maximize_window()

    def login(self):
        driver = self.driver
        driver.get(baseurl+"accounts/login/")
        sleep(2)
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_name('password').send_keys(pw)
        sleep(3)
        driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button/div').click()
        sleep(3)
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()
        sleep(2)
        driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()

    def hashChecker(self, hashtag):
        driver = self.driver
        driver.get(baseurl+"explore/tags/"+hashtag+"/")
        sleep(3)

    def profileChecker(self, profile):
        driver = self.driver
        driver.get(baseurl+profile+"/")
        sleep(3)

    def post_liker(self, count):
        driver = self.driver
        driver.find_element_by_class_name('v1Nh3').click()

        for i in range(1, count):
            sleep(1)
            # class for like button
            '''color = driver.find_element_by_class_name(
                'fr66n').get_attribute("fill")
            if color == '#ed4956':
                continue
            else:'''
            driver.find_element_by_class_name('fr66n').click()
            # class for next arrow on post
            driver.find_element_by_class_name(
                'coreSpriteRightPaginationArrow').click()

    def first_picture(self):
        driver = self.driver
        driver.find_element_by_class_name("_9AhH0").click()

    def like_pic(self):
        sleep(4)
        driver = self.driver
        driver.find_element_by_class_name('fr66n').click()

    def next_pic(self):
        sleep(2)
        driver = self.driver
        driver.find_element_by_class_name(
            'coreSpriteRightPaginationArrow')

    '''def continue_liking(self):
        sleep(2)
        while(True):
            if self.next_pic() != False:
                driver = self.driver
                driver.find_element_by_class_name(
                    'coreSpriteRightPaginationArrow').click()
                sleep(2)

                self.like_pic()
                sleep(2)
            else:
                break

        self.profileChecker('rohan__kamath')'''

    def liking_loop(self):
        sleep(2)
        try:
            while(True):
                if self.next_pic() != False:
                    driver = self.driver
                    driver.find_element_by_class_name(
                        'coreSpriteRightPaginationArrow').click()
                    sleep(2)

                    self.like_pic()
                    sleep(2)
        except:
            self.profileChecker('add profile to like here')


kamath_kool = insta_bot(username, pw)
kamath_kool.login()
kamath_kool.profileChecker('add profile to like here')
kamath_kool.first_picture()
kamath_kool.like_pic()
kamath_kool.next_pic()
kamath_kool.liking_loop()
# kamath_kool.hashChecker('add hashtag here')
# kamath_kool.post_liker(add integer amount here)
