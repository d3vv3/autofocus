import os
import time
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime


def get_exif(path: str):
    try:
        image = Image.open(path)
        exif = {
            TAGS[k]: v
            for k, v in image._getexif().items()
            if k in TAGS
        }
    except:
        exif = {}
    return exif


def build_image_item(file_path: str, file_name: str):
    exif_data = get_exif(file_path)
    return {'filename': file_name,
            'path': file_path,
            'type': 'image',
            'manufacturer': get_manufacturer(exif_data),
            'camera': get_camera(exif_data),
            'height': get_height(exif_data),
            'width': get_width(exif_data),
            'aperture': get_aperture(exif_data),
            'shutter_speed': get_shutter_speed(exif_data),
            'focal_length': get_focal_length(exif_data),
            'focal_length_in_35mm': get_focal_length_35mm(exif_data),
            'exposure_time': get_exposure_time(exif_data),
            'iso': get_iso(exif_data),
            'created_at': get_created_at(exif_data, file_path),
            'coordinates': get_coordinates(exif_data),
            'tags': {},
            'people': {}
            }
    return item

def build_video_item(file_path: str, file_name: str):
    ts = os.path.getmtime(file_path)
    return {'filename': file_name,
            'path': file_path,
            'type': 'video',
            'created_at': datetime.fromtimestamp(ts) if ts != None else datetime.now(),
            'tags': {},
            'people': {}
            }

def get_manufacturer(exif_data: dict):
    try:
        return str(exif_data.get('Make', None))
    except:
        return None

def get_camera(exif_data: dict):
    try:
        return str(exif_data.get('Model', None))
    except:
        return None

def get_height(exif_data: dict):
    try:
        return int(exif_data.get('ExifImageHeight', None))
    except:
        return None

def get_width(exif_data: dict):
    try:
        return int(exif_data.get('ExifImageWidth', None))
    except:
        return None

def get_aperture(exif_data: dict):
    try:
        return float(exif_data.get('FNumber', None))
    except:
        return None

def get_shutter_speed(exif_data: dict):
    try:
        return float(exif_data.get('ShutterSpeedValue', None))
    except:
        return None

def get_focal_length(exif_data: dict):
    try:
        return float(exif_data.get('FocalLength', None))
    except:
        return None

def get_focal_length_35mm(exif_data: dict):
    try:
        return float(exif_data.get('FocalLengthIn35mmFilm', None))
    except:
        return None

def get_exposure_time(exif_data: dict):
    try:
        return float(exif_data.get('ExposureTime', None))
    except:
        return None

def get_iso(exif_data: dict):
    try:
        return int(exif_data.get('ISOSpeedRatings', None))
    except:
        return None

def get_created_at(exif_data: dict, file_path):
    time_str = exif_data.get('DateTimeDigitized', None)
    try:
        if time_str is not None:
            ts = datetime.strptime(str(time_str).strip(), '%Y:%m:%d %H:%M:%S')
        else:
            ts = datetime.fromtimestamp(os.path.getmtime(file_path)) or datetime.now()
    except:
        ts = datetime.fromtimestamp(os.path.getmtime(file_path)) or datetime.now()
    return ts

def get_coordinates(exif_data: dict):
    gps_info = exif_data.get('GPSInfo', None)
    if gps_info is None:
        return {'latitude': None, 'longitude': None}
    try:
        return degrees_to_decimal(gps_info)
    except:
        return {'latitude': None, 'longitude': None}

def degrees_to_decimal(exif_gps_info: dict):
    try:
        lat_degrees, lat_minutes, lat_seconds = exif_gps_info.get(2)
        lon_degrees, lon_minutes, lon_seconds = exif_gps_info.get(4)
        latitude_decimal = lat_degrees + (lat_minutes / 60) + (lat_seconds / 3600)
        longitude_decimal = lon_degrees + (lon_minutes / 60) + (lon_seconds / 3600)
    except Exception as e:
        logging.warning(e)
        latitude_decimal, longitude_decimal = None, None
    return {'latitude': float(latitude_decimal),
            'longitude': float(-longitude_decimal)}