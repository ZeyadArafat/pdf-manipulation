# Program: PDF editor that takes PDF paths as an input then returns a new file as willed.
# Authors:  Zeyad Mohamed Arafat        20230161
#           Moaaz Mohamed Soliman       20230410
#           Youssef Ahmed Beshir        20230476
# Version: 2.0
# Date: March 2, 2024


# PdfWriter : to create (write) new documents.
# PdfReader : to read existing documents.
from PyPDF2 import PdfWriter, PdfReader


def merge(path1, path2, new_path):
    merged = PdfWriter()

    merged.append(path1)    # append the first PDF to the new PDF.
    merged.append(path2)    # append the second PDF to the new PDF.

    merged.write(new_path)  # create the new merged PDF to the specified location.
    merged.close()


def extract(pdf_path, page_number):
    path_to_save = pdf_path.replace(".pdf", "")
    path_to_save += "_page" + str(page_number) + ".pdf"   # naming the extracted PDF page.

    pdf_file = open(pdf_path, "rb")
    target_page = PdfWriter()                             # create the new extracted PDF page.

    target_page.append(fileobj=pdf_file, pages=(page_number-1, page_number))
    target_page.write(open(path_to_save, "wb"))


def split(pdf_path):
    pdf_file = open(pdf_path, 'rb')
    info_reader = PdfReader(pdf_path)
    number_of_pages = len(info_reader.pages)            # get pages' number

    for page in range(1, number_of_pages + 1):          # iterating throw the PDF and split each page.
        path_to_save = pdf_path
        path_to_save.replace(".pdf", "")
        path_to_save += "_page" + str(page) + ".pdf"        # naming the files.
        target_page = PdfWriter()
        target_page.append(fileobj=pdf_file, pages=(page - 1, page))  # appending each page to a new PDF file.
        target_page.write(open(path_to_save, "wb"))


# Application running
print("Welcome to pdf editor \n")
while True:
    print("""1- Merge two files
2- Extract a page from file
3- Split file into separate pages
4- Exit

!!ALERT!!
PLEASE MAKE SURE YOU DO NOT ADD [""] OR ANY OTHER CHARACTERS TO THE PATH!\n""")
    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            path_1 = input('Enter The path of the first PDF: ')
            path_2 = input('Enter The path of the second PDF: ')
            new = input('Enter The path of the new pdf PDF: ')
            merge(path_1, path_2, new)
            print("Done ;) \n")

        elif choice == "2":
            pdfPath = input("Enter the path of the PDF: ")
            pageNumber = int(input("Enter the number of the page: "))
            extract(pdfPath, pageNumber)
            print("Done ;) \n")

        elif choice == "3":
            pdfPath = input("Enter the path of the PDF: ")
            split(pdfPath)
            print("Done ;) \n")

        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("Not a valid choice, try again. \n")

    # handling possible errors.
    except FileNotFoundError:
        print("Invalid path, Please enter a valid file path! \n")
    except ValueError:
        print("Invalid page number, Page numbers should be Positive integers only! \n")
    except IndexError:
        print("Invalid page number, Page number is not Found! \n")
