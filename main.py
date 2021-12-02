#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 04:59:44 2021

@author: prajwalmr
"""

import PySimpleGUI as sg
import json

import CMUCourseRecommender
import ResumeParser

sg.theme('Reddit')
font = ("Arial", 11)

layout = [  
            [sg.Text("This tool finds the skills you are yet to acquire and recommends courses to acquire them, to get the job you always wanted.")],
            [sg.Text("Let's get some basic details about your career goals")],
            [sg.Text()],
            
            [sg.Text("Upload your resume")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse()],
            [sg.Text('Enter the job titles you are looking for as comma sepaerated values'), sg.InputText()],
            [sg.Button('Search CMU Courses')],[sg.Button('Search Online Courses')]
         ]

# Create the Window
window = sg.Window('TartanHired', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
        
    if event == 'Search CMU Courses':
        resume_path = values[0]
        if(resume_path == "" or resume_path==None or (".pdf" not in resume_path)):
            sg.popup('Invalid file path for resume')
        else:
            current_skills = set(ResumeParser.get_current_skills(resume_path))
        
            demanded_skills = set(['java', 'sql'])
            
            required_skills = demanded_skills - current_skills
            
            print(required_skills)
            req_skill_list = "".join(skill + " " for skill in required_skills)
            
            recommended_courses = CMUCourseRecommender.get_recommended_courses(list(required_skills))
    
            layout = [ 
                        [sg.Button('Back')],
                        [sg.Text('Recommended CMU Courses for skills : ' + req_skill_list)],
                        *[[sg.Text(course),] for course in recommended_courses]
                        
                     ]
            
            window1 = sg.Window('TartanHired').Layout(layout)
            window.Close()
            window = window1
            
            print(type(values[0]))
    
    if event == 'Back':
        layout = [  
                    [sg.Text("This tool finds the skills you are yet to acquire and recommends courses to acquire them, to get the job you always wanted.")],
                    [sg.Text("Let's start with some basic details about your career goals")],
                    [sg.Text()],
                    
                    [sg.Text("Upload your resume")], [sg.Text("Choose a file: "), sg.Input(), sg.FileBrowse()],
                    [sg.Text('Enter the job titles you are looking for as comma sepaerated values'), sg.InputText()],
                    [sg.Button('Search CMU Courses')],[sg.Button('Search Online Courses')]
                 ]
        window1 = sg.Window('TartanHired').Layout(layout)
        window.Close()
        window = window1
    

window.close()
    
    
