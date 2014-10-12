#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys


def fake_duplex(path):
    """
    * Takes in a path to a folder full of jpg files and renames the
      jpg files so that they are in Fake Duplex Order.
    * This allows you to scan all one side, flip the comic around and scan
      the other side.
    * Then Just run this script on the output and it will put the pages in the correct order.
    * Then you can zip up the directory and have a cbz file, or save to pdf.
    :param path:
    """
    filenames = next(os.walk(path))[2]
    counter=0
    total_pages = len(filenames)
    half_number_of_pages = total_pages/2
    duplex_done_suffix="_TGMG"

    for jpg_file in filenames:
        if duplex_done_suffix in jpg_file: break
        counter+=1

        if counter <= half_number_of_pages:
            new_number = (counter*2)-1
        else:
            new_number = (total_pages - (counter-1))*2

        full_old_path =os.path.join(path,jpg_file)
        new_number_str = '0'+str(new_number)
        if new_number < 10: new_number_str='0'+new_number_str
        full_new_path =os.path.join(path,new_number_str+ duplex_done_suffix+".jpg")
        os.rename(full_old_path, full_new_path)

        print "Renamed:"+full_old_path+" to "+full_new_path


if __name__ == '__main__':
    if (len(sys.argv) > 1):
        path =sys.argv[1]
        print path
        fake_duplex(path)
        print "Finished! Warning Only do this once!"
    else:
        print "You need to provide the path to the folder of images you want duplexed!"
