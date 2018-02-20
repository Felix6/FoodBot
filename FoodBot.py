# Author: Felix "punkRat"
# Dependencies: Selenium, splinter, Firefox Quantum
#
# Broke college student + python + hacker "because-i-can-mentallity" = This
#
# Script was made to get free soda with every purchase at Firehouse Subs.
#
# Scprit will sometimes crash depending on how fast the page loads.
#
from splinter import Browser



SurvCode =  raw_input("Please enter survey code: ").split('-')
CodeArr= [str(num) for num in SurvCode]

total = raw_input("Please enter total: ").split('.')
totalArr = [str(num) for num in total]

browser = Browser(driver_name='firefox')
#with Browser(driver_name='firefox') as browser:
    # Visit URL
url = "https://firehouselistens.smg.com/usa?AspxAutoDetectCookieSupport=1"
browser.visit(url)

# PAGE 1
browser.fill("CN1", CodeArr[0])
browser.fill("CN2", CodeArr[1])
browser.fill("CN3", CodeArr[2])
browser.fill("CN4", CodeArr[3])
browser.fill("TS1", totalArr[0])
browser.fill("TS2", totalArr[1])
browser.find_by_name('NextButton').first.click()

#PAGE 2
browser.find_by_xpath('//label [@for="R001000.1"]').first.click()
browser.find_by_value('Next').click()

#PAGE 3
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span').first.click()
browser.find_by_value('Next').click()

# PAGE 4
browser.find_by_xpath('//label [@for="R000012.1"]').first.click()
browser.find_by_value('Next').click()

# PAGE 5
browser.find_by_xpath('//label [@for="R104000.3"]').first.click()
browser.find_by_value('Next').click()

# PAGE 6
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[3]/td[2]/span').first.click()
browser.find_by_value('Next').click()

# PAGE 7
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[3]/td[2]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[4]/td[2]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[5]/td[2]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[6]/td[2]/span').first.click()
browser.find_by_value('Next').click()

# PAGE 8
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[3]/td[2]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[4]/td[2]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[5]/td[2]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[6]/td[2]/span').first.click()
browser.find_by_value('Next').click()

# PAGE 9
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[3]/td[2]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[4]/td[2]/span').first.click()
browser.find_by_value('Next').click()

# PAGE 10
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]/span').first.click()
browser.find_by_value('Next').click()

# PAGE 11
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[3]/td[2]/span').first.click()
browser.find_by_value('Next').click()


# PAGE 12
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span').first.click()
browser.find_by_value('Next').click()

# PAGE 13
browser.find_by_xpath('//label [@for="R000031.5"]').first.click()
browser.find_by_value('Next').click()

# PAGE 14
browser.find_by_value('Next').click()

# PAGE 15
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span').first.click()
browser.find_by_value('Next').click()

# PAGE 16
browser.find_by_xpath('//label [@for="R000011.2"]').first.click()
browser.find_by_value('Next').click()

# PAGE 17
browser.find_by_xpath('//label [@for="R053000.1"]').first.click()
browser.find_by_value('Next').click()

# PAGE 18
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]/span').first.click()
browser.find_by_value('Next').click()

# PAGE 19
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[3]/td[2]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[4]/td[2]/span').first.click()
browser.find_by_value('Next').click()

# PAGE 20
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span').first.click()
browser.find_by_value('Next').click()

# PAGE 21
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/div[1]/div[2]/div[5]/span/span').first.click()
browser.find_by_value('Next').click()

# PAGE 22
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span').first.click()
browser.find_by_value('Next').click()

# PAGE 23
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]/span').first.click()
browser.find_by_xpath('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[3]/td[3]/span').first.click()
browser.find_by_value('Next').click()

# PAGE 24


# 19101-00898-1002-1384
