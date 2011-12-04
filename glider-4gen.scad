
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


union() {
span_cube(-2,-3,-3,-2,0);
span_cube(-2,-3,-1,-2,0);
span_cube(-1,-2,-1,-2,0);
span_cube(-1,-2,-2,-1,0);
span_cube(-1,-2,-1,-1,0);
span_cube(-3,-1,-3,-2,0);
span_cube(-3,-1,-2,-1,0);
span_cube(-3,-1,-2,0,0);
span_cube(-2,-1,-3,-2,0);
span_cube(-2,-1,-1,-2,0);
span_cube(-2,-1,-2,-1,0);
span_cube(-2,-1,-1,-1,0);
span_cube(-2,-1,-2,0,0);
span_cube(-1,-1,-1,-2,0);
span_cube(-1,-1,-2,-1,0);
span_cube(-1,-1,-1,-1,0);
span_cube(-1,-1,-2,0,0);
span_cube(-3,-2,-3,-1,1);
span_cube(-1,-2,-1,-2,1);
span_cube(-1,-2,-1,-1,1);
span_cube(-2,-1,-1,-2,1);
span_cube(-2,-1,-3,-1,1);
span_cube(-2,-1,-1,-1,1);
span_cube(-2,-1,-2,0,1);
span_cube(-2,-1,-1,0,1);
span_cube(-1,-1,-1,-2,1);
span_cube(-1,-1,-1,-1,1);
span_cube(-1,-1,-2,0,1);
span_cube(-1,-1,-1,0,1);
span_cube(-2,0,-3,-1,1);
span_cube(-2,0,-1,-1,1);
span_cube(-2,0,-2,0,1);
span_cube(-2,0,-1,0,1);
span_cube(-1,-2,-2,-2,2);
span_cube(-1,-2,-1,-1,2);
span_cube(-1,-2,0,-1,2);
span_cube(-3,-1,-2,-2,2);
span_cube(-3,-1,-2,0,2);
span_cube(-1,-1,-2,-2,2);
span_cube(-1,-1,-1,-1,2);
span_cube(-1,-1,0,-1,2);
span_cube(-1,-1,-2,0,2);
span_cube(-1,-1,-1,0,2);
span_cube(-2,0,-1,-1,2);
span_cube(-2,0,-2,0,2);
span_cube(-2,0,-1,0,2);
span_cube(-1,0,-1,-1,2);
span_cube(-1,0,0,-1,2);
span_cube(-1,0,-2,0,2);
span_cube(-1,0,-1,0,2);
}
