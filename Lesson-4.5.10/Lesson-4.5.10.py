from zipfile import ZipFile

def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1024:
        return f'{size} B'
    elif 1024 <= size < 1048576:
        return f'{round(size / 1024)} KB'
    elif 1048576 <= size < 1073741824:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'

with ZipFile('desktop.zip') as zip_file:
    info = zip_file.infolist()
    lst = []
    for item in info:
        if item.file_size:
            s = f"{item.filename.split('/')[-1]} {convert_bytes(item.file_size)}"
            spaces = '  '*item.filename.count('/')
            lst.append(spaces+s)
        else:
            spaces = '  '*(item.filename.count('/')-1)
            lst.append(spaces+item.filename.split('/')[-2])
    print(*lst, sep='\n')