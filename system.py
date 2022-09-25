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

def management(localization, database_name, id_logged):
    while True:
        data = get_data(localization, database_name)
        header('Gerenciamento de contas!')
        print('''
1 - Mudar rank
2 - Apagar contas
3 - Voltar
''')
        while True:
            try:
                option = int(input('Opção: '))
                if 0 < option < 4:
                    break
            except:
                continue
        match option:
            case 1:
                users(localization, database_name)
                while True:
                    option2 = int(input('Qual usuário você quer trocar o rank? '))
                    if option2 < len(data):
                        break
                print('''
1 - admin
2 - normal
''')
                while True:
                    try:
                        option_rank = int(input('Opção: '))
                        if 0 <= option_rank < 3:
                            break
                    except:
                        continue
                if option_rank == 1:
                    data[option2]['rank'] = 'admin'
                elif option_rank == 2:
                    data[option2]['rank'] = 'normal'
                with open(localization + database_name, 'w') as database:
                    json.dump(data, database, indent=4)
            case 2:
                users(localization, database_name)
                while True:
                    try:
                        cant_delete = get_index_by_id(localization, database_name, id_logged)
                        option2 = int(input('Qual usuário você quer apagar? '))
                        if cant_delete == option2:
                            print('Você não pode deletar seu usuário dessa forma.')
                            continue
                        if 0 <= option2 < len(data):
                            break
                    except:
                        continue
                while True:
                    option3 = str(input('Tem certeza? ')).strip().upper()[0]
                    if option3 == 'N':
                        return
                    else:
                        break
                del data[option2]
                with open(localization + database_name, 'w') as database:
                    json.dump(data, database, indent=4)
            case 3:
                return
            case _:
                continue

def get_data_logged(localization, database_name, id_logged):
    data = get_data(localization, database_name)
    for c in data:
        if c['id'] == id_logged:
            return [c['username'],
                    c['email'],
                    c['password'],
                    c['rank'],
                    c['forca-victories'],
                    c['forca-defeats'],
                    c['forca-games']
]

def users(localization, database_name):
    data = get_data(localization, database_name)
    print('*' + '-' * 57 + '*')
    print(F'| Num |{"Nome de usuário" : ^31}|   Rank   |   ID   |')
    print('|-----|-------------------------------|----------|--------|')
    for l, c in enumerate(data):
        print(F"|  {l}  | {c['username'] : <30}|{c['rank'] : ^10}|{c['id'] : ^8}|")
    print('*' + '-' * 57 + '*')