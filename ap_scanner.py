import csv
from pygle import network

#Function that will pass BSSID to wigle API and return geolocation
def locate_network(bssid):
    net_info = network.search(netid=bssid)
    temp=net_info['results']
    latitude=temp[0]['trilat']
    longitude=temp[0]['trilong']
    return (str(latitude)+','+str(longitude))

def remove_duplicate_ssids(csvfile):
    i=2
    tempcsv=[]
    while i<len(csvfile):
        temp=csvfile[i]
        temp_BSSID=temp[0]
        temp_SSID=temp[1]

        if temp_BSSID in tempcsv:
            continue
        else:
            tempcsv.append(temp_BSSID)



    f = 0
    for i in csvfile:
        if csvfile[i] in tempcsv:
            continue
        #else:
        #    tempcsv[i]=csvfile[i]
        #    return 0
        


#Open the Kismet csv file
with open('wigle.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

i=2
while i<len(data):
    
    temp = data[i]
    unique_SSID = []
    
    if temp[0] == "Station MAC":
        i = len(data)
    if len(temp) > 10:
        temp_BSSID = temp[0] 
        temp_SSID = temp[13]
        i=i+1
        
    if temp_BSSID not in unique_SSID:
    #location = str(locate_network(temp[0]))
        with open('output.csv', 'a') as out:
            #out.write(temp[0]+','+temp[13]+','+location+'\n')
            out.write(temp[0]+','+temp[13]+'\n')
     

