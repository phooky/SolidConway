#!/usr/bin/python

import re
import sys

def usage():
	print """
Solid Conway is a script for converting a series of RLE files
representing generations in the game of life into an openSCAD
program producing a solid object representing the evolution
of the pattern.

Usage:
solid_conway.py gen1.rle gen2.rle ...
"""

preamble = """
module skew_cube(a,b) {
	multmatrix(m = [
		[1, 0, a, 0],
		[0, 1, b, 0],
		[0, 0, 1, 0]
	]) cube(size=1.00001);
}

module span_cube(x1,y1,x2,y2,z) {
	translate(v=[x1,y1,z])
	skew_cube(x2-x1,y2-y1);
}

"""

reXY = re.compile(r"x\s*=\s*([0-9]+),\s*y\s*=\s*([0-9]+)")
rePos = re.compile(r"Pos\s*=\s*(\-?[0-9]+),\s*(\-?[0-9]+)")

def parseOutRLE(raw,row):
	count = 0
	off = 0
	for c in raw:
		if c <= '9' and c >= '0':
			count = (count * 10) + int(c)
		else:
			if count == 0: count = 1
			if c == 'b':
				row[off:off+count] = [0]*count
			elif c == 'o':
				row[off:off+count] = [1]*count
			off = off + count
			count = 0

class Generation:
	def __init__(self, position, data):
		self.pos = position
		self.data = data
	def has(self,i,j):
		i = i - self.pos[0]
		j = j - self.pos[1]
		if i < 0 or j < 0:
			return 0
		if j >= len(self.data):
			return 0
		if i >= len(self.data[j]):
			return 0
		return self.data[j][i]
	def walk(self, fn):
		"Walk the tuples of on cells"
		for j in range(len(self.data)):
			for i in range(len(self.data[j])):
				if self.data[j][i]:
					fn(i+self.pos[0],j+self.pos[1])

def loadRLE(path):
	lines = open(path).readlines()
	data = []
	pos=(0,0)
	dim=(0,0)
	y = 0
	for line in lines:
		posMatch = rePos.search(line)
		if posMatch:
			pos=(int(posMatch.group(1)),int(posMatch.group(2)))
			continue
		xyMatch = reXY.match(line)
		if xyMatch:
			dim=(int(xyMatch.group(1)),int(xyMatch.group(2)))
			data=[[0 for i in range(dim[0])] for j in range(dim[1])]
			continue
		if line and line[0] != "#":
			# line is data
			rows=line.split("$")
			for row in rows:
				parseOutRLE(row,data[y])
				y = y + 1
	#print pos,data
	return Generation(pos,data)

paths = sys.argv[1:]
generations = map(loadRLE,paths)

def buildParentsForGen(genAbove,z):
	def buildParents(i,j):
		# use genAbove
		irange = range(i-1,i+2)
		jrange = range(j-1,j+2)
		for jt in jrange:
			for it in irange:
				if genAbove.has(it,jt):
					print "span_cube({0},{1},{2},{3},{4});".format(i,j,it,jt,z)
	return buildParents

if len(generations) < 2:
	print "Need at least two generations."
	usage()
	sys.exit(1)

print preamble

print "union() {"
for idx in range(len(generations)-1):
	generations[idx].walk(buildParentsForGen(generations[idx+1],idx))
print "}"

