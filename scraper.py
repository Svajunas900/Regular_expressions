from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def get_text_from_wiki(user_input: str) -> str:
  driver = Chrome() 

  url = "https://www.wikipedia.org/"

  driver.get(url)

  input = driver.find_element(by=By.XPATH, value="/html/body/main/div[2]/form/fieldset/div/input")
  input.send_keys(user_input)

  button = driver.find_element(by=By.XPATH, value="/html/body/main/div[2]/form/fieldset/button")
  button.click()

  main_text_element = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]")
  main_text = main_text_element.text
  driver.quit()
  return main_text

