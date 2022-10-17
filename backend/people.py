#!/usr/bin/env python3
# Preamble
# Tandon Jenkins
import re


class Employee(object):
    def __init__(self, fname='', lname='', id='', dept=''):
        self.__initialize(fname, lname, id, dept)
        self.__check_ID()

    # Initialzing variables
    def __initialize(self, fname, lname, id, dept):
        self._fname = fname
        self._lname = lname
        self._id = id
        self._dept = dept

    # get properties
    @property
    def fname(self):
        return self._fname

    @property
    def lname(self):
        return self._lname

    @property
    def id(self):
        return self._id

    @property
    def dept(self):
        return self._dept

    # setter properties
    @fname.setter
    def fname(self, f):
        self._fname = f

    @lname.setter
    def lname(self, l):
        self._lname = l

    @id.setter
    def id(self, i):
        self._id = i
        self.__check_ID()

    @dept.setter
    def dept(self, d):
        self._dept = d

    # Checks that id is only numbers
    def __check_ID(self):
        loop = True
        self._id = self._id.replace(" ", "")  # replaces whitespace
        while loop:
            result = re.sub("[0-9]+", '', self._id)  # regex function
            # If no letters are in id, breaks loop
            if len(result) == 0:
                loop = False
            else:
                print('\n"{0}" in {1} invalid'.format(result, self._id))
                self.renew_id()

    def renew_id(self):
        x = input('Re-enter ID with only integers:')
        if x == '':
            self._id = '1'
        # Using setter property
        self.id = x

    # Concatenated data
    def __str__(self):
        # .replace Removes whitespace
        strung = str('Name:{0} {1}\nID:{2}\nDept:{3}'.format(self.fname, self.lname, self._id,
                                                             self.dept.replace(
                                                                 " ", ""),))
        return strung


if __name__ == '__main__':
    Employee()
