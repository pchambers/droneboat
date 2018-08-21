"""
gpxTupleParse - pass common tuple format to gpx for passing 
deals with paths as list of tuples. 
"""
import gpxpy
import gpxpy.gpx

def tupsToGpx(tups):
	gpx = gpxpy.gpx.GPX()
	# Create first track in our GPX:
	gpx_track = gpxpy.gpx.GPXTrack()
	gpx.tracks.append(gpx_track)

	# Create first segment in our GPX track:
	gpx_segment = gpxpy.gpx.GPXTrackSegment()
	gpx_track.segments.append(gpx_segment)

	# Create points:
	for pt in tups:
		gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(pt[0], pt[1], elevation=0))

	# You can add routes and waypoints, too...

	print 'Created GPX:', gpx.to_xml()
	return gpx.to_xml();

