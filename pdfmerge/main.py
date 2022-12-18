import PyPDF2
import os

if __name__ == '__main__':
    os.remove("combined.pdf")
    merger = PyPDF2.PdfFileMerger()
    for file in os.listdir(os.curdir):
        if file.endswith(".pdf"):
            merger.append(file)
    merger.write("combined.pdf")





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
