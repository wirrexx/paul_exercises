import zipfile
from io import BytesIO

stream = BytesIO()

with zipfile.ZipFile(stream, 'w') as zip_file:
    zip_file.writestr('file.txt')