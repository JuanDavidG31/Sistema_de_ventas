# BACKVENTAS/router.py
# (Si tu archivo router.py no existe, créalo con este contenido)

class ImageDBRouter:
    """
    Un router para controlar qué modelos van a qué base de datos.
    - Los modelos que contienen imágenes (ProductoImagen) van a 'mongo_db'.
    - Los demás modelos van a la base de datos 'default'.
    """

    def db_for_read(self, model, **hints):
        """
        Intenta leer modelos ProductoImagen desde mongo_db.
        """
        if model._meta.app_label == 'BACKVENTAS' and model._meta.model_name == 'productoimagen':
            return 'mongo_db'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Intenta guardar modelos ProductoImagen en mongo_db.
        """
        if model._meta.app_label == 'BACKVENTAS' and model._meta.model_name == 'productoimagen':
            return 'mongo_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Permite relaciones si ambos objetos están en la misma base de datos, 
        o si es la relación específica entre Producto y ProductoImagen.
        
        Aquí está la CLAVE para solucionar tu ValueError.
        """
        
        # 1. Obtenemos los nombres de los modelos
        model1_name = obj1._meta.model_name
        model2_name = obj2._meta.model_name
        
        # 2. Verificamos la relación específica Producto <-> ProductoImagen
        # Si la relación es entre Producto (default) y ProductoImagen (mongo_db)
        if (model1_name == 'producto' and model2_name == 'productoimagen') or \
           (model1_name == 'productoimagen' and model2_name == 'producto'):
            # Permite esta relación de clave foránea cruzada.
            # Nota: Esto solo permite la relación, el acceso requerirá más lógica si no usas .id
            return True

        # 3. Regla general: Si los modelos están en la misma base de datos, la relación está permitida
        db1 = self.db_for_read(obj1)
        db2 = self.db_for_read(obj2)
        
        if db1 and db2 and db1 == db2:
            return True
        
        # 4. Evitar relaciones cruzadas no manejadas explícitamente
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Asegura que solo se creen las tablas en la base de datos correcta.
        """
        if app_label == 'BACKVENTAS' and model_name == 'productoimagen':
            # El modelo ProductoImagen sólo se migra a 'mongo_db'
            return db == 'mongo_db'
        
        # Todos los demás modelos (incluido Producto) solo se migran a 'default'
        return db == 'default'