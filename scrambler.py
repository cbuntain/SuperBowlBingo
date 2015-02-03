#!/usr/bin/python

import sys
import os
import subprocess
import pipes
import random

outDir = './tabs'
boardDir = './boards'
backingImg = 'comp_back.bmp'

boardCopies = 10

if ( len(sys.argv) > 1 ):
	print "Board Copies:", sys.argv[1]
	boardCopies = int(sys.argv[1])

cellW = 85
cellH = 78

boardOffsetX = 66
boardOffsetY = 278

dim = 5

tabList = []
(_, _, filenames) = os.walk(outDir).next()
tabList.extend(filenames)
tabList = filter(lambda x: not x.startswith('.'), tabList)

for boardNumber in range(boardCopies):

	newFile = str(boardNumber) + ".pdf"

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

	cmd = ['mv', 'out.pdf', boardDir + '/' + newFile]
	print ' '.join(cmd)
	subprocess.call(' '.join(cmd), shell=True)
