from selenium import webdriver

class keepfaceTest:

        
    def __init__(self, url, email, password):
        self.driver = webdriver.Chrome()
        self.url = url
        self.email = email
        self.password = password        
        self.driver.get(url)

    def login(self):
        btn = self.driver.find_element_by_name('useremail')
        btn.clear()
        btn.send_keys(self.email)
        btn = self.driver.find_element_by_name('userpassword')
        btn.clear()
        btn.send_keys(self.password)
        btn.submit()
        btn = self.driver.find_element_by_class_name('profilebox')
        btn.click()
        btn = self.driver.find_element_by_link_text('AZ')
        btn.click()

    def testCampaigns(self):
        btn = self.driver.find_element_by_link_text('Kampaniyalar')
        btn.click()
        btn = self.driver.find_element_by_link_text('ƏTRAFLI BAX')
        btn.click()                        

    def testSendingProposal(self):
        btn = self.driver.find_element_by_link_text('Təklif Göndər')
        btn.click()
        btn = self.driver.find_element_by_class_name('bootstrap-select')
        print(btn.text)

    def favList(self):
        btn = self.driver.find_element_by_link_text('Sevimli Brendlərim')
        btn.click()
        btn = self.driver.find_element_by_class_name('right-left')
        btn.click()
    
    def myChannels(self):
        btn = self.driver.find_element_by_link_text('Kanallarım')
        btn.click()

    def profile(self):
        btn = self.driver.find_element_by_link_text('Profil')
        btn.click()

    def payments(self):
        btn = self.driver.find_element_by_link_text('Ödənişlər').click()

    def settings(self):
        btn = self.driver.find_element_by_link_text('Tənzimləmələr').click()

test1 = keepfaceTest('https://az.keepface.com/az/user/login/', '', '')


