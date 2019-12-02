# criando banco e tabelas
import sqlite3

# conectando...
conn = sqlite3.connect('dbteste.db')
# definindo um cursor
cursor = conn.cursor()

# apagar tabelas se ja existem
#tables = [(gradeestudo, usuario, materia, atividade,HorarioEstudo)]
#cursor.executemany("""drop tables (?,?,?,?,?);""", tables)


# criando a tabela (schema)
cursor.execute("""
create table usuario(
	id INTEGER PRIMARY KEY AUTOINCREMENT not null,
    nome varchar(100) not null,
    email varchar(255) not null,
    senha varchar(255) not null
);
""")

cursor.execute("""
create table materia(
	id integer primary key AUTOINCREMENT,
    horario varchar(22), 
    nome varchar(255)
);

""")
cursor.execute("""
create table horarioestudo(
	id int auto_increment primary key,
	aluno int not null,
    materias int not null,
    horario varchar(9) 
);
""")

cursor.execute("""
create table gradeestudo( 
	id integer primary key AUTOINCREMENT,
	aluno int not null,
    materias int not null
);
""")

cursor.execute("""
create table atividade(
	id integer primary key AUTOINCREMENT,
	aluno int not null,
    materia int,
    conteudo varchar(255)
);
""")

'''

cursor.execute("""
alter table gradeestudo
	ADD CONSTRAINT aluno foreign key (aluno) references usuario(id),
    add constraint materia foreign key (materias) references materia(id);

""")

cursor.execute("""
alter table horarioestudo
	add constraint aluno foreign key (aluno) references usuario(id),
    add constraint materio foreign key (materias) references materia(id);
""")

cursor.execute("""
alter table atividade
	add constraint aluno foreign key (aluno) references usuario(id),
    add constraint materias foreign key (materia) references materia(id);
""")

'''


