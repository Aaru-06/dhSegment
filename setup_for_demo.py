import urllib.request
import zipfile
import os
from tqdm import tqdm

link = ['https://github.com/dhlab-epfl/dhSegment/releases/download/v0.2/model.zip','https://github.com/dhlab-epfl/dhSegment/releases/download/v0.2/pages.zip']

def progress_hook(t):
    last_b = [0]

    def update_to(b=1, bsize=1, tsize=None):
        if tsize is not None:
            t.total = tsize
        t.update((b - last_b[0]) * bsize)
        last_b[0] = b

    return update_to

if __name__ == '__main__':
    modelname = "model.zip"
    sampledata = "pages.zip"
    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1,
              desc="Downloading pre-trained model") as t:
        urllib.request.urlretrieve(link[0], modelname,
                                   reporthook=progress_hook(t))
    print("Unziping model.zip..")
    with zipfile.ZipFile("model.zip",'r') as actualzipfile:
        actualzipfile.extractall()
    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1,
              desc="Downloading sample data") as t:
        urllib.request.urlretrieve(link[1], sampledata,
                                   reporthook=progress_hook(t))
    print("Unziping sample_data.zip..")
    with zipfile.ZipFile("pages.zip",'r') as actualzipfile:
        actualzipfile.extractall()
    print("Done......")
    print("copy the images to be segmented from pages folder into the prediction_input/images")
    print("run \"python predict.py\"")