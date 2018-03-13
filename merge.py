import os
import re

from PyPDF2 import PdfFileMerger, PdfFileReader


dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(dir_path, 'data')

pdfs_to_merge = [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f))]

print('Merging Files in /data')
merger = PdfFileMerger(strict=False)
for pdf in pdfs_to_merge:
    print('\tMerging: ' + pdf)
    merger.append(
        PdfFileReader(
            open(os.path.join(dir_path, 'data', pdf), 'rb'),
            strict=False
        )
    )

merger.write(os.path.join(dir_path, 'merged.pdf'))
print('merged.pdf file written')
