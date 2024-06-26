class Usuario:
    def __init__(self,nome,nickname,senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


usuario1 = Usuario('Roger Alves Rodrigues Melo','roger','denise02')
usuario2 = Usuario('Denise Azevedo da Silva Rodrigues','deh','keka2412')
usuario3 = Usuario('Aylla Vitória Alves Azevedo', 'aylla', 'denise02')

usuario = {usuario1.nickname:usuario1,
           usuario2.nickname:usuario2,
           usuario3.nickname:usuario3}

