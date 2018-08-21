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

pathXML = gpxTupleParse.tupsToGpx(path)

newRoute = open("test1.gpx", "w")
newRoute.write(pathXML)

