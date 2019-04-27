import os
from PIL import Image as img

inpath = './In-JPG/'
outpath = './Out-PNG/'

for i in os.listdir(inpath):

    print('[INFO] Saving ' + i + ' as PNG...')
    raw = img.open(inpath + i)
    raw.save(outpath + i[:-3] + 'png')

for i in os.listdir(outpath):

    print('[INFO] Converting ' + i + ' to RGBA...')
    pic = img.open(outpath + i).convert('RGBA')
    pic.save(outpath + i)
