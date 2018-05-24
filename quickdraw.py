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
              'cloud', 'cow', 'cup', 'dog', 'duck', 'house', 'moon', 'pig', 'rabbit', 'sheep', 'streetlight',
              'sun', 'table', 'tree', 'duck', 'umbrella']
cate_counts = [0 for i in range(len(categories))]


data = json.load(open('data.json'))

if not os.path.exists('data'):
    os.makedirs('data')

for cate in categories:
    if not os.path.exists('data/' + cate):
        os.makedirs('data/' + cate)

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
    # get label
    k = 0
    for i, x in enumerate(a['output']):
        if x == 1:
            k = i
            break
    cate = categories[k]
    cv2.imwrite('data/%s/%d.png' % (cate, cate_counts[k]), mat)
    cate_counts[k] += 1




