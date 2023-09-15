import os

class Config:
    # Configuración de la base de datos (MySQL en este caso)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/premium'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Deshabilita las notificaciones de cambios en la base de datos

    # Configuración de la clave secreta
    SECRET_KEY = "sumamaestarepoderosa"

    # Configuración de archivos estáticos
    STATIC_URL = 'static/'
    STATICFILES_DIRS = [
        os.path.join(os.path.dirname(__file__), 'static')  # Ruta relativa a la ubicación del archivo actual
    ]
    STATIC_ROOT = 'static'
