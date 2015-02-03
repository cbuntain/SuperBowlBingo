#!/usr/bin/python

import sys
import os
import subprocess
import pipes
import random

imgDir = './imgs'
outDir = './tabs'
backingImg = 'comp_back.bmp'

cellW = 85
cellH = 78

boardOffsetX = 66
boardOffsetY = 278

dim = 5

files = []

(_, _, filenames) = os.walk(imgDir).next()
files.extend(filenames)

files = filter(lambda x: not x.startswith('.'), files)

baseGeoString = "%dx%d" % (cellW, cellH)
baseCmd = ['convert', '-size', baseGeoString, 'xc:white', 'comp_back.bmp']
subprocess.call(' '.join(baseCmd), shell=True)

geoString = "%dx%d+0+0" % (cellW, cellH)
counter = 0;
for fileName in files:
	outFile = "%s/%04d.png" % (outDir, counter)
	filePath = "%s/%s" % (imgDir, fileName)
	filePath = pipes.quote(filePath)

	cmd = ['composite', '-quality', '10', '-gravity', 'Center', '-geometry', geoString, filePath, backingImg, outFile]
	print ' '.join(cmd)

	subprocess.call(' '.join(cmd), shell=True)

	counter = counter + 1

tabList = []
(_, _, filenames) = os.walk(outDir).next()
tabList.extend(filenames)
tabList = filter(lambda x: not x.startswith('.'), tabList)

random.shuffle(tabList)
bingoTabs = tabList[:25]

bingoTabs[12] = '../center.png'

subprocess.call('convert board.pdf out.pdf', shell=True)

index = 0
for row in range(dim):

	yOffset = boardOffsetY + (cellH + 3) * row

	for col in range(dim):

		tabFile = "%s/%s" % (outDir, bingoTabs[index])

		xOffset = boardOffsetX + (cellW + 5) * col

		geoString = "+%d+%d" % (xOffset, yOffset)

		cmd = ['composite', '-geometry', geoString, tabFile, 'out.pdf', 'out.pdf']
		print ' '.join(cmd)
		subprocess.call(' '.join(cmd), shell=True)

		index = index + 1


