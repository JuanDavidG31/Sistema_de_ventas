import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

# Configuration       
cloudinary.config( 
    cloud_name = "dyomq1xyf", 
    api_key = "448119751486741", 
    api_secret = "stjOfMBVwyNvs4VcPw96Oh9bwNM", 
    secure=True
)

def upload_to_cloudinary(file, product_id):
    """
    Sube un archivo a Cloudinary y devuelve el URL.
    
    :param file: El objeto de archivo subido (UploadedFile).
    :param product_id: El ID del producto para usar como carpeta o tag.
    :return: El URL seguro del archivo subido.
    """
    
    # Convertir el objeto File a un formato que Cloudinary pueda leer
    # En DRF, el file puede ser un BytesIO o un TemporaryUploadedFile
    
    upload_result = cloudinary.uploader.upload(
        file,
        folder=f"ventas/productos/{product_id}", # Carpeta donde se guardará en Cloudinary
        resource_type="image"
    )
    
    return upload_result['secure_url']