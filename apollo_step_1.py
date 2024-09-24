from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from login import user_login, user_password, machine
from slack import SendSlack
import json, os, time

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36')

options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

print('-'*45)
print('|', ' '*41, '|')
print('|','         Welcome to Apollo V2             |')
print('|', ' '*41, '|')
print('-'*45)


if not os.path.exists('Collected'):
	os.makedirs('Collected')

if not os.path.exists('Done'):
	os.makedirs('Done')

try:
	driver.get("https://app.apollo.io/#/settings/account/mailboxes")
	driver.maximize_window()
	time.sleep(3)

	email_login = driver.find_element(By.NAME, 'email')
	email_login.send_keys(user_login)
	time.sleep(1)
	password = driver.find_element(By.NAME, 'password')
	password.send_keys(user_password)
	password.send_keys(Keys.ENTER)
	time.sleep(5)

	slack_payload = {"text": f"[{machine}]Parser Apollo. Step 1 Start..."}

	SendSlack(slack_payload)

	def persUrl():
		personLocations = input("""Select a location, default will be United States(y): 
			1. United States
			2. India
			3. Russia
			4. Ukraine
			5. Europe
			6. North America
			7. Americas
			8. Australia
			9. United Kingdom
			Select a Location: """)
		if personLocations == 'y' or personLocations == '' or personLocations == '':personLocations = 'United States'
		elif personLocations == '2':personLocations = 'India'
		elif personLocations == '3':personLocations = 'Russia'
		elif personLocations == '4':personLocations = 'Ukraine'
		elif personLocations == '5':personLocations = 'Europe'
		elif personLocations == '6':personLocations = 'North America'
		elif personLocations == '7':personLocations = 'Americas'
		elif personLocations == '8':personLocations = 'Australia'
		elif personLocations == '9':personLocations = 'United Kingdom'
		else: personLocations = 'United States'

		print(f'Location: {personLocations}')

		personSeniorities = input("""
			Select a Job Titles, default will be Owner(y): 
			1. Owner
			2. Founder
			3. Partner
			4. Vp
			5. Head
			6. Director
			7. Manager
			8. C Suite
			Select a Job Titles: 
			""")
		if personSeniorities == 'owner' or personSeniorities == '1':personSeniorities = 'owner'
		elif personSeniorities == 'y' or personSeniorities == '':personSeniorities = 'owner'
		elif personSeniorities == '2':personSeniorities = 'founder'
		elif personSeniorities == '3':personSeniorities = 'partner'
		elif personSeniorities == '4':personSeniorities = 'vp'
		elif personSeniorities == '5':personSeniorities = 'head'
		elif personSeniorities == '6':personSeniorities = 'director'
		elif personSeniorities == '7':personSeniorities = 'manager'
		elif personSeniorities == '8':personSeniorities = 'c_suite'
		else: personSeniorities = 'owner'

		print(f'Job Title: {personSeniorities}')
		
		organizationIndustryTagIds = input("""
			Select a Indastrial, default will be Graphical Design(y): 
			1. Graphical Design
			2. Banking
			3. Computer Games
			4. Design
			5. Political Organization
			6. Program Development
			7. Animation
			8. Design
			9. Computer software
			10. Venture Capital & Private Equity
			11. Commercial Real Estate
			12. Computer & Network Security
			13. E-learning
			Select a Indastrial: """)
		if organizationIndustryTagIds == '' or organizationIndustryTagIds == '1' or organizationIndustryTagIds == 'y':organizationIndustryTagIds = '5567cd4d73696439d9040000'
		elif organizationIndustryTagIds == '2':organizationIndustryTagIds = '5567ce237369644ee5490000'
		elif organizationIndustryTagIds == '3':organizationIndustryTagIds = '5567cd8b736964540d0f0000'
		elif organizationIndustryTagIds == '4':organizationIndustryTagIds = '5567cdbc73696439d90b0000'
		elif organizationIndustryTagIds == '5':organizationIndustryTagIds = '5567e25f736964256cff0000'
		elif organizationIndustryTagIds == '6':organizationIndustryTagIds = '5567e2907369642433e60200'
		elif organizationIndustryTagIds == '7':organizationIndustryTagIds = '5567e36f73696431a4970000'
		elif organizationIndustryTagIds == '8':organizationIndustryTagIds = '5567cdbc73696439d90b0000'
		elif organizationIndustryTagIds == '9':organizationIndustryTagIds = '5567cd4e7369643b70010000'
		elif organizationIndustryTagIds == '10':organizationIndustryTagIds = '5567e1587369641c48370000'
		elif organizationIndustryTagIds == '11':organizationIndustryTagIds = '5567e1887369641d68d40100'
		elif organizationIndustryTagIds == '12':organizationIndustryTagIds = '5567cd877369644cf94b0000'
		elif organizationIndustryTagIds == '13':organizationIndustryTagIds = '5567e19c7369641c48e70100'
		else: organizationIndustryTagIds = organizationIndustryTagIds

	
		organizationNumEmployeesRanges_min = input('Select the MINIMUM number of employees: ')
		organizationNumEmployeesRanges_max = input('Select the MAXIMUM number of employees: ')
		print('\n')
		page = 0
		pages = int(input("\nHow many search pages do you need to go through? "))
		while page < pages:
			page+=1
			driver.get(f'https://app.apollo.io/#/people?finderViewId=5b6dfc5a73f47568b2e5f11c&page={page}&personLocations[]={personLocations}&personSeniorities[]={personSeniorities}&organizationIndustryTagIds[]={organizationIndustryTagIds}&organizationNumEmployeesRanges[]={organizationNumEmployeesRanges_min}%2C{organizationNumEmployeesRanges_max}')
			time.sleep(2)	        

			print("------\nPage ", page, " Found\n------")
			
			blocks = driver.find_elements(By.CLASS_NAME, 'zp_xVJ20')
			num = 0
			links = []
			for block in blocks:
				num += 1
				link = block.find_element(By.TAG_NAME, 'a')
				href = link.get_attribute('href')
				print(f'{num}.', href)
				links.append(href)
				url_h = href
				trimmed_url = url_h.rsplit('/', 1)[1]
				FILE_JSON = f'{trimmed_url}.json'
				with open(f'Collected/{FILE_JSON}', 'w') as outfile:
					json.dump({'Links': href}, outfile)
			num = 0

	persUrl()

except Exception as ex:
	print(ex)
finally:
	slack_payload = {"text": f"[{machine}]Parser Apollo. Step 1 Stop..."}
	SendSlack(slack_payload)
	driver.close()
	driver.quit()
