#!/usr/bin/env python3
# Preamble
# Tandon Jenkins
# 4/20/2022
# Final Project

from http.client import LineTooLong
import re
import dataUpdate
from people import Employee


class EmployeeTest:
    def __init__(self):
        self.initial()
        self.employeeList()
        self.createMenu()
        self.save()

    # defining class object in dictionary
    def initial(self):
        self.employDict = {}
        self.employDict[Employee()] = self.employDict
        self.filename = 'people.txt'

    def employeeList(self):
        self.employDict.clear()
        try:
            with open(self.filename, 'r+') as f:
                # Tries to read lines from file

                for line in f:
                    # eliminates /n and /t in each line
                    line = re.sub(r'\n', '', line)
                    line = re.sub(r'\t', '', line)

                    # holds variables at each comma found per line
                    f, i, d = line.split(',')
                    self.newbie = Employee()  # Employee object
                    first, *last = f.split()  # Splits name into two variables
                    self.newbie.fname = first
                    self.newbie.lname = " ".join(last)
                    self.newbie.id = i
                    self.newbie.dept = d

                    self.employDict.update(
                        {self.newbie.id: self.newbie})  # adds id as key and the entire object as value
        # self.employDict[self.newbie.id] = self.newbie  # adds id as key and the entire object as value
        except FileNotFoundError as error:
            print('Oops\n', error)
            quit()

    # Menu
    def createMenu(self):
        ans = True
        while ans:
            print("""
	1. Look Up Employee
	2. Add new Employee
	3. Change current Employee Attribute
	4. List All Employees
	5. Delete Employee
	6. Quit/Save
			    """)
            ans = input("What would you like to do? ")
            if ans == "1":
                # Displays current list then inputs badge number
                self.printer()
                badge = input("\nEnter Badge Number:")
                self.lookup(badge)
            elif ans == "2":
                self.addNew()
            elif ans == "3":
                self.printer()
                self.editor()
            elif ans == "4":
                self.printer()
            elif ans == '5':
                self.printer()
                delname = input("First name of employee to delete?: ")
                self.delete(str(delname.capitalize()))

            elif ans == '6':
                print('\n Goodbye')
                self.save()
                quit()
            elif ans != "":
                print("\n Not Valid Choice Try again")

    # splits each line  ex. name: John deere... John deere
    def saveFormat(self, line):
        try:
            a, v = line.replace('-', ':').split(':')
            return str(v)
        except ValueError as v:
            print('Formatting error\n', v)

    def save(self):
        updateName = ''
        updateID = ''
        updateDept = ''

        # variable for line breaks
        lastLine = True
        with open('people.txt', 'w+') as f:
            for item, (k, v) in enumerate(self.employDict.items()):
                # inserts line break at end of for loop
                if lastLine is False:
                    f.write('\n')
                    lastLine = True  # Resetting to True becuase new line
                try:
                    v = str(v)
                    for line in v.splitlines():
                        # title is at the end of line and doesnt need comma
                        if 'Name' in line:
                            f.write(str(self.saveFormat(line) + ','))
                            updateName = self.saveFormat(line)
                            lastLine = False
                        elif 'Dept' not in line:
                            f.write(str(self.saveFormat(line) + ','))
                            updateID = self.saveFormat(line)
                            lastLine = False  # False meaning end of line

                        # Runs when dept is found
                        else:
                            v = self.saveFormat(line)
                            f.write(v)
                            updateDept = v

                    # For loop to update database
                    dataUpdate.DataUpdate(
                        updateName, updateID, updateDept)

                except SyntaxError as s:
                    print('Save Error\n', s)
                    break
        quit()

    # Method to add new Employee
    def addNew(self):
        # Loop variable
        add = True
        while add:
            try:
                # Employee object
                newbie = Employee()
                newbie.fname = input('New Employee Portal\nFirst name:')
                newbie.lname = input("\nLast name: ")
                newbie.id = input(str('\nBadge number: '))
                newbie.dept = input('\nDepartment: ')
                self.employDict[newbie.id] = newbie  # Add to dictionary
                add = False
            except:
                print('Invalid Entry')

    def printer(self, request=None):
        # Iterates through and prints __str__
        print()
        if request is not None:
            print(self.employDict[request].__str__(), '\n')
        else:
            for i in self.employDict:
                print(self.employDict[i].__str__(), '\n')

    # Finds and deletes Employee
    def delete(self, valueToFind):
        verify = False
        for item, (k, v) in enumerate(self.employDict.items()):
            # Gets first name variable of object
            nameHold = str(self.employDict[k].fname)
            if valueToFind == nameHold.capitalize():
                # Pops the employee using the key
                self.employDict.pop(k)
                print('Employee', k, 'Deleted')
                verify = True
                break
            else:
                verify = False
                continue
        if verify is False:
            print('Employee "{0}" Not Found'.format(valueToFind))

    # Looks in entire dict for matching badge number
    def lookup(self, person):
        badBadge = True
        for item, (k, v) in enumerate(self.employDict.items()):
            badgeNum = str(self.employDict[k].id)
            if person == badgeNum:
                # sends key to the printer
                self.printer(badgeNum)
                badBadge = False
                break
            else:
                badBadge = True
        if badBadge is True:
            print('Employee not Found')

    def editor(self):
        verify = False
        # Uses first name and iterates through dict for match
        choice = input('Enter Employee first name: ')
        for item, (k, v) in enumerate(self.employDict.items()):
            first = str(self.employDict[k].fname)
            # Once match is found menu
            if choice == first:
                choice = input('1. Edit First Name\n'
                               '2. Edit Last Name\n'
                               '3. Edit Department\n'
                               '4. Quit\n')
                # Updates the variable of the object in the dictionary
                if choice == '1':
                    newData = input('First Name:')
                    # Uses the property setter of the employee class
                    self.employDict[k].fname = newData
                    print('First Name Updated')
                    verify = True

                if choice == '2':
                    newData = input('Last Name:')
                    self.employDict[k].lname = newData
                    print('Last Name Updated')
                    verify = True

                if choice == '3':
                    newData = input('Department:')
                    self.employDict[k].dept = newData
                    print('Department Updated')
                    verify = True

                if choice == '4':
                    verify = True
                    break
        if verify == False:
            print('Employee not Found')


if __name__ == '__main__':
    EmployeeTest()
