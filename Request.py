import requests
import cv2
from fake_useragent import UserAgent

page_link = 'https://www.avito.ru/pskov/vakansii?cd=1&q=псков+работа'
image_back = cv2.imread("Tota/back.png")
gray_image = cv2.cvtColor(image_back, cv2.COLOR_BGR2GRAY)

session = requests.Session()

session.headers = {
        'User-Agent': UserAgent().random,
        'Accept': 'text/html',
        'Accept-Language': 'ru,en-US;q=0.5',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache'
}

response = session.get(page_link)
session.close()
print(f"{response}\n{response.text}")