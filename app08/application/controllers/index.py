import web
import application.models.conexion as conexion

render = web.template.render('application/views/', base='master')

class Index:
    def __init__(self):
        pass

    def GET(self):  
        datos = conexion.select_datos().list()
        return render.index(datos)
