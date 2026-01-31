from cloudinary.uploader import upload, destroy
from fastapi import UploadFile
from app.core.config import settings
import app.core.cloudinary

ALLOWED = {"image/jpeg", "image/png", "image/jpg"}

def upload_image(file: UploadFile):
    if file.content_type not in ALLOWED:
        raise ValueError("Only JPEG and PNG files are allowed.")
    result = upload(
        file.file,
        folder=settings.CLOUDINARY_FOLDER,
        resource_type="image"
    )

    return result["secure_url"], result["public_id"]

def delete_image(public_id: str):
    if public_id:
        destroy(public_id, resource_type="image")