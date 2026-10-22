# Builds build/artifact.html (Artifact flavor) from index.html (GitHub Pages flavor)
import re,os
s=open('index.html').read()
css=open('vendor/leaflet.css').read().replace('url(images/','url(vendor/images/')
a=s
a=re.sub(r'^<!doctype html>\s*<html lang="en">\s*<head>\s*','',a)
a=a.replace('<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n','')
a=a.replace('<title>Cornerstone General Contractors — Property Survey</title>','<title>Cornerstone Property Survey</title>\n<meta name="claude:viewport-fit-sides" content="cover">')
a=a.replace('<link rel="stylesheet" href="vendor/leaflet.css">','<style>'+css+'</style>')
a=a.replace('<script src="vendor/leaflet.js"></script>','<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>')
a=a.replace('</head>\n<body>\n','').replace('</body>\n</html>','')
a=a.replace('.nav{position:sticky;top:0;','.nav{position:sticky;top:env(safe-area-inset-top,0px);')
os.makedirs('build',exist_ok=True); open('build/artifact.html','w').write(a); print(len(a))
