import urllib.request
import json
def locu_search(address,city):
    api_key = 'bf8dfc5feaf8be58'
    url = 'https://api.eatstreet.com/publicapi/v1/restaurant/search?method=both&access-token=' + api_key

    address_mod = address.replace(' ', '+')
    city_mod = city.replace(' ','+')
    final_url = url + "&street-address=" + address_mod + "," + city_mod

# request = urllib2.Request(final_url, None,"")
    print(final_url)
    with urllib.request.urlopen(final_url) as url1:
        json_obj = url1.read()
    #
    # json_obj= urllib3.urlopen(final_url)

# json_obj = urllib2.urlopen(final_url)
    data = json.loads(json_obj)


    for item in data['restaurants']:
        print ('\t\t' + item['name'] + '\n')
        restaurantkey = item['apiKey']
        menuurl = 'https://api.eatstreet.com/publicapi/v1/restaurant/' + restaurantkey + '/menu?includeCustomizations=false&access-token=' + api_key
        with urllib.request.urlopen(menuurl) as url2:
            json_obj = url2.read()
        # json_obj = urllib3.urlopen(menuurl)
        menudata = json.loads(json_obj)
        for item in menudata:
            print(item['name'].upper())
            for item2 in item['items']:
                print(item2['name'])


locu_search('701 W Stadium Ave','West Lafayette')


appid = '8415a1a1'
appkey = 'f853ce28eb141c235f6ee9176812d652'
foodstr = '1 large apple'
foodstr_mod = foodstr.replace(' ', '%20')

nutritionurl = 'https://api.edamam.com/api/nutrition-data?app_id='+appid+'&app_key='+appkey+'&ingr=1cheeseburger'

with urllib.request.urlopen(nutritionurl) as url3:
    json_obj_2 = url3.read()

nutritiondata = json.loads(json_obj_2)
for item in nutritiondata['totalNutrients']:
    print(item)
    # print item['label'],item['quantity'], item['unit']

#
# import requests
# headers = {'x-access-token': 'bf8dfc5feaf8be58'}
# r = requests.get("https://api.eatstreet.com/publicapi/v1/restaurant/09aa1f99e7792411144247b91fbcb2f349e8e58504b5a530/menu?includeCustomizations=false",headers=headers)
# # r = requests.get("https://api.eatstreet.com/publicapi/v1/restaurant/search?method=both&street-address=701+W+Stadium+Ave,West+Lafayette",headers=headers)
# r.json()
#
#
# data = r.json()
# for item in data:
#     print item['name'].upper()
#     for item2 in item['items']:
#         print item2['name']