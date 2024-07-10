#importando bibilioteca para conexão do python ao mysql-server
import mysql.connector
from mysql.connector import errorcode
# from flask_bcrypt import generate_password_hash



print("Conectando ao Mysql Server...")
#realizando a conexão ao banco de dados
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno ==  errorcode.ER_ACCESS_DENIED_ERROR:
            print('Usuário ou senha inválido')
      else:
            print(err)
#garantindo a criação da banco game_list e selecionando-o
cursor = conn.cursor()
cursor.execute("drop database if exists `game_list`;")
cursor.execute("create database `game_list`;")
cursor.execute("use `game_list`;")

# criando tabelas no banco
TABLES = {}
TABLES['Games'] = ('''
      create table `games`(
            `id` int(11) not null auto_increment,
            `title` varchar(70) not null,
            `genre` varchar(30) not null,
            `platform` varchar(20) not null,
            primary key (`id`)
            ) engine=InnoDB default charset=utf8 collate=utf8_bin;''')

TABLES['Users'] = ('''
      create table `users`(
            `name` varchar(50) not null,
            `nickname` varchar(8) not null,
            `password` varchar(100) not null,
            primary key (`nickname`)
            ) engine=InnoDB default charset=utf8 collate=utf8_bin;''')

for nome_tabela in TABLES:
      tabela_sql = TABLES[nome_tabela]

      try:
            print('Criando a tabela: {}'.format(nome_tabela), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('A Tabela {} já existe no banco.'.format(nome_tabela))
            else:
                  print(err.msg)
      else:
            print('OK')

#inserindo usuarios
usuario_sql = 'insert into users (name, nickname, password) values (%s, %s, %s)'
usuarios = [('Roger Alves Rodrigues Melo', 'roger','123456'),
            ('Aylla Vitória Alves Azevedo', 'aylla', '123456'),
            ('Denise Azevedo da Silva Rodrigues', 'denise', '123456'),
            ('Saulo bananeira', 'saulo','123456'),
            ('Wellington','tom','123456')
]
cursor.executemany(usuario_sql,usuarios)

#select na tabela usuarios para teste
cursor.execute('select * from game_list.users')
print('-'*13+' Usuários: '+'-'*13)
for user in cursor.fetchall():
      print(user[1])

#inserindo jogos na tabela games
jogos_sql = 'insert into games (title, genre, platform) values (%s, %s, %s)'
jogos = [
      ('80 Days','Casual','STEAM'),
      ('Ace Combat Assault Horizon Enhanced Edition','Ação','STEAM'),
      ('America`s Army: Proving Grounds','Ação','STEAM'),
      ('The Coma 2: Vicious Sisters','Aventura','GOG GALAXY'),
      ('Control Ultimate Edition','Aventura','GOG GALAXY'),
      ('Cyberpunk','Aventura','GOG GALAXY'),
      ('3 out of 10 Ep. 1: Welcome To Shovelworks','Aventura','EPIC GAMES'),
      ('20XX','Aventura','EPIC GAMES'),
      ('A Plague Tale: Innocence','Aventura','EPIC GAMES'),
      ('Fifa', 'Esposte','ORIGIN EA'),
      ('Ghost Reacon Break Point','Simulação/Ação','UPLAY')
]
cursor.executemany(jogos_sql,jogos)

#select na tabela games para teste
cursor.execute('select * from game_list.games')
print('-'*13+' Jogos: '+'-'*13)
for game in cursor.fetchall():
      print(game[1])

#commintando as alterações para gravar no banco
conn.commit()
#fechando a conexão com o banco.
cursor.close()
conn.close()