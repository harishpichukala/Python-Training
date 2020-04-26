import requests
url="https://www.nltk.org/"
output=requests.get(url) # Output is an object
f=open("F:\\hello123.html",'w')
f.write(output.text)
f.close()

