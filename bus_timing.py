from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def bus_timing(busstop):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--start-maximized")
    driver = webdriver.Chrome(options = chromeOptions)

    driver.get('https://www.nextbuses.sg/')

    time.sleep(3)
    inputElement = driver.find_element_by_xpath('//*[@id="theform"]/input[1]')
    inputElement.send_keys(busstop)
    inputElement.send_keys(Keys.ENTER)
    
    time.sleep(3)
    location = driver.find_element_by_xpath('//*[@id="stop-description"]').text
    buses = driver.find_elements_by_xpath('/html/body/div[3]/table/tbody/tr')
    data = location + "\nBus number: Next, Subsequent\n"
    for bus in buses:
        number = bus.get_attribute("id")
        try:
            next = bus.find_element_by_class_name("next")
            next_time = next.text
        except:
            next_time = ""
        try:
            subsequent = bus.find_element_by_class_name("subsequent")
            subsequent_time = subsequent.text
        except:
            subsequent_time = ""

        data += "{0}: {1}, {2} \n".format(number, next_time, subsequent_time)
    driver.close()
    return data

if __name__ == "__main__":
    print(bus_timing("55009"))