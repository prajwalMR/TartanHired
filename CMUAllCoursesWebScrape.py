#!/usr/bin/env python
# coding: utf-8

# In[99]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import json


# In[5]:


URL = "https://enr-apps.as.cmu.edu/open/SOC/SOCServlet/search"


# In[75]:


driver = webdriver.Chrome("/Users/prajwalmr/Downloads/chromedriver")
driver.get(URL)

# def setup_driver():
#     driver_path = "/Users/prajwalmr/Downloads/chromedriver"
#     chrome_service = Service(driver_path)
#     chrome_options = Options()
#     chrome_options.headless = True
#     driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
#     return driver

# driver = setup_driver()

# driver.get(URL)

sem = driver.find_element_by_name("SEMESTER")
sem.send_keys("Fall 2021")
submit = driver.find_element_by_name("SUBMIT")
submit.click()

links = driver.find_elements_by_tag_name("a")
print(len(links))


# In[93]:


course_object = {}


# In[101]:


import time

for index in range(9,len(links)):
    print(str(index) + links[index].text)
    
    links = driver.find_elements_by_tag_name("a")
    
    if(links[index].text != ""):
        try:
            links[index].click()
            time.sleep(2)

            modal_title = driver.find_elements_by_class_name("modal-title")
            
            for i in modal_title:
                modal_data = i.text.split("\n")[1].split(" ")
                course_no = modal_data[0]
                course_title = ''.join(str(elem + " ") for elem in modal_data[2:]) 
                print(course_title + " -> " + course_no)
                
                cur_course_object = {}
                cur_course_object['course_no'] = course_no


#             course_data = modal_title[0].split(" ")
#             course_no = course_data[0]
#             course_title = course_data[1]
#             print(course_no , " -> " , course_title)

            modal_content = driver.find_elements_by_id("course-detail-description")

            description = driver.find_elements_by_tag_name("p")

            for p in description:
                if(len(p.text) > 0):
                    print(p.text)
                    cur_course_object['course_description'] = p.text

            course_object[course_title] = cur_course_object

            close_button = driver.find_elements_by_tag_name("button")
            close_button[1].click()

        except Exception as e :
            print("error : " + str(e.args) )

     


# In[102]:


print(len(course_object))


# In[103]:


all_courses_file = open("all_cmu_courses.json", "w")
json.dump(course_object, all_courses_file)
all_courses_file.close()


# In[104]:


with open('all_cmu_courses.json') as f:
    all_cmu_courses_data = json.load(f)


# In[106]:


len(all_cmu_courses_data)


# In[168]:


skills_needed = ['data science']


# In[169]:


recommended_courses = []

for course,description in all_cmu_courses_data.items():
    for skill in skills_needed:
        if (skill in course.lower()) or (skill in description['course_description'].lower()):
            recommended_courses.append({course:description['course_no']})
87
recommended_courses


# In[ ]:




