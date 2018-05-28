import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    #print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    #print 'Retrieved',len(data),'characters'
    #print data
    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        #print data
        continue

    #print json.dumps(js, indent=4)

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lon = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat: ',lat
    print "lon:", lon
    location = js['results'][0]['formatted_address']
    #print location
    api_key = 'a61a3f82abf9bbcc88a393a8c9c4a091'

    weatherURL = 'https://api.forecast.io/forecast/%s/%s,%s?'  %(api_key,lat,lon)
    #print weatherURL


    url2 = weatherURL + urllib.urlencode({'sensor':'false', 'address': address})
    #print "Retrieving:", url2
    uh2 = urllib.urlopen(url2)
    data2 = uh2.read()
    #print 'Retrieved',len(data2),'characters''\n'
    #print ()
    try: js2 = json.loads(str(data2))
    except: js2 = None


    summary = js2["currently"]["summary"]
    temp =js2["currently"]["temperature"]
    forecast = js2["hourly"]["summary"]
    #print data2
    tempC= round((float(temp)-32.0)/1.8,1)
    print location, '\n'
    #print ('\n')
    print "Currently: ",summary
    print "Temp F: ", temp, "Temp C:", tempC
    print "Forecast: ", forecast, '\n'
