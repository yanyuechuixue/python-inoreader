import os
import tqdm
import requests

def download_images(images, folder_name):

    # make a dir named folder_name if not exist
    if not os.path.exists('images'):
        os.mkdir('images')

    folder_name = 'images/' + folder_name

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

        
    i = 0
    for image_link in tqdm.tqdm(images):
        try:
            r = requests.get(image_link).content
            try:

                # possibility of decode
                r = str(r, 'utf-8')

            except UnicodeDecodeError:

                # After checking above condition, Image Download start
                with open(f"{folder_name}/images{i+1}."+str(image_link.split('.')[-1]), "wb+") as f:
                    f.write(r)
                i += 1
        except:
            pass
  