from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime

#checking for time of day
dt = datetime.datetime.now()
hour = dt.hour
dayname = dt.strftime("%A")
monthday = dt.day  #Day of the month
msarydate = 01 #Date of Monthsary
msarydays = msarydate - monthday   #Days Left till next Monthsary
year = dt.year
rs = datetime.date(2020, 01, 01)  #Date when the relation started
td = datetime.date.today() - rs   #Number of Days Passed Since
rsdays = td.days  #Formats it properly into days-USE THIS

#text composition in sample formats, please edit these appropriately.
morning_text = "<text> today is {} <text>. Our love is now {} Days old. <text>   -piddubot".format(dayname, rsdays)
afternoon_text = "<text>    -piddubot"
evening_text = "<text> Monthsary is coming up in {} days    -piddubot".format(msarydays)
night_text = "<text>    -piddubot"

#selecting message
if    5 <hour < 12:
        send_text = morning_text
elif  12 <= hour < 16:
        send_text = afternoon_text
elif  16 <= hour < 19:
        send_text = evening_text    
else:
        send_text = night_text


#getpage
options = FirefoxOptions()
#options.add_argument("--headless")   #to run in headless mode(without gui), remove "#" at the start of this line
driver = webdriver.Firefox(executable_path="C:\WebDriver\bin\<driver>.exe")  #edit driver location
driver = webdriver.Firefox(options=options)
driver.maximize_window()
driver.get("https://www.messenger.com/")

#login
userid = driver.find_element_by_id("email").click()
userid.send_keys("<your emailid>")  #email id
driver.find_element_by_id("pass").send_keys("<yourpassword>")  #password
driver.find_element_by_id("loginbutton").click()
driver.find_element_by_tag_name('html').send_keys(Keys.ESCAPE)

#select person x
wait = WebDriverWait(driver, 10)
xsel = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-href='https://www.messenger.com/t/firstname.lastname.38' and @class='_1ht5 _2il3 _6zka _5l-3 _3itx']")))  # edit the url in this line to appropriate one    
xsel.click()

#send message to person x and exit
xtext = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'_5rpu') and @role='combobox']")))
xtext.click()
xtext.send_keys(send_text)
xtext.send_keys(Keys.RETURN)
driver.quit()
