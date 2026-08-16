class Porta:
    def abrir(self):
        print(f"Girar a macaneta e empurrar/puxar a porta")


class Empresa:
    def abrir(self):
        print(f"Vá ao portal do empreendedor com toda a documentação para abrir um CNPJ")


class Ovo:
    def abrir(self):
        print(f"Quebre a casca com um garfo e separe as partes sobre uma frigideira")


class Pedra:
    pass


def tentar_abrir(objeto):
    try:
        # Duck Typing: Não importa a classe, apenas se o objeto "sabe" abrir
        objeto.abrir()
    except AttributeError:
        # Se o objeto não tiver o método abrir(), cai aqui
        print(f"Não é possível abrir objeto do tipo {objeto.__class__.__name__}.")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar abrir: {e}")