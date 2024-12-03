import re

def text_cleaning (content):
    content = re.sub(r'\.{3,}', ' ', content)
    content = re.sub(r'(\.\s){3,}', ' ', content)
    
    
    content = re.sub(r'[⎠⎞⎝⎛©§]+', '', content)
    return content