from svgpathtools import *
import base64,math,numpy as np, sys
from graphicsgd import level
def mad(data, axis=None):
	return np.mean(abs(data - np.mean(data, axis)), axis)
def slope(x1, y1, x2, y2):
	try:
		m = math.atan2(y2-y1,x2-x1)
	except:
		return 0
	else:
		return m
def uploadSvg(file_path,scale,lname,uname,password):
	pths, _ = svg2paths(file_path)
	wsvg(pths,filename='.tmp.svg')
	paths, _ = svg2paths('.tmp.svg')
	pathsxy = []
	lvl = level.Level(lname)
	for path in paths:
		x = [0.1]
		y = [0.1]
		slopes = []
		for p in path:
			numm = []
			p.start /= scale
			p.end /= scale
			if type(p) == CubicBezier:
				p.control1/=scale
				p.control2/=scale
			elif type(p) == Arc:
				p.radius/=scale
			elif type(p) == QuadraticBezier:
				p.control/=scale
			elif type(p) != Line:

				print(p)
			for i in range(round(p.length())):
				comp = p.point(i/p.length())
				slopes.append(slope(x[-1],y[-1],comp.real,comp.imag))
				x.append(comp.real)
				y.append(comp.imag)
		pathsxy.append(np.column_stack((x[1:],y[1:],slopes,)))
	svglengthx = max(np.concatenate([l[:,0] for l in pathsxy]))
	svglengthy = max(np.concatenate([l[:,1] for l in pathsxy]))
	total = 0
	for path in pathsxy:
		for point in path:
				total += 1
				lvl.addBlock(917,point[0]*2,((-1*point[1])+svglengthy)*2,rotation=math.degrees(point[2]),size=0.3,dont_fade=1,dont_enter=1)
	print("Objects used: "+str(total)+". Note: if the level uses over 3000 objects, it might not load")
	print("In order to properly upload, we need an account to upload it to")
	lid = lvl.uploadLevel(uname,password,lpassword="1",description="")
	return lid