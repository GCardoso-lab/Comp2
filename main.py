import json

# Utils
def class_to_json(obj):
    return json.dumps(obj.__dict__)


# Objeto Curso
class Curso():
    def __init__(self, id, nome, materias_obrigatorias, materias_opcionais, configuracoes, **kwargs):
        self.id = id
        self.nome = nome
        self.materias_obrigatorias = list(set(materias_obrigatorias))
        self.materias_opcioanis = list(set(materias_opcionais))
        self.configuracoes = dict(configuracoes)




p1 = Curso("EST001", "Estatística", ["MAC001", "MAC002"], ["CMP003"], {"ch_materias_obrigatorias": 1400, "ch_materias_opcionais": 600})


print(class_to_json(p1))
