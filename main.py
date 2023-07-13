import wikipedia
import os

page_obj = wikipedia.page('List of programming languages')
for lang in page_obj.links:
    fmt = lang.replace(' (programming language)','').replace('-','_').replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '').replace(',', '').replace('++','pp').replace('+', '_plus').replace('#', '_sharp').replace('′′','_double_prime').replace('\'\'','_double_prime').replace('′','_prime').replace('\'','_prime').replace('*','_star')
    # print(fmt)
    try:
        os.mkdir('/Users/maverick/Coding_Folder/Languages/'+fmt)
    except Exception as e:
        print("ERROR: "+fmt,e)
