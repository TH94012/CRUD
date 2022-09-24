from system import *


localization = 'c:/Users/User/dev/CRUD/'
database_name = 'database.json'

create_database(localization, database_name)
data = get_data(localization, database_name)

logged = False

while True:
    header('Bem vindo ao Login')
    print('''\033[1;33m
1 - Login
2 - Registrar
3 - Sair do programa
\033[m''')
    while True:
        try:
            option1 = int(input(cyan + 'Opção: ' + yellow))
        except:
            continue
        if option1 > 3:
            continue
        elif option1 < 1:
            continue
        break
    if option1 == 1:
        username_logged, email_logged, password_logged, rank_logged, victories_logged, defeats_logged, games_logged, id_logged = login(localization, database_name)
        logged = True
        #print(F'{username_logged} {email_logged} {password_logged} {rank_logged} {victories_logged} {id_logged}')
        while True:
            if logged == False:
                break
            header(F'Conectado com o rank {rank_logged}')
            print('''
1 - Forca
2 - Logout
3 - Informações Conta''')
            if rank_logged == 'admin':
                print('''4 - Gerenciar contas''')
            print()
            while True:
                try:
                    option2 = int(input('Opção: '))
                    if 0 < option2 < 5:
                        if option2 == 4:
                            if rank_logged == 'admin':
                                pass
                            else:
                                continue
                    else:
                        continue
                except:
                    continue
                else:
                    break
            match option2:
                case 1:
                    play_forca(localization, database_name, get_index_by_id(localization, database_name, id_logged))
                case 2:
                    username_logged = email_logged = password_logged = rank_logged = victories_logged = id_logged = None
                    logged = False
                    break
                case 3:
                    while True:
                        info(username_logged, email_logged, password_logged, rank_logged, victories_logged, defeats_logged, games_logged, id_logged)
                        input('Voltar ')
                case 4:
                    management(localization, database_name)
                case _:
                    raise Exception('Você bugou o sistema!')
    elif option1 == 2:
        register(localization, database_name)
    else:
        break
print(F'{cyan}Volte Sempre!\033[m')