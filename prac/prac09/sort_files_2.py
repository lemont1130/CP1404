import os
import shutil
def main():
    os.chdir('../FilesToSort')
    try:
        os.mkdir('Spreadsheets')
    except FileExistsError:
        pass
    sourcepath='../FilesToSort'
    sourcefiles=os.listdir(sourcepath)
    for file in sourcefiles:
        if file.endswith('.xls'):
            shutil.move(os.path.join(sourcepath,file),'Spreadsheets/')
        if file.endswith('.xlsx'):
            shutil.move(os.path.join(sourcepath,file),'Spreadsheets/')
    try:
        os.mkdir('Images')
    except FileExistsError:
        pass
    sourcepath='../FilesToSort'
    sourcefiles=os.listdir(sourcepath)
    for file in sourcefiles:
        if file.endswith('.jpg'):
            shutil.move(os.path.join(sourcepath,file),'Images/')
        if file.endswith('.png'):
            shutil.move(os.path.join(sourcepath,file),'Images/')
        if file.endswith('.gif'):
            shutil.move(os.path.join(sourcepath,file),'Images/')
    try:
        os.mkdir('Docs')
    except FileExistsError:
        pass
    sourcepath='../FilesToSort'
    sourcefiles=os.listdir(sourcepath)
    for file in sourcefiles:
        if file.endswith('.txt'):
            shutil.move(os.path.join(sourcepath,file),'Docs/')
        if file.endswith('.docx'):
            shutil.move(os.path.join(sourcepath,file),'Docs/')
        if file.endswith('.doc'):
            shutil.move(os.path.join(sourcepath,file),'Docs/')
main()
