reservas = {}

def boas_vindas():
    print("Bem-vindo à Cafeteria Expresso dos Sonhos!\n")
    print("Faça, consulte e cancele suas reservas a hora que quiser!\n")

def fazer_reserva(nome, horario):
    if horario in reservas:
        print("Desculpe, esse horário já está reservado.")
    else:
        reservas[horario] = nome
        print(f"Reserva feita para {nome} às {horario}.")

def consultar_reservas():
    if reservas:
        print("Reservas atuais:")
        for horario, nome in reservas.items():
            print(f"Horário: {horario}, Nome: {nome}")
    else:
        print("Não há reservas.")

def cancelar_reserva(horario):
    if horario in reservas:
        del reservas[horario]
        print(f"A reserva para o horário {horario} foi cancelada.")
    else:
        print("Não há reservas.")

def main():
    boas_vindas()
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Fazer reserva.")
        print("2. Consultar reservas.")
        print("3. Cancelar reserva.")
        print("4. Sair.")
        
        escolha = input("Digite o número que corresponde à sua escolha: ")
        
        if escolha == '1':
            nome = input("Digite seu nome: ")
            horario = input("Digite o horário que deseja fazer a reserva(ex: 13:00): ")
            fazer_reserva(nome, horario)
        elif escolha == '2':
            consultar_reservas()
        elif escolha == '3':
            horario = input("Digite o horário da reserva a ser cancelada (ex: 13:00): ")
            cancelar_reserva(horario)
        elif escolha == '4':
            print("Obrigado por utilizar o sistema de reservas da Cafeteria Expresso dos Sonhos! Volte sempre.")
            break
        else:
            print("Opção inválida! Por favor, tente novamente.")

if __name__ == "__main__":
    main()
