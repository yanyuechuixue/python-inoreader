from inoreader.main import get_client
import bs4
from DownloadImg import download_images
import subprocess
client = get_client()
stars = client.fetch_starred()

'''run a shell command line 'inoreader login' , if it runs sucessful, do nothing, otherwise stop. we use subprocess to run the command line'''
subprocess.call(['inoreader', 'login'])

for article in list(stars):
    bs4content = bs4.BeautifulSoup(article.content, 'html.parser')
    imgs = bs4content.findAll('img')
    Images_for_download = []
    for img_ in imgs:
        if 'www.inoreader.com/adv' in img_['src']: continue
        Images_for_download.append(img_['src'])

    #download_images(Images_for_download, article.id.split('/')[-1])
    download_images(Images_for_download, article.title)
    client.remove_starred([article])