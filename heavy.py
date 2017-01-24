#!/usr/bin/env python
# Notes:
# Author: Marcin Taracha
# Version: 1.0

import os
import subprocess
import time

basedir = os.path.abspath(os.path.dirname(__file__))

class Heavy(object):
    """Class that creates CPU heavy objects"""
    def __init__(self, id=0, file_name='random.img', compress='True'):

        self.file_name = file_name
        self.id = id
        self.compress = compress
        self.basedir = basedir
        self.time = 0
        self.data = {}



    def __del__(self):

        self.data['time'] = self.time
        
        print "Operation took: %s" % self.time

        if os.path.exists(self.file_name):
            try:
                if (self.compress == "True"):
                    os.remove(self.file_name + ".tar.gz")
                print ("Removing: " + self.file_name)
                os.remove(self.file_name)
            except Exception as e:
                print ("Error: %s - %s." % (e.self.file_name,e.strerror))
                return 400
        else:
            print("Sorry, I can not remove %s file." % self.file_name)

        return self.data, 200

    def get_time(self):

        return 0

    def create_file(self):
        start_time = time.time() 
        try:
            print ("Creating: " + self.file_name)
            #subprocess.call(["dd", "if=/dev/urandom", "of="+self.file_name, "count=64", "bs=1M"])
            file = open(self.file_name, 'w+')
        except Exception as e:
            raise e
            return "Bad request", 400

        if (self.compress == "True"):
            self.compress_file()

        self.time = time.time() - start_time
        self.data['time'] = self.time

        #content = {'please move along': 'nothing to see here'}
        return self.data, 200


    def compress_file(self):

        try:
            subprocess.call(["tar", "-czvf", self.file_name+".tar.gz", self.file_name])
        except Exception as e:
            raise e
            return 400

        return 200

if __name__ == '__main__':
    heavy_operation = Heavy()
