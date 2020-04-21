from selenium import webdriver
from time import sleep
from secrets import psw


class InstaBot:
    def __init__(self,username, psw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(10)    
        self.driver.find_element_by_xpath('//input[@name=\"username\"]')\
            .send_keys(username)
        self.driver.find_element_by_xpath('//input[@name=\"password\"]')\
            .send_keys(psw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click() 
        sleep(10)
        #sleep needs to take place in order to be able to load the page 
        #and to targed the elements of the new page loaded
        self.driver.find_element_by_xpath('//button[text()="Not Now"]')\
            .click()
        sleep(10)


    def get_unfollowers(self):

        sleep(5)
        self.driver.find_element_by_xpath('//a[contains(@href,"/{}")]'.format(self.username))\
            .click()

        sleep(10)
        self.driver.find_element_by_xpath('//a[contains(@href,"/following")]')\
            .click()
        following = self._get_names()
        self.driver.find_element_by_xpath('//a[contains(@href,"/followers")]')\
            .click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)




    def _get_names(self):
        sleep(5)
        scroll_box  = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
        last_ht, ht = 0 , 1 
        while last_ht != ht: 
            last_ht  = ht
            sleep(5)
            ht=self.driver.execute_script("""arguments[0].scrollTo(0,arguments[0].scrollHeight)
                return arguments[0].scrollHeight;
                """, scroll_box) 
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
        return names

my_bot = InstaBot("noahgiesel", psw)
my_bot.get_unfollowers()