# -*- coding: utf-8 -*-
"""
Write a program to keep track of conference attendees. For each attendee,
your program should keep track of name company, state and email address.
Your program should allow users to do things such as add a new attendee,
display information of attendee, delete an attendee, list the names and email
addresses of all attendees from a given state.
"""

class Person:
     #Constructor
    def __init__(self, name, state, email):
        self.name = name
        self.state = state
        self.email = email
        
    #Methods    
    def getName(self):
        return self.name
    
    def getState(self):
        return self.state
        
    def getEmail(self):
        return self.email
    

class Attendee(Person):
    def __init__(self, name, state, email, company):
        super().__init__(name,state,email)
        self.company = company
        
    def getCompany(self):
        return self.company
    
class Conference:
    def __init__(self, name):
        self.name = name
        self.attendees = []
        
    def addAttendee(self, attendee):
        self.attendees.append(attendee)
        
    def deleteAttendee(self,att):
            self.attendees.remove(att)
    
    
    def displayInformation(self,att):
        for attendee in self.attendees:
            if attendee == att:
                print("Information about " + attendee.getName() + ":")
                print("Email: " + attendee.getEmail())
                print("State: " + attendee.getState())
                print("Company: " + attendee.getCompany())
                return 
        print("Attendee not found")
        return 
    
    def getAttendeesByState(self,state):
        for attendee in self.attendees:
            if attendee.getState() == state:
                print("Information about " + attendee.getName() + ":")
                print("Email: " + attendee.getEmail())
                print("State: " + attendee.getState())
                print("Company: " + attendee.getCompany())
                
        
    
#Create Attendees    
att1 = Attendee("Alex", "Sverige", "a@gmail.com", "Chalmers")
att2 = Attendee("Lisa", "Sverige", "l@gmail.com", "KTH")
att3 = Attendee("Sven", "Sverige", "s@gmail.com", "Chalmers")

#Create conference and add attendees
conf  = Conference("Chalemrs conference")
conf.addAttendee(att1)
conf.addAttendee(att2)
conf.addAttendee(att3)

#Perform actions
conf.displayInformation(att1)
conf.getAttendeesByState("Sverige")
conf.deleteAttendee(att1)
conf.displayInformation(att1)



