#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:51:32 2020

@author: Mukut Ranjan Kalita
Objective 
Today, we're delving into Inheritance. Check out the attached tutorial for learning materials and an instructional video!
Task 
You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.
Complete the Student class by writing the following:
A Student class constructor, which has  parameters:
A string, firstname
A string, lastname
An integer,idnumber
An integer array (or vector) of test scores, scores
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
  Input Format
The locked stub code in your editor calls your Student class constructor and passes it the necessary arguments. It also calls the calculate method (which takes no arguments).
You are not responsible for reading the following input from stdin: 
The first line contains , , and , respectively. The second line contains the number of test scores. The third line of space-separated integers describes .
Constraints



Output Format
This is handled by the locked stub code in your editor. Your output will be correct if your Student class constructor and calculate() method are properly implemented.  
"""

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    
    def __init__(self,firstName, lastName, idNumber,scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    #   Function Name: calculate
    def calculate(self):
        total_score = sum(self.scores)/len(self.scores)
        if 90<=total_score<=100:
            return 'O'
        if 80<=total_score<90:
            return 'E'
        if 70<=total_score<80:
            return 'A'
        if 55<=total_score<70:
            return 'P'
        if 40<=total_score<55:
            return 'D'
        if total_score<40:
            return 'T'
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())