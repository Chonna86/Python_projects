import os
import shutil
import sys


def normalize(s):
    translit = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e',
        'є': 'ie', 'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i',
        'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
        'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'iu', 'я': 'ia',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E',
        'Є': 'IE', 'Ж': 'ZH', 'З': 'Z', 'И': 'Y', 'І': 'I', 'Ї': 'I', 'Й': 'I',
        'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R',
        'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'KH', 'Ц': 'TS', 'Ч': 'CH',
        'Ш': 'SH', 'Щ': 'SHCH', 'Ь': '', 'Ю': 'IU', 'Я': 'IA',
    }

    normalized = ''
    for char in s:
        if char in translit:
            normalized += translit[char]
        elif char.isalnum():
            normalized += char
        else:
            normalized += '_'
    return normalized


def sort_files(directory):
    categories = {
        'images': ['JPEG', 'PNG', 'JPG', 'SVG'],
        'video': ['AVI', 'MP4', 'MOV', 'MKV'],
        'documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
        'audio': ['MP3', 'OGG', 'WAV', 'AMR'],
        'archives': ['ZIP', 'GZ', 'TAR'],
    }

    known_extensions = set()
    unknown_extensions = set()

    for root, _, files in os.walk(directory):
        for filename in files:
            _, extension = os.path.splitext(filename)
            extension = extension[1:].upper()  

            if extension in categories['images']:
                category = 'images'
            elif extension in categories['video']:
                category = 'video'
            elif extension in categories['documents']:
                category = 'documents'
            elif extension in categories['audio']:
                category = 'audio'
            elif extension in categories['archives']:
                category = 'archives'
            else:
                category = 'unknown'
                unknown_extensions.add(extension)
            
            source_path = os.path.join(root, filename)
            normalized_filename = normalize(filename)
            dest_path = os.path.join(directory, category, normalized_filename)
            
            if category == 'archives':
                archive_folder = os.path.join(directory, 'archives', normalized_filename[:-len(extension) - 1])
                os.makedirs(archive_folder, exist_ok=True)
                shutil.unpack_archive(source_path, archive_folder)
            else:
                os.makedirs(os.path.join(directory, category), exist_ok=True)
                shutil.move(source_path, dest_path)
            
            known_extensions.add(extension)

    return known_extensions, unknown_extensions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sort.py <directory>")
        sys.exit(1)

    target_directory = sys.argv[1]
    known_extensions, unknown_extensions = sort_files(target_directory)

    print("Known extensions:", ', '.join(known_extensions))
    print("Unknown extensions:", ', '.join(unknown_extensions))