
class ImageDBRouter:
   

    def db_for_read(self, model, **hints):
        
        if model._meta.app_label == 'BACKVENTAS' and model._meta.model_name == 'productoimagen':
            return 'mongo_db'
        return 'default'

    def db_for_write(self, model, **hints):
        
        if model._meta.app_label == 'BACKVENTAS' and model._meta.model_name == 'productoimagen':
            return 'mongo_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        
        
        model1_name = obj1._meta.model_name
        model2_name = obj2._meta.model_name
        
        
        if (model1_name == 'producto' and model2_name == 'productoimagen') or \
           (model1_name == 'productoimagen' and model2_name == 'producto'):
           
            return True

        db1 = self.db_for_read(obj1)
        db2 = self.db_for_read(obj2)
        
        if db1 and db2 and db1 == db2:
            return True
        
        return False

def allow_migrate(self, db, app_label, model_name=None, **hints):
        
        if model_name == 'productoimagen':
            return db == 'mongo_db'

        if app_label == 'BACKVENTAS':
            return db == 'default'

       
        if db == 'mongo_db':
            return False 

        
        return db == 'default'