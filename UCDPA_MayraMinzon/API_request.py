#import the library 'requests'
import requests

request = requests.get('https://api.github.com')

#print status code: 200 means everything went ok, 404 server not found
print(request.status_code)
if request.status_code == 200:
    print('Success!')
elif request.status_code == 404:
    print('Not Found.')

print(request.text)