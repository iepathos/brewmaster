#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import argparse
from subprocess import check_output
from datetime import datetime

log_filename = os.path.expanduser('~/brewmaster.log')


class BrewMaster(object):

    def __init__(self, log_filename=log_filename):
        self.log_filename = log_filename

    def check_log(self, func, text):
        try:
            os.makedirs(os.path.dirname(self.log_filename), exist_ok=True)
        except:
            pass
        func(self.log_filename, text)

    def add_to_log(self, file_handle, text):
        with open(file_handle, "a") as f:
            f.write(str(text))

    def log(self, text):
        self.check_log(self.add_to_log, text)

    def update_packages(self):
        print("Running brew cask update ....")
        output = check_output(["brew", "cask", "update"])
        print("Saving updates to log %s" % self.log_filename)
        self.log(str(datetime.utcnow()) + "\n" + output.decode("utf-8"))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='BrewMaster - Automatic Updates and Logging for HomeBrew'
        )
    parser.add_argument("--log", "-l")

    args = parser.parse_args()
    if args.log:
        brewmaster = BrewMaster(args.log)
        brewmaster.update_packages()
    else:
        brewmaster = BrewMaster(log_filename)
        brewmaster.update_packages()
