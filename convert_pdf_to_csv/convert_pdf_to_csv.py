"""
Convert a pdf to a csv.

- input: path to a pdf
- output: csv in the same path of the pdf
- use PyPDF2 to read the pdf
- panda to manipulate and save the data as a CSV file
"""

# import the libraries
import PyPDF2
import pandas as pd
import os

# get the path of the pdf
def get_pdf_path():
    """
    Get the path of the pdf.
    """
    pdf_path = input("Enter the path of the pdf: ")
    return pdf_path

# main function
def main():
    """
    Main function.
    """
    # get the path of the pdf
    pdf_path = get_pdf_path()

    # open the pdf
    pdf_file = open(pdf_path, 'rb')

    # read the pdf
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # get the number of pages
    num_pages = len(pdf_reader.pages)

    # create a list of the pages
    pages = []
    for i in range(num_pages):
        page = pdf_reader.pages[i]
        pages.append(page)

    # create a dataframe
    df = pd.DataFrame()

    # iterate over the pages
    for page in pages:
        # get the text of the page
        page_text = page.extract_text()

        # split the text by the new line
        page_text = page_text.split('\n')

        # create a dataframe with the page text
        df_page = pd.DataFrame(page_text)

        # append the dataframe to the main dataframe
        df = df._append(df_page)

    # save the dataframe as a csv
    csv_path = os.path.splitext(pdf_path)[0] + '.csv'
    df.to_csv(csv_path, index=False)
    
if __name__ == "__main__":
    main()