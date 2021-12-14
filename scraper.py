import requests
from bs4 import BeautifulSoup
youtube_url='https://www.youtube.com/feed/trending'

## doesnot exexute the javascript
response=requests.get(youtube_url)
print('Status Code',response.status_code)

## Now we can write this thing in the one file 
with open('trending.html','w') as f:
  f.write(response.text)

## Now to work with html docuemnt we use beaustiful soap 
## We can papse info from html docuemst using beautiful saop
## W ehave created one object
doc=BeautifulSoup(response.text,'html.parser')
print('Page title',doc.title.text)
## To just want the titile text fo trnd

video_divs=doc.find_all('div',class_='ytd-video-renderer')

print(f'Found {len(video_divs) } videos')








print('Hello World')