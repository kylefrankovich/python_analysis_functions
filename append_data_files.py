__author__ = 'kfranko'

def append_files(master_file_name_path, list_of_files):
    with open(master_file_name_path, 'a') as output: # append to first file (or master file of subject if simply adding new subjects)
        for fname in list_of_files:
            with open(fname) as infile:
                next(infile, None) # skip header for all non-first files
                for line in infile:
                    output.write(line)


for fname in list_of_files:
    print fname

append_files(master_file_name_path, list_of_files)