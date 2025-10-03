from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_filename):
    merger = PdfMerger()
    
    for pdf in pdf_list:
        merger.append(pdf)
    
    merger.write(output_filename)
    merger.close()

if __name__ == "__main__":
    # Example usage
    pdfs_to_merge = [ "Howard_SoonCV_DE.pdf", "250404_Arbeitstzeugnis_Howard_Yi_Soon.pdf", "Fachochschulreife_Howard.pdf", 
                     "Immatrikulationsbescheinigung_Howard.pdf", "Leistungnachweis.pdf","Projektmanager_zertifikat.pdf"]
    output_file = "CV_Zeugnis_merge.pdf"
    
    merge_pdfs(pdfs_to_merge, output_file)
    print(f"PDFs merged successfully into {output_file}")
