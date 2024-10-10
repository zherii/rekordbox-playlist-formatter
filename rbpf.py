from os import startfile
from platform import system
from subprocess import run
from sys import argv


def get_filenames(f_input):
    if '.txt' == f_input[-4:]:
        f_output = f_input[:-4] + '_out.txt'
    else:
        f_output = f_input + '_out.txt'
        f_input += '.txt'
    return f_input, f_output


def get_track_info(line):
    artist = line[3]
    if not artist:
        artist = '**NO ARTIST NAME**'
    track = line[2]
    if not track:
        track = '**NO TRACK NAME**'
    return artist, track


def open_file(file_name):
    if system() == 'Windows':
        startfile(file_name)
    elif system() == 'Darwin':  # mac os
        run(['open', file_name])
    else:  # linux
        run(['xdg-open', file_name])


def main():
    filename_input, filename_output = get_filenames(argv[1])

    # choose between enumerated (n: ) or time stamped (00:00) lines
    # choose between dash or dots between artist and track (artist - track, or artist: track)
    timestamp = False
    separator = ' - '
    COLON = 'c'
    TIMESTAMPS = 't'

    if len(argv) > 2:
        args = argv[2]
        if args[0] == '-':
            timestamp = TIMESTAMPS in args

            if COLON in args:
                separator = ': '

    try:
        r = open(filename_input, 'r', encoding='utf-16-le')
        w = open(filename_output, 'w', encoding='utf-16-le')

        # skip first header line
        next(r)

        line_num = 1
        for line in r:
            line_array = line.split("\t")

            artist, track = get_track_info(line_array)

            if timestamp:
                w.write(f'00:00 {artist}{separator}{track}\n')
            else:
                w.write(f'{line_num}: {artist}{separator}{track}\n')
                line_num += 1

        r.close(), w.close()

    except OSError:
        input('File not found, press enter to continue ')
        return

    file_open = input('Successfully wrote to file, open file? (y/n) ')
    if 'y'.startswith(file_open):
        open_file(filename_output)


if __name__ == '__main__':
    main()
