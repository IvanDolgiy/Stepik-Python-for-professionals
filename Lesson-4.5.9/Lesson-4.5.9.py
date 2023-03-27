from zipfile import ZipFile
import json

with ZipFile('data.zip') as zip_file:
    info = zip_file.infolist()
    lst_files = [i.filename for i in info if i.filename.split('.')[-1]=='json']
    lst = []
    for path in lst_files:
        with zip_file.open(path) as file:
            try:
                s = json.loads(file.read().decode('utf-8'))
                lst.append(s)
            except ValueError:
                pass
    footbalists = []
    for item in lst:
        if item['team']=='Arsenal':
            footbalists.append(item['first_name']+' '+item['last_name'])
    print(*sorted(footbalists), sep='\n')



            




    
            
        