import html2md 

path=r"D:\Python\Projects\Github\awesome-python-projects\Python_Projects\html_md.html"

def html_to_md():
    html = open(path, 'r').read()
    md=html2md.convert(html)
    md_path = 'save_md.md'
    
    with open(md_path, 'w') as mdr:
        mdr.write(md)
        mdr.close()
        
    md_save_str = f"You have successfully written the HTML to a MD file and it is saved at {md_path}"
    print(md_save_str)
html_to_md()