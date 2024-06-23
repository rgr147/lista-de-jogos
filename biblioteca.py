class Jogo:
    def __init__(self,titulo,genero,plataforma):
        self.titulo = titulo
        self.genero = genero
        self.plataforma = plataforma

def main():
    jogo1 = Jogo('The Witcher 3','RPG','GOG Galaxy')
    jogo2 = Jogo('Fallout 4','RPG','Steam')
    jogo3 = Jogo('Cyber Punk 2077','RPG','GOG Galaxy')

    lista = [jogo1, jogo2, jogo3]

    return lista

if __name__ == '__main__':
    main()