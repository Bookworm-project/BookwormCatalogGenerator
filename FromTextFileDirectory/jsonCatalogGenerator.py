#!/usr/bin/env python

import os
import re

"""
This script assumes that all txt files are appropriately named with the associated metadata and located in a selected directory

e.g. Running the script at the following directory /my/file/path/text/raw  :

/text
--/ raw
----/ USA_15SEPT2008_GOV.txt
----/ USA_16SEPT2008_GC.txt
----/ USA_16SEPT2014_GOV.txt
----/ USA_16SEPT2014_GC.txt

will return a jsoncatalog file containing

{"date": "2008-9-15", "country": "USA", "recipient": "GOV", "filename": "USA_15SEPT2008_GOV"}
{"date": "2008-9-16", "country": "USA", "recipient": "GC", "filename": "USA_16SEPT2008_GC"}
{"date": "2014-9-16", "country": "USA", "recipient": "GC", "filename": "USA_16SEPT2014_GC"}
{"date": "2014-9-16", "country": "USA", "recipient": "GOV", "filename": "USA_16SEPT2014_GOV"}

"""

# REPLACE WITH YOUR FILE PATH
filepath = "/Users/muhammadsaadshamim/Desktop/BookwormCatalogGenerator/FromTextFileDirectory/raw/text"


# parsing dates of the form: 15SEPT2008
dateStringParser = re.compile("([0-9]+)([a-zA-Z]+)([0-9]+)")
months = ["JAN","FEB","MARCH","APRIL","MAY","JUNE","JULY","AUG","SEPT","OCT","NOV","DEC"]

def parseDate(combinedDate):
	splitDate = dateStringParser.match(combinedDate)
	date = splitDate.group(1)
	month = splitDate.group(2)
	month = str(months.index(month) + 1)
	year = splitDate.group(3)
	return year, month, date


def parseFilenameForMetadata(filename):
	# this example is for something of the form
	# USA_15SEPT2008_GOV
	splitName = filename.split("_")
	country = splitName[0]
	year, month, date = parseDate(splitName[1])
	recipient = splitName[2]
	return "{\"date\": \""+year+"-"+month+"-"+date+"\", \"country\": \""+country+"\", \"recipient\": \""+recipient+"\", \"filename\": \""+filename+"\"}"


listOfFiles = []
for txtFileName in os.listdir(filepath):
    if txtFileName.endswith(".txt"):
    	listOfFiles.append(txtFileName.replace(".txt",""))


jsonOutputFile = open("jsoncatalog.txt","w")
for txtFileName in listOfFiles:
	try:
		jsonOutputFile.write(parseFilenameForMetadata(txtFileName)+"\n")
	except Exception as inst:
		print inst
		print txtFileName
jsonOutputFile.close()
