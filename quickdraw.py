import cv2
import numpy as np
import json
import os

# quickdraw.py
# convert quickdraw.js results into bitmap pictures
# first, npm install quickdraw.js
# run node quickdraw.js
# run python quickdraw.py
# Author: Ruofei Du

categories = ['airplane', 'apple', 'banana', 'basket', 'bee', 'bench', 'bicycle', 'bus', 'butterfly', 'cat', 'chair',
              'cloud', 'cow', 'cup', 'dog', 'duck', 'horse', 'house', 'moon', 'pig', 'rabbit', 'sheep', 'streetlight',
              'sun', 'table', 'tree', 'truck', 'umbrella']
# cate_counts = [490, 125, 49, 73, 218, 264, 46, 108, 168, 137, 500, 51, 175, 62, 230, 92, 479, 234, 44, 168, 168, 170,
#                69, 139, 692, 687, 79, 19]
cate_counts = [0 for i in range(len(categories))]

if not os.path.exists('output'):
    os.makedirs('output')

for cid, cate in enumerate(categories):
    if not os.path.exists('output/' + cate):
        os.makedirs('output/' + cate)
    data = json.load(open('json128/%s.json' % cate))
    size = data['input']
    w = int(size ** 0.5)
    mat = np.zeros((w, w, 1), np.uint8)

    for a in data['set']:
        # copy pics
        k = 0
        for x in a['input']:
            i = k // w
            j = k % w
            k += 1
            mat[i][j] = np.uint8(255 - x * 255)
            pass
        cv2.imwrite('output/%s/%d.png' % (cate, cate_counts[cid]), mat)
        cate_counts[cid] += 1
    print(cate)
