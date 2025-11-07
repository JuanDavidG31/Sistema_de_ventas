# back/db_routers.py

class MultiDBRouter:
    """
    Un router para controlar qué operaciones de base de datos manejan qué modelos.
    """

    def db_for_read(self, model, **hints):
        """Lee operaciones para ProductoImagen van a Mongo."""
        if model._meta.app_label == 'back' and model._meta.model_name == 'productoimagen':
            return 'mongo_db'
        return 'default'

    def db_for_write(self, model, **hints):
        """Escribe operaciones para ProductoImagen van a Mongo."""
        if model._meta.app_label == 'back' and model._meta.model_name == 'productoimagen':
            return 'mongo_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """Permitir relaciones si ambos objetos están en la misma DB."""
        # Si un modelo está en MySQL y el otro en Mongo, la relación NO ES VÁLIDA a nivel de DB.
        # En tu caso, Producto está en MySQL y ProductoImagen en Mongo, por lo que la relación
        # debe gestionarse a nivel de la lógica de aplicación (DRF/Python), no a nivel de DB.

        # Retorna None para que la relación sea permitida por Django (asumiendo que manejamos FKs manualmente).
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Controlar qué modelos se migran a qué DB."""
        
        # Migra el modelo ProductoImagen SOLAMENTE a la base de datos 'mongo_db'
        if model_name == 'productoimagen':
            return db == 'mongo_db'
        
        # Migra el resto de modelos SOLAMENTE a la base de datos 'default' (MySQL)
        elif app_label == 'back':
            return db == 'default'
        
        # Otros modelos (como auth, admin) van a la default
        return db == 'default'