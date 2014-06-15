#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os



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

    for jpg_file in filenames:
        if "_TGMG" in jpg_file: break
        counter+=1

        if counter <= half_number_of_pages:
            new_number = (counter*2)-1
        else:
            new_number = (total_pages - (counter-1))*2

        full_old_path =os.path.join(path,jpg_file)
        full_new_path =os.path.join(path,str(new_number)+"_TGMG.jpg")
        os.rename(full_old_path, full_new_path)

        # print "("+str(counter) + "->" + str(new_number)+") "
