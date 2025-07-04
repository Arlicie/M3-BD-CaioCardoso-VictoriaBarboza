from mysql.connector import Error
import mysql.connector
import time

'''
    Prof, na conexeão com o banco de dados, caso necessário, você pode alterar o nome do usuário, 
    senha e banco de dados. Porém não consegui rodar o código direito, o MySQL estava dando uns erros e eu não consegui resolver.
'''
conn = None  # Initialize conn to None
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='vicky1478!MS',
        database='farmauni'
    )
    if conn.is_connected():
        print("Conexão bem-sucedida!")
except Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

'''
    O menu foi feito de forma mais extensiva para facilitar a criação do código e tabém foi utilizado
    time.sleep para melhor visualização do menu.
'''
def menu():
    while True:
        print("\n--- Menu Funcionario ---")
        print("01. Inserir Funcionário")
        print("02. Consultar um Funcionário")
        print("03. Listar funcionario")
        print("04. Atualizar Funcionário")
        print("05. Deletar Funcionário")

        time.sleep(1)

        print("\n--- Menu Medicamento ---")
        print("06. Inserir Medicamento")
        print("07. Consultar um Medicamento")
        print("08. Listar Medicamentos")
        print("09. Atualizar estoque Medicamento")
        print("10. Deletar Medicamento")

        time.sleep(1)

        print("\n--- Menu Entrega ---")
        print("11. Gerar registro de Entrega")
        print("12. Consultar Entrega")
        print("13. Listar Entregas")
        print("14. Atualizar status de Entrega")
        print("15. Deletar Entrega")
        
        time.sleep(1)

        print("\n--- Menu Unidade ---")
        print("16. Inserir Unidade")
        print("17. Listar Unidades")
        print("18. Deletar Unidade")

        time.sleep(1)

        print("\n0. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            inserir_funcionario()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "2":
            consultar_funcionario()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "3":
            listar_funcionarios()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "4":
            print("\n Essa opção ainda não está implementada!")
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "5":
            deletar_funcionario()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "6":
            inserir_medicamento()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "7":
            consultar_medicamento()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "8":
            listar_medicamentos()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "9":
            print("\n Essa opção ainda não está implementada!")
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "10":
            deletar_medicamento()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "11":
            inserir_entrega_medicamentos()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "12":
            consultar_entrega()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "13":
            listar_entregas()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "14":
            atualizar_status_entrega()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "15":
            deletar_entrega()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "16":
            inserir_unidade()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()
        elif opcao == "17": 
            listar_unidades()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu() 
        elif opcao == "18":
            deletar_unidade()
            print("\n Você está sendo redirecionado para o menu principal...")
            time.sleep(2)
            menu()  
        elif opcao == "0":
            print("Saindo do sistema...")
            time.sleep(1)
            break
            
def inserir_funcionario(): 
    cursor = conn.cursor()
    print("\n-- Inserir Funcionário --")
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = float(input("Salário: "))
    cpf = input("CPF: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    nascimento = input("Data de nascimento (YYYY-MM-DD): ")
    unidade = int(input("Código da unidade de trabalho: "))  
    sql = dados = (nome, cargo, salario, cpf, email, telefone, nascimento, unidade)
    cursor.execute(sql, dados)
    conn.commit()
    print("Funcionário inserido com sucesso. ID gerado:", cursor.lastrowid)
    cursor.close()

def consultar_funcionario():
    cursor = conn.cursor()
    
    print("\n-- Consultar Funcionário --")
    codigo = int(input("ID do funcionário a ser atualizado: "))
    sql = "SELECT * FROM Funcionario WHERE codigo_funcionario = %s"
    cursor.execute(sql, (codigo,))
    resultado = cursor.fetchone()  

    if resultado:
        print("\nInformações do Funcionário:")
        print(f"Código: {resultado[0]}")
        print(f"Nome: {resultado[1]}")
        print(f"Cargo: {resultado[2]}")
        print(f"Salário: R$ {resultado[3]:.2f}")
        print(f"CPF: {resultado[4]}")
        print(f"E-mail: {resultado[5]}")
        print(f"Telefone: {resultado[6]}")
        print(f"Nascimento: {resultado[7]}")
        print(f"Unidade de Trabalho: {resultado[8]}")
    else:
        print("Funcionário não encontrado.")

    cursor.close()

def listar_funcionarios():
    cursor = conn.cursor()
    print("\n-- Listar Funcionários --")
    sql = "SELECT * FROM Funcionario"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    if resultados:
        for funcionario in resultados:
            print(f"\nCódigo: {funcionario[0]}")
            print(f"Nome: {funcionario[1]}")
            print(f"Cargo: {funcionario[2]}")
            print(f"Salário: R$ {funcionario[3]:.2f}")
            print(f"CPF: {funcionario[4]}")
            print(f"E-mail: {funcionario[5]}")
            print(f"Telefone: {funcionario[6]}")
            print(f"Nascimento: {funcionario[7]}")
            print(f"Unidade de Trabalho: {funcionario[8]}")
    else:
        print("Nenhum funcionário encontrado.")

    cursor.close()
'''
def atualizar_funcionario():
    cursor = conn.cursor()
    
    while true:
        print("\n-- Qual campo deseja atualizar? --")
        print("1. Nome")
        print("2. Cargo")
        print("3. Salário")
        print("4. CPF")
        print("5. Email")
        print("6. Telefone")
        print("7. Data de nascimento")
        print("8. Unidade de trabalho")
        print("9. Todos os campos")
        print("0. Voltar ao menu principal")
        campo = input("Escolha o número do campo: ")
        if campo == "1":
            atualizar_nome(cursor)
        elif campo == "2":
            atualizar_cargo(cursor)
        elif campo == "3":
            atualizar_salario(cursor)
        elif campo == "4":
            atualizar_cpf(cursor)
        elif campo == "5":
            atualizar_email(cursor)
        elif campo == "6":
            atualizar_telefone(cursor)
        elif campo == "7":
            atualizar_nascimento(cursor)
        elif campo == "8":
            atualizar_unidade(cursor)
        elif campo == "9":
            atualizar_todos(cursor)
        elif campo == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
        
    print("\n-- Atualizar Funcionário --")
    funcionario_id = int(input("ID do funcionário a ser atualizado: "))
    nome = input("Novo nome: ")
    cargo = input("Novo cargo: ")
    salario = float(input("Novo salário: "))
    cpf = input("Novo CPF: ")
    email = input("Novo email: ")
    telefone = input("Novo telefone: ")
    nascimento = input("Nova data de nascimento (YYYY-MM-DD): ")
    unidade = int(input("Novo código da unidade de trabalho: "))
    sql = "UPDATE funcionario SET nome = %s, cargo = %s, salario = %s, cpf = %s, email = %s, telefone = %s, nascimento = %s, unidade_id = %s WHERE id = %s"
    dados = (nome, cargo, salario, cpf, email, telefone, nascimento, unidade, funcionario_id)
    cursor.execute(sql, dados)
    conn.commit()
    print("Funcionário atualizado com sucesso.")
    cursor.close()
    '''

def deletar_funcionario():
    cursor = conn.cursor()

    print("\n-- Deletar Funcionário --")
    print("Atenção: Esta ação não pode ser desfeita.")
    codigo = int(input("Digite o código do funcionário a ser deletado: "))
    cursor.execute("SELECT * FROM Funcionario WHERE codigo_funcionario = %s", (codigo,))
    funcionario = cursor.fetchone()

    if funcionario:
        cursor.execute("DELETE FROM Funcionario WHERE codigo_funcionario = %s", (codigo,))
        conn.commit()
        print("Funcionário deletado com sucesso.")
    else:
        print("Funcionário não encontrado.")
    
    cursor.close()


def inserir_medicamento(): 
    cursor = conn.cursor()
    print("\n-- Inserir Medicamento --")
    nome = input("Nome: ")
    descricao = input("Descricao: ")
    laboratorio = input("Laboratorio: ")
    preco = input("Preco: ")
    qtde_estoque = input("Quantidade em estoque: ")
    sql = dados = (nome, descricao, laboratorio, preco, qtde_estoque)
    cursor.execute(sql, dados)
    conn.commit()
    print("Medicamento inserido com sucesso. ID gerado:", cursor.lastrowid)
    cursor.close()

def consultar_medicamento():
    cursor = conn.cursor()
    
    print("\n-- Consultar Medicamento --")
    codigo = int(input("ID do medicamento a ser atualizado: "))
    sql = "SELECT * FROM Medicamento WHERE codigo_medicamento = %s"
    cursor.execute(sql, (codigo,))
    resultado = cursor.fetchone()  

    if resultado:
        print("\nInformações do Funcionário:")
        print(f"Código: {resultado[0]}")
        print(f"Nome: {resultado[1]}")
        print(f"Descrição: {resultado[2]}")
        print(f"Laboratorio: {resultado[3]:.2f}")
        print(f"Preço: R$ {resultado[4]}")
        print(f"Quantidade no estoque: {resultado[5]}")
    else:
        print("Medicamento não encontrado.")

    cursor.close()

def listar_medicamentos():
    cursor = conn.cursor()
    print("\n-- Listar Medicamentos --")
    sql = "SELECT * FROM Medicamento"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    if resultados:
        for medicamento in resultados:
            print(f"\nCódigo: {medicamento[0]}")
            print(f"Nome: {medicamento[1]}")
            print(f"Descrição: {medicamento[2]}")
            print(f"Laboratorio: {medicamento[3]}")
            print(f"Preço: R$ {medicamento[4]:.2f}")
            print(f"Quantidade no estoque: {medicamento[5]}")
        else:
            print("Nenhum medicamento encontrado.")

def deletar_medicamento():
    cursor = conn.cursor()
    print("\n-- Deletar Medicamento --")
    codigo = int(input("Digite o código do medicamento a ser deletado: "))
    cursor.execute("SELECT * FROM Medicamento WHERE codigo_medicamento = %s", (codigo,))
    med = cursor.fetchone()

    if med:
        cursor.execute("DELETE FROM Medicamento WHERE codigo_medicamento = %s", (codigo,))
        conn.commit()
        print("Medicamento deletado com sucesso.")
    else:
        print("Medicamento não encontrado.")
    
    cursor.close()


def inserir_entrega_medicamentos():
    cursor = conn.cursor()
    print("\n-- Inserir nova entrega --")
    nome = input("Nome do destinatário: ")
    endereco = input("Endereço do destinatário: ")
    telefone = input("Telefone do destinatário: ")
    total = float(input("Total da compra: "))
    status = input("Status (feita, separação, etc): ")
    data_gerado = input("Data do pedido gerado (YYYY-MM-DD HH:MM:SS): ")
    funcionario = int(input("Código do funcionário responsável: "))
    unidade = int(input("Código da unidade responsável: "))

    # Inserindo a entrega
    sql_entrega = """
    INSERT INTO Entrega (
        nome_destinatario, endereco_destinatario, telefone_destinatario,
        total_compra, status, data_pedido_gerado,
        funcionario_responsavel, unidade_responsavel
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    dados_entrega = (nome, endereco, telefone, total, status, data_gerado, funcionario, unidade)
    cursor.execute(sql_entrega, dados_entrega)
    conn.commit()

    id_entrega = cursor.lastrowid
    print(f"\nEntrega inserida com sucesso! Código gerado: {id_entrega}")

    # Loop para adicionar medicamentos à entrega
    while True:
        print("\n-- Vincular medicamento à entrega --")
        codigo_medicamento = int(input("Código do medicamento: "))
        quantidade = int(input("Quantidade: "))

        sql_medicamento_entrega = """
        INSERT INTO Medicamento_Entrega (codigo_medicamento, codigo_entrega, quantidade)
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql_medicamento_entrega, (codigo_medicamento, id_entrega, quantidade))
        conn.commit()
        print("Medicamento vinculado com sucesso.")

        continuar = input("Deseja adicionar outro medicamento para essa entrega? (s/n): ").lower()
        if continuar != 's':
            break

    print("Entrega finalizada com medicamentos adicionados.")
    
    cursor.close()

def consultar_entrega():
    cursor = conn.cursor()
    print("\n-- Consultar Entrega --")
    codigo = int(input("Digite o código da entrega: "))
    cursor.execute("SELECT * FROM Entrega WHERE codigo_entrega = %s", (codigo,))
    entrega = cursor.fetchone()

    if entrega:
        for chave, valor in entrega.items():
            print(f"{chave}: {valor}")
    else:
        print("Entrega não encontrada.")

    cursor.close()

def listar_entregas():
    cursor = conn.cursor()
    print("\n-- Lista de Entregas com Medicamentos --")
    
    # Consulta todas as entregas
    cursor.execute("SELECT * FROM Entrega")
    entregas = cursor.fetchall()

    if not entregas:
        print("Nenhuma entrega encontrada.")
        return

    for entrega in entregas:
        print("\n===============================")
        print(f"Código da entrega: {entrega['codigo_entrega']}")
        print(f"Destinatário: {entrega['nome_destinatario']}")
        print(f"Endereço: {entrega['endereco_destinatario']}")
        print(f"Telefone: {entrega['telefone_destinatario']}")
        print(f"Total da compra: R$ {entrega['total_compra']:.2f}")
        print(f"Status: {entrega['status']}")
        print(f"Data do pedido gerado: {entrega['data_pedido_gerado']}")
        print(f"Data de saída: {entrega['data_pedido_saida']}")
        print(f"Data de entrega: {entrega['data_pedido_entregue']}")
        print(f"Funcionário responsável (ID): {entrega['funcionario_responsavel']}")
        print(f"Unidade responsável (ID): {entrega['unidade_responsavel']}")

        # Consulta os medicamentos dessa entrega
        cursor.execute("""
            SELECT me.quantidade, m.nome
            FROM Medicamento_Entrega me
            JOIN Medicamento m ON me.codigo_medicamento = m.codigo_medicamento
            WHERE me.codigo_entrega = %s
        """, (entrega['codigo_entrega'],))
        medicamentos = cursor.fetchall()

        if medicamentos:
            print("\n  Medicamentos:")
            for med in medicamentos:
                print(f"   - {med['nome']} (Quantidade: {med['quantidade']})")
        else:
            print("  Nenhum medicamento registrado nesta entrega.")
    cursor.close()

def atualizar_status_entrega():
    cursor = conn.cursor()
    print
    codigo = int(input("\nDigite o código da entrega a ser atualizada: "))
    novo_status = input("\nDigite o novo status: ")
    if novo_status == "entregue":
        print("\nA entrega foi marcada como entregue.")
        print("\nInforme a data de entrega (YYYY-MM-DD HH:MM:SS): ")
        data_entrega = input()
        cursor.execute("UPDATE Entrega SET status = %s, data_entrega = %s WHERE codigo_entrega = %s", (novo_status, data_entrega, codigo))
    elif novo_status == "cancelada":
        print("\nA entrega foi cancelada.")
        cursor.execute("UPDATE Entrega SET status = %s, WHERE codigo_entrega = %s", (novo_status, codigo))
    else:
        cursor.execute("UPDATE Entrega SET status = %s WHERE codigo_entrega = %s", (novo_status, codigo))
    conn.commit()
    print("Status atualizado com sucesso.")
    cursor.close()

def deletar_entrega():
    cursor = conn.cursor()
    codigo = int(input("Digite o código da entrega a ser deletada: "))
    cursor.execute("SELECT * FROM Entrega WHERE codigo_entrega = %s", (codigo,))

    print("\n-- Deletar Entrega --")

    entrega = cursor.fetchone()

    if entrega:
        cursor.execute("DELETE FROM Entrega WHERE codigo_entrega = %s", (codigo,))
        conn.commit()
        print("Entrega deletada com sucesso.")
    else:
        print("Entrega não encontrada.")

    cursor.close()

def deletar_medicamento_entrega():
    cursor = conn.cursor()
    cod_entrega = int(input("Código da entrega: "))
    cod_medicamento = int(input("Código do medicamento: "))

    print("\n-- Deletar Medicamento de Entrega --")

    cursor.execute("""
        DELETE FROM Medicamento_Entrega
        WHERE codigo_entrega = %s AND codigo_medicamento = %s
    """, (cod_entrega, cod_medicamento))
    conn.commit()
    print("Remoção realizada (se existia).")
    cursor.close()

def inserir_unidade():
    cursor = conn.cursor()
    print("\n-- Inserir Unidade --")
    endereco = input("Endereço da unidade: ")
    cep = input("CEP (xxxxx-xxx): ")

    sql = "INSERT INTO Unidade (endereco, cep) VALUES (%s, %s)"
    cursor.execute(sql, (endereco, cep))
    conn.commit()
    print("Unidade inserida com sucesso. Código:", cursor.lastrowid)
    cursor.close()

def listar_unidades():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Unidade")
    unidades = cursor.fetchall()

    if unidades:
        for u in unidades:
            print(f"\nCódigo: {u['codigo_unidade']}, Endereço: {u['endereco']}, CEP: {u['cep']}")
    else:
        print("Nenhuma unidade encontrada.")

    cursor.close()

def deletar_unidade():
    cursor = conn.cursor()
    print("\n-- Deletar Unidade --")
    codigo = int(input("Digite o código da unidade a ser deletada: "))
    cursor.execute("SELECT * FROM Unidade WHERE codigo_unidade = %s", (codigo,))
    unidade = cursor.fetchone()

    if unidade:
        cursor.execute("DELETE FROM Unidade WHERE codigo_unidade = %s", (codigo,))
        conn.commit()
        print("Unidade deletada com sucesso.")
    else:
        print("Unidade não encontrada.")
    cursor.close()

menu()