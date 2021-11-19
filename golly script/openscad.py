# OpenSCAD generator for Golly
# phooky@gmail.com

import golly

rect = golly.getrect()
if len(rect) == 0:
	golly.exit("Please create a pattern.")

count = int(golly.getstring("Number of generations to evolve:","8"))
ofile = open(golly.getstring("OpenSCAD output file:","golly.scad"),"w")

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


def cell_set(cell_list):
	cells = set()
	while len(cell_list) > 1:
		cells.add((cell_list.pop(0),cell_list.pop(0)))
	return cells

# get initial cells
initial = golly.getcells(rect)

# create cell sets for all generations
generations = [cell_set(golly.evolve(initial,c)) for c in range(count)]

# dump preamble to output
ofile.write(preamble)

# union of all cell transitions
ofile.write("union() { \n")

def buildLayerCubes(bottom,top,z,ofile):
	for (x,y) in bottom:
		candidates = set([(xp,yp) for xp in range(x-1,x+2) for yp in range(y-1,y+2)])
		for (xp,yp) in candidates.intersection(top):
			ofile.write("span_cube({0},{1},{2},{3},{4});\n".format(x,y,xp,yp,z))

for i in range(count-1):
	buildLayerCubes(generations[i],generations[i+1],i,ofile)

ofile.write("} \n")

ofile.close()

