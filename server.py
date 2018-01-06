# -*- coding: <UTF-8> -*-
import os, os.path, glob
from pathlib import Path

inList = glob.glob("./in/in*.html")
outList = glob.glob("./out/out*.html")

# functions
def generateRaport(message):
  try:
    with open("./raport/raport.html", "w", encoding="utf-8") as f:
      f.write(message)
      f.close()
  except IOError:
    print(IOError)


def generateDiv(name, data):
  message = """
    <div class="page-content__wrapper">
      <h2 class="page-content__title">Filename: %s</h2>
      <xmp class="page-content__data">%s</xmp>
    </div>"""
  
  div = message % (name,data)
  return div

#Opening input files
try:
  inData = dict()
  for path in inList:
    with open(path, "r", encoding="utf-8") as f:
      inData[path] = f.read()
      f.close()
except IOError:
    print(IOError)

# Opening output files
try:
  outData = dict()
  for path in outList:
    with open(path, "r", encoding="utf-8") as f:
      outData[path] = f.read()
      f.close()
except IOError:
    print(IOError)


inContent = ""
for ik,iv in inData.items():
  inContent += generateDiv(ik, iv)

outContent = ""
for ok, ov in outData.items():
  outContent += generateDiv(ok, ov)



template = """<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Raport JHTMLLET</title>
  <link rel="stylesheet" href="./style.css">
  <link href="https://fonts.googleapis.com/css?family=Lato|Merriweather" rel="stylesheet"> 
</head>
<body>
<div class="page-wrapper">
  <header class="page-header">
    <h1 class="page-header__title">JHTMLLET Raport</h1>
    <p class="page-header__description">JHTMLLET - Zamiana małych liter z tagów pliku HTML na litery wielkie</p>
  </header>
  <section class="page-content__data-wrapper">
    <section class="page-content__data--in">
    %s
    </section>
    <section class="page-content__data--out">
    %s
    </section>
  </section>
  <footer class="page-footer">Łukasz Tyszkiewicz - Semestr III - Informatyka 2017/2018 - Wydział Matematyki Stosowanej</footer>
</div>
</body>
</html>
"""

wrapper = template % (inContent, outContent)

generateRaport(wrapper)





