#!/usr/bin/python

import sys
import urllib.request
import urllib.error
import re

count = 0

"""
function to download an image
"""
def download_image(url):
  global count
  name = 'image' + str(count) + '.jpg'
  count += 1
  if url.endswith('.jpg') or url.endswith('.gif') or url.endswith('.png') or url.endswith('.bmp'):
    if real_web(url) == False:
       url = 'https:' + url
  try:
    urllib.request.urlretrieve(url, name)
  except Exception as e:
    print ('Error: ' + e + " in " + url + "will not save")

"""
checks to see if url is real, makes sure starts with http or https
"""
def real_web(url):
  if (len(url) != 9 and url[0:8] != 'https://') and (len(url) != 8 and url[0:7] != 'http://'):
    return False
  return True



"""
function to connect to the site
"""
def connect(url):
  #urllib.request.Request requires a real website
  #try to connect to the server
  head = {'User-Agent': 'Mozilla/5.0'}
  try:
    url_request = urllib.request.Request(url, headers = head)
    response_site = urllib.request.urlopen(url_request, timeout = 10)
    site_txt = response_site.read().decode('utf-8')
  except urllib.error.URLError as err:
    if hasattr(err,'code'):
      print('Error: ' + str(err.code))
    if hasattr(err,'reason'):
      print('Error: ' + str(err.reason))
  except urllib.error.HTTPError as err:
    if hasattr(err,'code'):
      print('Error: ' + str(err.code))
    if hasattr(err,'reason'):
      print('Error: ' + str(err.reason))
  return site_txt
 # except urllib.error.ContentTooShortError(msg, content) as err:
 #    print(e)

def main():
  #make sure there are only two console arguments
  if len(sys.argv) != 2:
    print ('ERROR NEED URL')
    sys.exit()

  #name of webpage and header to bypass any rejections i.e. Forbidden 403 since urllib.request.Request requires a real url
  # need to test to make sure it starts with https
  webpage_given = sys.argv[1]
  if real_web(webpage_given) == False:
    print('The webpage probably does not exist, need https:// or http://')
    sys.exit()

  site_txt = connect(webpage_given)
  regex = "(?:href\=\")([^\s]+\.(?:jpg|png|gif|bmp))\""
  line = site_txt
  sites = set(re.findall(regex,line))
  print(site_txt)
  for x in sites:
    print(x)
    download_image(x)

  print(sites)


if __name__ == "__main__":
    main()
