# -*- coding: latin-1 -*-

import csv

print """<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
    <meta charset="utf-8">
    <title>Simple markers</title>
    <style>
      html, body, #map-canvas {
        height: 100%;
        margin: 0px;
        padding: 0px
      }
    </style>
    <script src="https://maps.googleapis.com/maps/api/js?v=3.exp&signed_in=true"></script>
    <script>
function initialize() {
  var myLatlng = new google.maps.LatLng(37.4219957,-122.0843128);
  var center = new google.maps.LatLng(38.5804149,-98.4107151);
  var mapOptions = {
    zoom: 4,
    center: center
  }
  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
  var markers = [];
"""


with open('jlu.csv') as f:
  reader = csv.DictReader(f)
  for row in reader:
    print '  markers.push(new google.maps.Marker({'
    print '      position: new google.maps.LatLng(',row['经纬度'],'),'
    print '      map:map,'
    print '      title:"',row['Marker显示信息'],'"'
    print '  }));'
print '}'
print """google.maps.event.addDomListener(window, 'load', initialize);

    </script>
      </head>
  <body>
    <div id="map-canvas"></div>
  </body>
</html>
"""
