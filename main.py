import os
import subprocess
import sys

if __name__ == '__main__':

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'PyPDF2'])

    import PyPDF2

    directory = os.getcwd()
    files = os.listdir(directory)
    merger = PyPDF2.PdfFileMerger()

    for filename in files:
        if filename.endswith('.pdf'):
            merger.append(fileobj=open(os.path.join(directory, filename), 'rb'))

    merger.write(open(os.path.join(directory, 'res.pdf'), 'wb'))
