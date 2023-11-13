import os
import shutil
import concurrent.futures

categories = {
    'images': ['JPEG', 'PNG', 'JPG', 'SVG'],
    'video': ['AVI', 'MP4', 'MOV', 'MKV'],
    'documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
    'audio': ['MP3', 'OGG', 'WAV', 'AMR'],
    'archives': ['ZIP', 'GZ', 'TAR'],
}

source_directory = "Хлам"
destination_directory = "Сортовані файли"

if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

def get_category(file_extension):
    for category, extensions in categories.items():
        if file_extension.upper() in extensions:
            return category
    return 'other'

def move_file(source, destination):
    try:
        shutil.move(source, destination)
    except Exception as e:
        print(f"Помилка під час переміщення файлу {source}: {e}")

def process_file(file, source_dir, dest_dir):
    _, file_extension = os.path.splitext(file)
    category = get_category(file_extension[1:])
    category_directory = os.path.join(dest_dir, category)

    if not os.path.exists(category_directory):
        os.makedirs(category_directory)

    source_path = os.path.join(source_dir, file)
    destination_path = os.path.join(category_directory, file)
    move_file(source_path, destination_path)

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for root, _, files in os.walk(source_directory):
            for file in files:
                executor.submit(process_file, file, root, destination_directory)

if __name__ == "__main__":
    main()