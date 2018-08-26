"""
Testing waypionts and tracking for autopilot.  

Start in water near home, plot path around islands and back. 
"""

import gpxTupleParse

home = (42.184580,- 71.420189)

wp1 = (42.187203,-71.422325)
wp2 = (42.186043, -71.425086)
wp3 = (42.184982, -71.424051)
wp4 = (42.185130, -71.420475)

# path: home > 1 > 2 > 3 > 4 > home
path = [home, wp1, wp2, wp3, wp4, home]

"""
write gpx takes in a list of tuples(lat, long) and creates a new GPX doc, route1
"""
def writeGPX(tups):
	pathXML = gpxTupleParse.tupsToGpx(tups)

	newRoute = open("./GPX_Routes/route1.gpx", "w")
	newRoute.write(pathXML)
	newRoute.close()

#writeGPX(path)

