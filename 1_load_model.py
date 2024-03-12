import requests
import zipfile


url = 'https://firebasestorage.googleapis.com/v0/b/countdown-jobfiar.appspot.com/o/kanji_small.zip?alt=media&token=4167f478-91d1-44cc-8d9b-2425d764be97'
model_url = 'https://firebasestorage.googleapis.com/v0/b/countdown-jobfiar.appspot.com/o/vgg16_model.h5?alt=media&token=8f1afebf-fc88-4755-a3b9-aeebc9802544'

def load(url, name, filename):
    response = requests.get(url, stream=True)  # Stream download for efficiency
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):  # Download in chunks
                f.write(chunk)
        print(name, 'download complete!')
    else:
        print('Error downloading file:', response.status_code)

# load unclean datasets
load(url, 'kanji_small', 'kanji_small.zip')
with zipfile.ZipFile('kanji_small.zip', 'r') as zip_ref:
    zip_ref.extractall('kanji_small')  # Specify a desired extraction path
print('Extraction kanji_small completed!')
# load final vgg16 model
load(model_url, 'model', 'vgg16_model.h5')