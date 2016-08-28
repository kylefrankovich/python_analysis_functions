__author__ = 'kfranko'


def append_files(master_file_name_path, list_of_files, num_lines_per_sub):
    with open(master_file_name_path, 'a') as output:  # append to first file (or master file of subject
        # if simply adding new subjects)
        # add carriage return:
        # output.write('this_is_a_text_string')
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


file_path = '/Users/kfranko/Google Drive/Young_Hall_data_analysis' \
            '/analysis_scripts/analysis_functions/python_analysis_functions' \
            '/YH_LOTP_mk6_master_data.txt'

file_path = '/Users/kylefrankovich/Google Drive/Young_Hall_data_analysis/analysis_scripts/analysis_functions/python_analysis_functions/YH_LOTP_mk6_master_data.txt'


file_list_mk2 = ['3_LOTP_ladies_and_gentlemen.txt','4_LOTP_ladies_and_gentlemen.txt',
             '5_LOTP_ladies_and_gentlemen.txt','6_LOTP_ladies_and_gentlemen.txt',
             '8_LOTP_ladies_and_gentlemen.txt','9_LOTP_ladies_and_gentlemen.txt',
             '10_LOTP_ladies_and_gentlemen.txt','11_LOTP_ladies_and_gentlemen.txt',
             '13_LOTP_ladies_and_gentlemen.txt','14_LOTP_ladies_and_gentlemen.txt',
             '15_LOTP_ladies_and_gentlemen.txt', '16_LOTP_ladies_and_gentlemen.txt',
             '17_LOTP_ladies_and_gentlemen.txt','18_LOTP_ladies_and_gentlemen.txt',
             '20_LOTP_ladies_and_gentlemen.txt','23_LOTP_ladies_and_gentlemen.txt',
             '24_LOTP_ladies_and_gentlemen.txt','25_LOTP_ladies_and_gentlemen.txt',
             '26_LOTP_ladies_and_gentlemen.txt']

file_list_mk3 = ['2_LOTP_ladies_and_gentlemen_mk3.txt']

file_list_LOTP_mk6 = ['08_LOTP_mk6.txt','09_LOTP_mk6_fixed.txt',
                      '08_LOTP_mk6.txt','10_LOTP_mk6.txt',
                      '12_LOTP_mk6.txt','15_LOTP_mk6.txt',
                      '16_LOTP_mk6.txt','17_LOTP_mk6.txt',
                      '19_LOTP_mk6.txt','20_LOTP_mk6.txt',
                      '21_LOTP_mk6.txt','22_LOTP_mk6.txt',
                      '23_LOTP_mk6.txt','24_LOTP_mk6.txt',
                      '26_LOTP_mk6.txt','1024_LOTP_mk6.txt',
                      '1030_LOTP_mk6.txt',]

len(file_list_LOTP_mk6)

import os

os.getcwd()

os.listdir(os.getcwd())

append_files(file_path,file_list_LOTP_mk6, 257)

print file_list
