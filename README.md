A Migration script of todo lists from Basecamp to Acunote
=========================================================

Description
-----------
This script if made for those who want to migrate their todo lists from Basecamp to Acunote. As Acunote does not have (yet) an API, this script is making API calls to get the data from Basecamp and outputs a CSV file that you can import in Acunote.


Usage
-----
Edit the file `params.py` according to your credentials :
<pre>
# Basecamp URL for API calls
url = "https://example.basecamphq.com"

# Basecamp API key
apikey = "04f69569a36d306701238466d5ea12cb097b959d"

# Users
# List here all the user IDs in Basecamp and associate a name in Acunote :
# Basecamp IDs => Acunote names
creatorNames = {
    '7248751' : "quentin",
    '1122334' : "bob",
}
</pre>

Give the todo list ID in argument to the script and it will output the CSV file to import in Acunote :
<pre>
$ python migration-basecamp-acunote.py 3248324
Level,Number,Description,Tags,Owner,Status,Priority,Estimate,Remaining,Wiki,Watchers,Related,Duplicate,Version 1
,"1","Item B",,"quentin","Not Started",,,,,,,,
,"1","Item C",,"quentin","Completed",,,,,,,,
,"2","Item A",,"bob","Not Started",,,,,,,,
,"3","Item D",,"blabla","Not Started",,,,,,,,
</pre>