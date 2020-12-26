import os

def get_type(path: str):
    _, file_extension = os.path.splitext(path)
    file_extension = file_extension.lower()
    if file_extension in ['.png', '.jpg', '.jpeg', 'svg']:
        return 'image'
    if file_extension in ['.mpeg', '.mp4', 'mp5', 'flv', '.mov', '.avi', 'mkv']:
        return 'video'
    if file_extension in ['iiq', '3fr', 'dcr', 'k25', 'kdc', 'crw', 'cr2', 'cr3',
                          'nef', 'nrw', 'orf', 'pef', 'rw2', 'arw', 'srf', 'sr2', 'tiff']:
        return 'raw'
    else:
        return 'other'