from selenium import webdriver

#def test_login():
driver = webdriver.Chrome(executable_path="C:\\Users\\Rakshith Yenadka\\Downloads\\chromedriver_win32\\chromedriver.exe")
#driver.implicitly_wait(30)
driver.get("http://localhost:1111/login")
driver.find_element_by_id("j_username").send_keys("madhuri")
driver.find_element_by_name("j_password").send_keys("rakmad035*")
driver.find_element_by_name("Submit").click()
driver.find_element_by_xpath("//b[text()='log out']").click()