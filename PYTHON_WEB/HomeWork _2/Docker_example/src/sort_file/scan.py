image_extensions = ("JPEG", "PNG", "JPG", "SVG")
video_extensions = ("AVI", "MP4", "MOV", "MKV")
docs_extensions = ("DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX")
audio_extensions = ("MP3", "OGG", "WAV", "AMR")
archive_extensions = ("ZIP", "GZ", "TAR")

registered_extensions = (
        image_extensions
        + video_extensions
        + docs_extensions
        + audio_extensions
        + archive_extensions
)

images = []
documents = []
audio = []
video = []
archives = []
unknown = []

categories = {
    "images": images,
    "documents": documents,
    "audio": audio,
    "video": video,
    "archives": archives,
}

known_extensions = set()
unknown_extensions = set()


def scan(pth):
    """
    Recursively scans a directory and categorizes its files based on their extensions.

    Args:
        pth (Path): The path to the directory to be scanned.

    Returns:
        Tuple[List[Path], List[Path], List[Path], List[Path], List[Path], List[Path]]: A tuple containing lists of files
        categorized as images, videos, audio, documents, archives, and unknown extensions.
    """
    for item in pth.iterdir():
        if item.is_file():
            suffix = item.suffix

            suff_upp = suffix[1:].upper()
            if suff_upp in registered_extensions:
                known_extensions.add(suffix)
            else:
                unknown_extensions.add(suffix)
            if suff_upp in image_extensions:
                images.append(item)
            elif suff_upp in video_extensions:
                video.append(item)
            elif suff_upp in audio_extensions:
                audio.append(item)
            elif suff_upp in docs_extensions:
                documents.append(item)
            elif suff_upp in archive_extensions:
                archives.append(item)
            else:
                unknown.append(item)

        else:
            scan(item)
            if not any(item.iterdir()):
                item.rmdir()
            continue
