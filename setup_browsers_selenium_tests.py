from selenium import webdriver
from pyvirtualdisplay import Display

def setup_headless_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    #optional - to set the size of disk cache as 0
    chrome_options.add_argument('--disk-cache-size=0')
    chrome_options.add_argument('--window-size=1200,1100')
    path_to_chromedriver = '/home/shahnaz/Downloads/chromedriver'
    driver = webdriver.Chrome(path_to_chromedriver, chrome_options=chrome_options)


#Note: if tests are running in parallel, we need to synchornize webdriver creation
# acquire and release lock before and after this function is called to solve the above problem
def setup_chrome_with_xvfb():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    display = Display(visible=0, size=(1200, 1100))
    display.start()
    path_to_chromedriver = '/home/shahnaz/Downloads/chromedriver'
    driver = webdriver.Chrome(path_to_chromedriver, chrome_options=chrome_options)




