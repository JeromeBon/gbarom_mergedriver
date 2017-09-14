## Dependencies
* Python 3

## Usage
1. Put gbamerge.py somewhere on your drive.
2. Add this stanza in the .git/config file of your local repo:
```
[merge "gbamerge"]
	name = A custom merge driver for roms
	driver = pathtothisfile %O %A %B %L
	recursive = binary
```
3. Add this line in the .git/info/attributes (or .gitattributes) of your local repo:
   *.gba merge=gbamerge
