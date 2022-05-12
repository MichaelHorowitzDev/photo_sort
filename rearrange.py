import os
from os.path import join
import shutil
from typing import Optional
from PIL import Image
from datetime import datetime


def get_image_date(url: str) -> Optional[datetime]:
    try:
        img = Image.open(url)
        exif = img.getexif()
        date = exif.get(306)
        return datetime.strptime(date, '%Y:%m:%d %H:%M:%S')
    except IOError:
        return None
    except TypeError:
        return None
    except ValueError:
        return None


def get_files(url: str) -> list[str]:
    directory = os.fsdecode(url)
    return os.listdir(directory)


def arrange(files: list[str], output_dir: str, year: bool, month: bool, day: bool):
    for file in files:
        filename = os.fsdecode(file)
        if not filename.endswith(('.jpeg', '.jpg')):
            continue
        image_date = get_image_date(filename)
        if image_date is None:
            continue
        else:
            path_types = []
            if year:
                path_types.append(str(image_date.year))
            if month:
                path_types.append(str(image_date.month))
            if day:
                path_types.append(str(image_date.day))
            output_path = join(output_dir, *path_types)
            os.makedirs(output_path, exist_ok=True)
            shutil.move(filename, output_path)


def main(current_dir: str, output_dir: str, options: dict):
    year = options.get('year', False)
    month = options.get('month', False)
    week = options.get('week', False)
    day = options.get('day', False)

    files = map(lambda x: os.path.join(current_dir, x), get_files(current_dir))
    arrange(list(files), output_dir, year, month, day)
