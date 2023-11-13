from clean_folder.organizer import normalize, sort_files
import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: clean-folder <directory>")
        sys.exit(1)

    target_directory = sys.argv[1]
    known_extensions, unknown_extensions = sort_files(target_directory)

    print("Known extensions:", ', '.join(known_extensions))
    print("Unknown extensions:", ', '.join(unknown_extensions))

if __name__ == "__main__":
    main()