from database import Database
from teachercrud import TeacherCRUD
# Configuração da conexão com o Neo4j
db=Database("bolt://18.206.64.77:7687" , "neo4j", "checkouts-reference-dynamometers")

teacher=TeacherCRUD(db)

teacher.create("Chris Lima", 1956, "189.052.396-66")

print(teacher.read("Chris Lima"))

teacher.update("Chris Lima", "162.052.777-77")

print(teacher.read("Chris Lima"))

db.close()

