#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 05:05:33 2021

@author: prajwalmr
"""

import slate3k as slate
import json
import re

def get_current_skills(resume_path):
    
    with open(resume_path, 'rb') as f:
        pdf = slate.PDF(f)
        
    pdf1 = pdf[0]
    
    re.sub(r'[^\x00-\x7f]',r'', pdf1)
    
    bag = set(['c++', 'c', 'python', 'nodejs', 'javascript'])
    
    resume_words = pdf1.split(" ")
    
    current_skills = set()
    
    for word in resume_words:
        for skill_word in bag:
            if(skill_word in word.lower()):
                current_skills.add(skill_word)
                
    print(current_skills)
    return current_skills