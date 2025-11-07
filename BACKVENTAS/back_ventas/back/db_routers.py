

class MultiDBRouter:
    """
    Un router para controlar qué operaciones de base de datos manejan qué modelos.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'back' and model._meta.model_name == 'productoimagen':
            return 'mongo_db'
        return 'default'

    def db_for_write(self, model, **hints):
        
        if model._meta.app_label == 'back' and model._meta.model_name == 'productoimagen':
            return 'mongo_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        
        
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Controlar qué modelos se migran a qué DB."""
        
        if model_name == 'productoimagen':
            return db == 'mongo_db'
        
        elif app_label == 'back':
            return db == 'default'
        
        return db == 'default'