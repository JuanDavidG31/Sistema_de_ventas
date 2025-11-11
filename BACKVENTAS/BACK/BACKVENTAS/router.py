
class ImageDBRouter:
    """
    Un enrutador para controlar todas las operaciones de la base de datos
    para los modelos de imágenes.
    """

    
    route_app_labels = {'BACKVENTAS'} 
    modelos_mongo = ['productoimagen'] 

    def db_for_read(self, model, **hints):
        """
        Dirige las operaciones de lectura de ProductoImagen a 'mongo_db'.
        """
        if model._meta.app_label in self.route_app_labels and model._meta.model_name in self.modelos_mongo:
            return 'mongo_db'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Dirige las operaciones de escritura de ProductoImagen a 'mongo_db'.
        """
        if model._meta.app_label in self.route_app_labels and model._meta.model_name in self.modelos_mongo:
            return 'mongo_db'
        return 'default'

    
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels and model_name in self.modelos_mongo:
            return db == 'mongo_db' 
        
        if db == 'mongo_db':
            return False
        
        return True