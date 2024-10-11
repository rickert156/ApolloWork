from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from login import user_login, user_password, machine
from slack import SendSlack
import csv, os, json, time, shutil

options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36')

options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options)

print('-'*45)
print('|', ' '*41, '|')
print('|','         Welcome to Apollo V2             |')
print('|', ' '*41, '|')
print('-'*45)


try:
	def start():
		driver.get("https://app.apollo.io/#/settings/account/mailboxes")
		driver.maximize_window()
		time.sleep(10)

		email_login = driver.find_element(By.NAME, 'email')
		email_login.send_keys(user_login)
		time.sleep(1)
		password = driver.find_element(By.NAME, 'password')
		password.send_keys(user_password)
		password.send_keys(Keys.ENTER)
		time.sleep(5)

		slack_payload = {"text": f"[{machine}]Parser Apollo. Step 2 Start..."}

		SendSlack(slack_payload)



	def persLink():
		num=0
		for file_json in os.listdir('Collected/'):
			with open(f'Collected/{file_json}', 'r') as file:
				data = json.load(file)
				second_value = data["Links"]
				with open('result.csv', 'a', newline='', encoding='utf-8') as file:  
					writer = csv.writer(file)
					
					#print(second_value)
					num+=1
					try:
						driver.get(second_value)
						time.sleep(5)
						print('\n')
						print('-'*5, f'Persone {num}', '-'*5)

						try:
							time.sleep(2)
							close_modal = driver.find_element(By.CLASS_NAME, 'zp-icon.mdi.mdi-close.zp_QUSTG.zp_K7tmh.zp_IMabJ')
							close_modal.click()
							print('Click and close modal window')
						except:
							pass
						try:
							close_modal = driver.find_element(By.CLASS_NAME, 'zp_qe0Li.zp_S5tZC.zp_nQ45Z')
							close_modal.click()
							print('Click and close modal window')
						except:pass
						try:
							button_email = driver.find_element(By.CLASS_NAME, 'zp-icon.apollo-icon.apollo-icon-download.zp_QUSTG.zp_K7tmh.zp_NGTfw')
							button_email.click()
							time.sleep(5)
						except:
							pass
						try:
							name_persone = driver.find_element(By.CLASS_NAME, 'zp-inline-edit-popover-trigger.zp_uH2hd.zp_voKSC.zp_drD_u').text
							print(f'Name: {name_persone}')
						except:
							name_persone = 'Not Defined'
							print(f'Name: {name_persone}')
						try:
							job_title = driver.find_element(By.CLASS_NAME, 'zp_usEUk').text
							print(f'Job Title: {job_title}')
						except:
							job_title = 'Not Defined'
							print(f'Job Title: {job_title}')
						try:
							email = driver.find_element(By.CLASS_NAME, 'zp_p2Xqs.zp_v565m.zp_N3Yvt.zp_kOWmA').text
							print(f'Email: {email}')
						except:
							email = 'Not Defined'
							print(f'Email: {email}')
						try:
							company_name = driver.find_element(By.CLASS_NAME, 'zp_p2Xqs.zp_v565m').text
							print(f'Company Name: {company_name}')
						except:
							company_name = 'Not Defined'
							print(f'Company Name: {company_name}')
						try:
							location = driver.find_element(By.CLASS_NAME, 'zp_U0WNp').text
							print(f'Location: {location}')
						except:
							location = 'Not Defined'
							print(f'Location: {location}')
						try:
							phone_number = driver.find_element(By.CLASS_NAME, 'zp-link.zp_OotKe.zp_lmMY6').text
							print(f'Phone: {phone_number}')
						except:
							phone_number = 'Not Defined'
							print(f'Phone: {phone_number}')
						try:
							linkedin_link = driver.find_element(By.XPATH, '//a[contains(@href, "linkedin.com")]')
							linkedin_url = linkedin_link.get_attribute("href")
							print(f'Linkedin: {linkedin_url}')
						except:
							linkedin_url = 'Not Defined'
							print(f'Linkedin: {linkedin_url}')	
						try:
							twitter_link = driver.find_element(By.XPATH, '//a[contains(@href, "twitter.com")]')
							twitter_url = twitter_link.get_attribute("href")
							print(f'Twitter: {twitter_url}')
						except:
							twitter_url = 'Not Defined'
							print(f'Twitter: {twitter_url}')

						try:
							facebook_link = driver.find_element(By.XPATH, '//*[@id="insights_card"]/div/div[2]/div/div/div[1]/div/div/div/div/div/form/div[1]/div[1]/div[2]/div/div/a[3]')
							facebook_url = facebook_link.get_attribute("href")
							print(f'Facebook: {facebook_url}')
						except:
							facebook_url = 'Not Defined'
							print(f'Facebook: {facebook_url}')
						
						time.sleep(20)
						writer.writerow([name_persone, job_title, email, company_name, location, phone_number, linkedin_url, twitter_url, facebook_url])
						print('Data written to CSV.\n', '-'*20)
						shutil.move(f'Collected/{file_json}', f'Done/{file_json}')
						if num == 50:break

					except:
						pass

	def main():
		start()
		persLink()

	main()

except Exception as ex:
	print(ex)
finally:
	slack_payload = {"text": f"[{machine}]Parser Apollo. Step 2 Stop..."}
	SendSlack(slack_payload)
	driver.close()
	driver.quit()

zp_qe0Li zp_S5tZC zp_nQ45Z