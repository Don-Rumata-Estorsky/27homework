"""
скачивание 10 картинок с сайта в разные папки
"""
import requests
import random
import os

def download(url_end, num_images=10, save='images'):

  if not os.path.exists(save):
      os.makedirs(save)

  for _ in range(num_images):
    url = random.choice(url_end)
    response = requests.get(url, stream=True)

    if response.status_code == 200:
      image_dir = os.path.join(save, f"image_{random.randint(1, 10)}")
      os.makedirs(image_dir, exist_ok=True)

      filename = os.path.join(image_dir, 'image.jpg')
      with open(filename, 'wb') as f:
        for chunk in response.iter_content(1024):
          f.write(chunk)

    else:
      print("Ошибка")

url_end = ["https://degrabebs.miraheze.org/wiki"]

if __name__ == "__main__":
    download(url_end)
