__author__ = 'kfranko'


def append_files(master_file_name_path, list_of_files, num_lines_per_sub):
    with open(master_file_name_path, 'a') as output:  # append to first file (or master file of subject
        # if simply adding new subjects)
        for fname in list_of_files:
            with open(fname) as infile:
                # print 'number of lines:', sum(1 for line in infile), '\n'
                if sum(1 for line in infile) == num_lines_per_sub:
                    print 'processing subject file:', fname, '\n'
                    with open(fname) as infile:
                        next(infile, None)  # skip header for all non-first files
                        for line in infile:
                            output.write(line)
                else:
                    print '***** subject has incorrect number of trials for this experiment:', fname