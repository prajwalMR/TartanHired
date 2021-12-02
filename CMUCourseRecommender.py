#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 05:02:27 2021

@author: prajwalmr
"""

import json

def get_recommended_courses(skills_needed):
    with open('all_cmu_courses.json') as f:
        all_cmu_courses_data = json.load(f)
    
    recommended_courses = []

    for course,description in all_cmu_courses_data.items():
        for skill in skills_needed:
            print(type(skill))
            if (skill.strip() in course.lower()) or (skill.strip() in description['course_description'].lower()):
                recommended_courses.append({course:description['course_no']})
    return recommended_courses