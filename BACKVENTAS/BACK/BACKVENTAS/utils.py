import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
import re
# Configuration       
cloudinary.config( 
    cloud_name = "dyomq1xyf", 
    api_key = "448119751486741", 
    api_secret = "stjOfMBVwyNvs4VcPw96Oh9bwNM", 
    secure=True
)

def upload_to_cloudinary(file, product_id):
    
    

    
    upload_result = cloudinary.uploader.upload(
        file,
        folder=f"ventas/productos/{product_id}", 
        resource_type="image"
    )
    
    return upload_result['secure_url']



def get_public_id_from_url(url):
    
    
    try:
        parts = url.split('/')
        
        index_folder = parts.index('ventas')
        
        file_name_with_ext = parts[-1]
        
        file_name_no_ext = file_name_with_ext.rsplit('.', 1)[0]
        
       
        return f"{parts[index_folder]}/{parts[index_folder+1]}/{parts[index_folder+2]}/{file_name_no_ext}"
        
    except ValueError:
         return None
    except IndexError:
         return None


def delete_from_cloudinary(url):
   
    public_id = get_public_id_from_url(url)
    
    if not public_id:
        print(f"Error: No se pudo extraer el Public ID de la URL: {url}")
        return False
        
    try:
        result = cloudinary.uploader.destroy(public_id)
        
        if result.get('result') == 'ok':
            print(f"Éxito al borrar en Cloudinary: {public_id}")
            return True
        else:
            print(f"Fallo al borrar en Cloudinary o no encontrado: {result}")
            return False
            
    except Exception as e:
        print(f"Excepción al borrar en Cloudinary: {e}")
        return False