import crud_academica_II
db = crud_academica_II.crud()

class crud_materias:
    def consultar_materias(self, buscar):
        return db.consultar("select * from materias where codigo like'%"+ buscar["buscar"] 
            +"%' or nombre like'%"+ buscar["buscar"] +"%'")
    
    def administrar(self, materias):
        if materias["accion"] == "nuevo":
            sql = """
                INSERT INTO materias (nombre, codigo, descripcion)
                VALUES (%s, %s, %s, %s)
            """
            val = (materias["nombre"], materias["codigo"], materias["descripcion"])
        elif materias["accion"] == "modificar":
            sql = """
                UPDATE materias
                    SET nombre=%s, codigo=%s, descripcion=%s
                WHERE idMateria=%s
            """
            val = (materias["nombre"], materias["codigo"], materias["descripcion"], materias["idMateria"])
        elif materias["accion"] == "eliminar":
            sql = """
                DELETE FROM materias
                WHERE idMateria=%s
            """
            val = (materias["idMateria"],)
        return db.ejecutar_consultas(sql, val)