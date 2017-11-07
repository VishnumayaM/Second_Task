from lxml import html  
import csv,os,json
import requests
from exceptions import ValueError
from time import sleep
 
def Parser(url):
    page = requests.get(url)
    while True:
        sleep(3)
        try:
            doc = html.fromstring(page.content)
            XPATH_NAME = '//h1[@class="overlay-h1"]//text()'
            XPATH_VENUE = '//li[@class="toh venue-li"]//text()'
	    XPATH_FOLLOWER = '//div[@class="detail"]//text()'
	    XPATH_EVENTS = '//div[@class="detail"]//text()'
            XPATH_TIME = '//ul[@class="meta-list"]//text()'
            XPATH_DESCRIPTION = '//div[@property="schema:description"]//text()'
	    #XPATH_TICKET='//div[@class="event-ticket-cont"]//text()'
            #XPATH_IMG = '//div[@class="cover"]//text()'
	    #XPATH_MAP = '//div[@class="venue-map"]//text()'


 
            RAW_NAME = doc.xpath(XPATH_NAME)
            RAW_VENUE = doc.xpath(XPATH_VENUE)
	    RAW_FOLLOWER = doc.xpath(XPATH_FOLLOWER)
	    RAW_EVENTS = doc.xpath(XPATH_FOLLOWER)
            RAW_TIME = doc.xpath(XPATH_TIME)
            RAW_DESCRIPTION = doc.xpath(XPATH_DESCRIPTION)
	    #RAW_TICKET = doc.xpath(XPATH_TICKET)
            #RAw_IMG = doc.xpath(XPATH_IMG)
	    #RAW_MAP = doc.xpath(XPATH_MAP)
 
            NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
            VENUE = ' '.join(''.join(RAW_VENUE).split()).strip() if RAW_VENUE else None
	    FOLLOWER = ' '.join(''.join(RAW_FOLLOWER).split()).strip() if RAW_FOLLOWER else None
	    EVENTS = ' '.join(''.join(RAW_EVENTS).split()).strip() if RAW_EVENTS else None
            TIME = ' '.join(''.join(RAW_TIME).split()).strip() if RAW_TIME else None
            DESCRIPTION = ''.join(RAW_DESCRIPTION).strip() if RAW_DESCRIPTION else None
	    #TICKET = ' '.join(''.join(RAW_TICKET).split()).strip() if RAW_TICKET else None
            #IMG = ''.join(RAw_IMG).strip() if RAw_IMG else None
	    #MAP = ''.join(RAW_MAP).strip() if RAW_MAP else None
 
            
 
            if page.status_code!=200:
                raise ValueError('captha')
            data = {
                    'NAME':NAME,
                    'VENUE':VENUE,
		    'FOLLOWER':FOLLOWER,
		    'EVENTS':EVENTS
                    'TIME':TIME,
                    'DESCRIPTION':DESCRIPTION,
		    #'TICKET':TICKET,
                    #'IMG':IMG,
		    #'MAP':MAP,
                    'URL':url,
                    }
 
            return data
        except Exception as e:
            print e
 
def ReadList():
    EventList = ['discover-your-brilliance/939513959466235',
		 'delhi-food-truck-festival/1946508412303834',
		 'adventure-camp-and-dj-night-party/80006771995676',
		 'human-rights-walk-commemorating-1984-anti-sikh-genocide/453326638395047',]
    extracted_data = []
    for i in EventList:
        url = "https://allevents.in/new delhi/"+i
        print "Processing: "+url
        extracted_data.append(Parser(url))
        sleep(5)
    f=open('event.json','w')
    json.dump(extracted_data,f,indent=4)
 
 
if __name__ == "__main__":
    ReadList()
        
