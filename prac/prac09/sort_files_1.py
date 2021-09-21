import os
import shutil
def main():
    os.chdir('../FilesToSort1')
    try:
        os.mkdir('TxT')
    except FileExistsError:
        pass
    sourcepath='../FilesToSort1'
    sourcefiles=os.listdir(sourcepath)
    for file in sourcefiles:
        if file.endswith('.txt'):
            shutil.move(os.path.join(sourcepath,file),'TxT/')
    try:
        os.mkdir('Doc')
    except FileExistsError:
        pass
    sourcepath='../FilesToSort1'
    sourcefiles=os.listdir(sourcepath)
    for file in sourcefiles:
        if file.endswith('.doc'):
            shutil.move(os.path.join(sourcepath,file),'Doc/')
    try:
        os.mkdir('Docx')
    except FileExistsError:
        pass
    sourcepath='../FilesToSort1'
    sourcefiles=os.listdir(sourcepath)
    for file in sourcefiles:
        if file.endswith('.docx'):
            shutil.move(os.path.join(sourcepath,file),'Docx/')
    try:
        os.mkdir('Png')
    except FileExistsError:
        pass
    sourcepath='../FilesToSort1'
    sourcefiles=os.listdir(sourcepath)
    for file in sourcefiles:
        if file.endswith('.png'):
            shutil.move(os.path.join(sourcepath,file),'Png/')
    try:
        os.mkdir('Gif')
    except FileExistsError:
        pass
    sourcepath='../FilesToSort1'
    sourcefiles=os.listdir(sourcepath)
    for file in sourcefiles:
        if file.endswith('.gif'):
            shutil.move(os.path.join(sourcepath,file),'Gif/')
    try:
        os.mkdir('Xls')
    except FileExistsError:
        pass
    sourcepath='../FilesToSort1'
    sourcefiles=os.listdir(sourcepath)
    for file in sourcefiles:
        if file.endswith('.xls'):
            shutil.move(os.path.join(sourcepath,file),'Xls/')
    try:
        os.mkdir('Xlsx')
    except FileExistsError:
        pass
    sourcepath='../FilesToSort1'
    sourcefiles=os.listdir(sourcepath)
    for file in sourcefiles:
        if file.endswith('.xlsx'):
            shutil.move(os.path.join(sourcepath,file),'Xlsx/')
    try:
        os.mkdir('Jpg')
    except FileExistsError:
        pass
    sourcepath='../FilesToSort1'
    sourcefiles=os.listdir(sourcepath)
    for file in sourcefiles:
        if file.endswith('.jpg'):
            shutil.move(os.path.join(sourcepath,file),'Jpg/')



main()
