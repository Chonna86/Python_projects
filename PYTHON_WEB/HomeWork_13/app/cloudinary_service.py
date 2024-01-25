import cloudinary
from cloudinary import uploader

cloudinary.config(
    cloud_name="test_cloud_name",
    api_key="test_api_key",
    api_secret="test_api_secret"
)

def upload_file(file):
    result = uploader.upload(file.file)
    return result["secure_url"]