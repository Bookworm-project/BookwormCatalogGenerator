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

