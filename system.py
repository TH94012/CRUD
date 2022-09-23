import json, string, random
import forca


cyan = '\033[1;36m'
yellow = '\033[1;33m'

def create_database(localization, database):
    try:
        with open(localization + database) as data:
            pass
    except:
        with open(localization + database, 'at+') as data:
            data.write('[]')

def get_data(localization, database_name):
    with open(localization + database_name) as data:
        return json.load(data)

def header(text):
    length = len(text)
    print('\033[1;36m', '-' * (length + 4))
    print(F'\033[1;33m   {text}')
    print('\033[1;36m', '-' * (length + 4), '\033[m')

def login(localization, database):
    header('Login!')
    with open(localization + database) as database_arc:
        database_obj = json.load(database_arc)
        while True:
            try:
                x = False
                email = str(input('Email: ')).strip()
                if '@' not in email:
                    print('Email inválido.')
                    continue
                for i, c in enumerate(database_obj):
                    if c['email'] == email:
                        index = i
                        x = True
                        break
                if x == True:
                    break
            except:
                continue
        while True:
            try:
                password = str(input('Senha: ')).strip()
                if database_obj[index]['password'] == password:
                    break
                else:
                    continue
            except:
                continue
        return [database_obj[index]['username'],
                database_obj[index]['email'],
                database_obj[index]['password'],
                database_obj[index]['rank'],
                database_obj[index]['forca-victories'],
                database_obj[index]['forca-defeats'],
                database_obj[index]['forca-games'],
                database_obj[index]['id']
        ]

def register(localization, database):
    header('Registrar!')
    with open(localization + database) as database_arc:
        obj_database = json.load(database_arc)
        while True:
            try:
                username = str(input("Nome de usuário: ")).strip()
                for c in obj_database:
                    if c['username'] == username:
                        print('Esse nome de usuário já está sendo utilizado!')
                        continue
            except:
                continue
            else:
                break
        while True:
            try:
                re = False
                email = str(input("Email: ")).strip()
                if '@' not in email:
                    print('Email Inválido!')
                    continue
                for c in obj_database:
                    if c['email'] == email:
                        print('Esse email já está sendo utilizado!')
                        re = True
                        break
                if re == True:
                    continue
            except:
                continue
            else:
                break
        while True:
            try:
                password = str(input("Senha: ")).strip()
                if len(password) < 8:
                    print("Sua senha deve conter pelo menos 8 caracteres!")
                    continue
            except:
                continue
            else:
                break
        dados = {'username': username,
                 'email': email,
                 'password': password,
                 'rank': 'normal',
                 'forca-victories': 0,
                 'forca-defeats': 0,
                 'forca-games': 0,
                 'id': generate_id(localization, database)
        }
        obj_database.append(dados)
        with open(localization + database, 'w') as data:
            json.dump(obj_database, data, indent=4)
    print('Parabéns!!! Você se cadastrou!!!')

def generate_id(localization, database):
    while True:
        re = False
        user_id = [None, None, None, None]
        for c in range(4):
            user_id[c] = random.choice(string.ascii_uppercase + string.digits)
        with open(localization + database) as database_arc:
            database_obj = json.load(database_arc)
            for l in database_obj:
                if l['id'] == user_id:
                    re = True
                    break
            if re == True:
                continue
        str_user_id = str()
        for c in range(4):
            str_user_id += user_id[c]
        return str_user_id

def get_index_by_id(localization, database, user_id):
    with open(localization + database) as database_arc:
        database_obj = json.load(database_arc)
        for i, c in enumerate(database_obj):
            if c['id'] == user_id:
                return i

def play_forca(localization, database, index):
    victories, defeats = forca.jogo()
    tot_games = victories + defeats
    with open(localization + database) as database_arc:
        database_obj = json.load(database_arc)
        database_obj[index]['forca-victories'] += victories
        database_obj[index]['forca-defeats'] += defeats
        database_obj[index]['forca-games'] += tot_games
        with open(localization + database, 'w') as database_arc2:
            json.dump(database_obj, database_arc2, indent=4)

def info(username, email, password, rank, victories, defeats, tot_games, id):
    header('Informações da conta')
    print(F'''
---------------------------------------
 Nome de Usuário: {username}
 Email: {email}
 Senha: {'*' * len(password)}
 Rank: {rank}
 Id: {id}

 Forca:
    Vitórias: {victories}
    Derrotas: {defeats}
    Total de jogos: {tot_games}
---------------------------------------

''')

def management(localization, database_name):
    data = get_data(localization, database_name)
    header('Gerenciamento de contas!')
    while True:
        print('''
1 - Mudar rank
2 - Apagar contas
3 - Voltar
''')
        option = int(input('Opção: '))
        match option:
            case 1:
                print('----------------------------------------')
                for c in data:
                    print(F"{c['username']}".ljust(), F"{c['id']}".rjust(40))
                pass
            case 2:
                pass
            case 3:
                return
            case _:
                continue
