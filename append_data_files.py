__author__ = 'kfranko'

def append_files(output_path, list_of_files, out_filename):
    with open(output_path, 'w') as out_filename:
    for fname in list_of_files:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)