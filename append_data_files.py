__author__ = 'kfranko'

def append_files(master_file_name_path, list_of_files):
    with open(master_file_name_path, 'w') as output:
        for fname in list_of_files:
            if fname == list_of_files[0]: # only open entire file (including header) if it's the first file
                with open(fname) as infile:
                    for line in infile:
                        output.write(line)
            else:
                with open(fname) as infile:
                    next(infile) # skip header for all non-first files
                    for line in infile:
                        output.write(line)


append_files(master_file_name_path, list_of_files)