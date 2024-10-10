Working in rekordbox 7.0.4

# rekordbox playlist formatter

## About

Automatically format rekordbox playlists or histories into neat .txt files with artist and track.

## Usage

1. Export the desired rekordbox playlist or history by right clicking it in the playlists tab, click "Export to a playlist file" -> "Export to a playlist file (.txt)".

2. Save or place the `*.txt` file in the same folder as the `rbpf.py` file.

3. On your preferred command line thingy (GIT Bash, Powershell, Command Prompt, ...), go to the file location with the playlist file, and enter the command:

```
python rbpf.py FILENAME [-ct]
```

The file will be saved as `FILENAME_out.txt` in the same folder.

Default line output format is `[n]: [artist] - [track]`

You may enter the file name with or without the `.txt` ending.

Options:

- t	output with timestamp template instead of enumeration
- c	output with colon in between artist and track instead of dash

Examples:

1. I want my text outputted with enumeration and dashes
```
python rbpf.py jazzy.txt
```
- 1: Bonobo - Black Sands
- 2: Bonobo - Kiara
- ...
		
2. I want my text outputted with timestamp templates and dashes
```
python rbpf.py jazzy.txt -t
```
- 00:00 Bonobo - Black Sands
- 00:00 Bonobo - Kiara
- ...
	
3. I want my text outputted with timestamp templates and colons
```
python rbpf.py jazzy -ct
```
- 00:00 Bonobo: Black Sands
- 00:00 Bonobo: Kiara
- ...