# My-Stuff-File-Name-Formatter
Renames .SZS files in a directory to be compatible with a MKWii CTGP "My Stuff" folder.

The script will attempt to rename tracks with no slot overlap, but sometimes that is impossible (such as having multiple tracks on slot +6.2) and in that case it will leave files with overlapping slots unchanged and write a text file saying which slot it should be replaced with.
### Requirements
* Computer
* Python 3.8+
* [Wiimm's SZS Toolset](https://szs.wiimm.de/)
