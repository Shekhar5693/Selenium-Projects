from webdriver_helpers import *

class Setup:
	def __init__(self, driver:WebDriver, url):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)
		self.url = url

class UserAccount(Setup):
    URL = "http://localhost/AD-event-management-main/HomePage/rishabh/"
	
    def __init__(self, driver:WebDriver):
        super().__init__(driver, self.URL)

# Open the project website
    def project_site(self):
        self.driver.get(UserAccount.URL)

# Navigating to the client signup form
    def client_signup_form(self):
        sign_up_locator = By.PARTIAL_LINK_TEXT, "SignUp"
        self.driver.find_element(*sign_up_locator).click()

        client_locator = By.CSS_SELECTOR,".ghost[id='signUp']"
        self.driver.find_element(*client_locator).click()

        client_signup_button_locator = By.CSS_SELECTOR,"button[formaction='signup_client.php']"
        self.wait.until(expected.element_to_be_clickable(client_signup_button_locator)).click()

# Filling the account form
    def enter_name(self,fullname):
        name_field_locator = By.CSS_SELECTOR, "input[name='name']"
        self.driver.find_element(*name_field_locator).send_keys(fullname)

    def enter_username(self,username):
        username_field_locator = By.CSS_SELECTOR, "input[name='username']"
        self.driver.find_element(*username_field_locator).send_keys(username)

    def enter_email(self,email):
        email_field_locator = By.CSS_SELECTOR, "input[name='email']"
        self.driver.find_element(*email_field_locator).send_keys(email)

    def enter_password(self,password):
        password_field_locator = By.CSS_SELECTOR, "input[name='password']"
        self.driver.find_element(*password_field_locator).send_keys(password)

    def enter_con_password(self,password):
        conPwd_field_locator = By.CSS_SELECTOR, "input[name='confirm_password']"
        self.driver.find_element(*conPwd_field_locator).send_keys(password)

    def enter_number(self,number):
        number_field_locator = By.CSS_SELECTOR, "input[name='mobile_no']"
        self.driver.find_element(*number_field_locator).send_keys(number)

    def click_submit_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
        submit_button_locator = By.CSS_SELECTOR, "button[value='Submit']"
        self.driver.find_element(*submit_button_locator).click()

    def created(self):
        return self.driver.title

    def log_in(self, username, password):
        username_locator = By.CSS_SELECTOR, "input[name='username']"
        password_locator = By.CSS_SELECTOR, "input[name='password']"
        submit_locator = By.CSS_SELECTOR, "button[value='Submit']"
        self.driver.find_element(*username_locator).send_keys(username)
        self.driver.find_element(*password_locator).send_keys(password)
        self.driver.find_element(*submit_locator).click()

    def logged_in(self):
        check = By.PARTIAL_LINK_TEXT, "Client Dashboard"
        return self.driver.find_element(*check).text
        

