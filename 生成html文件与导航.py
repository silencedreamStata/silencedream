# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:27:00 2024

@author: 85318
"""

import os
import re



directory = r'D:\github\silencedream\silencedream\EndProblem'
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        os.remove(os.path.join(directory, filename))


def extract_video_divs(md_content):
    """
    Extracts video divs from the markdown content using a regular expression.
    """
    video_div_pattern = r'<div style="text-align: center;">\s*<div style="border: 2px solid #ccc; padding: 10px; display: inline-block;">.*?</div>\s*</div>'
    video_divs = re.findall(video_div_pattern, md_content, re.DOTALL)
    return video_divs

def create_html_with_video(video_div, html_template_path=r"D:\github\ddd\EndProblem\subpageForEndProblem.html"):
    """
    Creates an HTML content by inserting the video_div into the HTML template.
    """
    with open(html_template_path, 'r',encoding = 'utf-8') as file:
        template = file.read()

    # Replace the placeholder in the template with the video div
    before_content = '<h2>教学视频</h2>'
    html_content = template.replace(before_content, video_div)
    return html_content

def process_markdown_files(directory,html_template_path=r"D:\github\ddd\EndProblem\subpageForEndProblem.html"):
    """
    Processes all markdown files in the specified directory.
    For each markdown file, it extracts video divs and creates corresponding HTML files.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            md_path = os.path.join(directory, filename)
            with open(md_path, 'r',encoding = 'utf-8') as md_file:
                md_content = md_file.read()

            video_divs = extract_video_divs(md_content)
            if video_divs:
                # Use the first video div found (or modify as needed for multiple videos)
                html_content = create_html_with_video(video_divs[0], html_template_path)
                html_filename = os.path.splitext(filename)[0] + '.html'
                html_path = os.path.join(directory, html_filename)
                with open(html_path, 'w',encoding = 'utf-8') as html_file:
                    html_file.write(html_content)


process_markdown_files(r"D:\github\silencedream\silencedream\EndProblem")




import pyperclip
filehtml = r'D:\github\ddd\Writing'
liFilePath = ''
for eachFile in os.listdir(filehtml):
    if not os.path.isdir(os.path.join(filehtml,eachFile)):
        fileName = os.path.split(filehtml)[1]
        eachFile = eachFile.replace(".html","")
        liFilePath = liFilePath + f'<li><a href="../{fileName}/{eachFile}.html">{eachFile}</a></li>' + '\n'
    pyperclip.copy(liFilePath)



allFilePath = os.listdir(r"D:\github\ddd")


for each in allFilePath:
    if os.path.isdir(os.path.join(r"D:\github\ddd",each)):
        print(os.path.join(r"D:\github\ddd",each))
        process_markdown_files(os.path.join(r"D:\github\ddd",each))


for each in allFilePath:
    if os.path.isdir(os.path.join(r"D:\github\ddd",each)):
        filepath = os.path.join(r"D:\github\ddd",each)
        allmd = os.listdir(filepath)
        for eachmd in allmd:
            if eachmd.endswith(".md"):
                os.remove(os.path.join(filepath,eachmd))



for each in allFilePath:
    if os.path.isdir(os.path.join(r"D:\github\ddd",each)):
        print(os.path.join(r"D:\github\ddd",each))
        filehtml = os.path.join(r"D:\github\ddd",each)
        fileName = os.path.split(filehtml)[1]
        liFilePath = ''
        for eachFile in os.listdir(filehtml):
            fileName = os.path.split(filehtml)[1]
            eachFile = eachFile.replace(".html","")

            with open(os.path.join(filehtml,eachFile+".html"),'r',encoding='utf=8') as f:
                content = f.read()

            after_content = f''''''
            html_content =  re.sub(r'<header>.*?</header>', after_content, content, flags=re.DOTALL)
              
            with open(os.path.join(filehtml,eachFile+".html"), 'w',encoding = 'utf-8') as f:
                f.write(html_content)                    

            



import os 
import re 
filepath = r'D:\github\ddd\Model'
for eachFile in os.listdir(filepath):
    if not os.path.isdir(os.path.join(filepath,eachFile)):
        fileName = os.path.join(filepath,eachFile)
    
        with open(fileName,'r',encoding='utf=8') as f:
            content = f.read()
    
        after_content = '<header></header>'
        html_content =  re.sub(r'<header>[\w\W]*?</header>', after_content, content)
        
        after_content = '<aside class="sidebar"></aside>'
        html_content =  re.sub(r'<aside class="sidebar">[\w\W]*?</aside>', after_content, html_content)
          
        after_content = '<footer></footer><script src="./subpagetemplate/loadContent.js"></script>'
        html_content =  re.sub(r'<footer>[\w\W]*?</footer>', after_content, html_content)    
          
        after_content = "<title>SilenceDream Sharing Website</title>"
        html_content =  re.sub(r"<title>Subpage - SilenceDream Sharing Website</title>", after_content, html_content)  
        with open(fileName, 'w',encoding = 'utf-8') as f:
            f.write(html_content)                    
    


allfilepath = ["D:\github\ddd\Writing",
"D:\github\ddd\PanelData",
"D:\github\ddd\pythonintro",
"D:\github\ddd\PythonPakage",
"D:\github\ddd\PythonSpider",
"D:\github\ddd\PythonTextAnalysis",
"D:\github\ddd\Question",
"D:\github\ddd\SelfIntro",
"D:\github\ddd\SPSSintro",
"D:\github\ddd\StataDraw",
"D:\github\ddd\StataIntro",
"D:\github\ddd\Stataputdocx",
"D:\github\ddd\Tools"]

for eachfilepath in allfilepath:
    filepath = eachfilepath
    for eachFile in os.listdir(filepath):
        if not os.path.isdir(os.path.join(filepath,eachFile)):
            fileName = os.path.join(filepath,eachFile)
        
            with open(fileName,'r',encoding='utf=8') as f:
                content = f.read()
        
            after_content = '<header></header>'
            html_content =  re.sub(r'<header>[\w\W]*?</header>', after_content, content)
            
            after_content = '<aside class="sidebar"></aside>'
            html_content =  re.sub(r'<aside class="sidebar">[\w\W]*?</aside>', after_content, html_content)
              
            after_content = '<footer></footer><script src="./subpagetemplate/loadContent.js"></script>'
            html_content =  re.sub(r'<footer>[\w\W]*?</footer>', after_content, html_content)    
              
            after_content = "<title>SilenceDream Sharing Website</title>"
            html_content =  re.sub(r"<title>Subpage - SilenceDream Sharing Website</title>", after_content, html_content)  
            with open(fileName, 'w',encoding = 'utf-8') as f:
                f.write(html_content)                    
        



