create schema farmauni;
use farmauni;

-- Criação da tabela Unidade
CREATE TABLE Unidade ( 
codigo_unidade INT PRIMARY KEY, 
endereco VARCHAR(255), 
cep VARCHAR(10) 
);

-- Criação da tabela Funcionario
CREATE TABLE Funcionario (
    codigo_funcionario INT PRIMARY KEY,
    nome VARCHAR(100),
    cargo VARCHAR(50),
    salario DECIMAL(10, 2),
    cpf VARCHAR(11) UNIQUE,
    email_interno VARCHAR(100) UNIQUE,
    numero_telefone VARCHAR(15) UNIQUE,
    data_nascimento DATE,
    unidade_de_trabalho INT,
    FOREIGN KEY (unidade_de_trabalho) REFERENCES Unidade(codigo_unidade)
);

-- Criação da tabela Medicamento
CREATE TABLE Medicamento (
    codigo_medicamento INT PRIMARY KEY,
    nome VARCHAR(100),
    descricao TEXT,
    laboratorio VARCHAR(100),
    preco DECIMAL(10, 2),
    qtde_estoque INT
);

-- Criação da tabela Entrega
CREATE TABLE Entrega (
    codigo_entrega INT PRIMARY KEY,
    nome_destinatario VARCHAR(100),
    endereco_destinatario VARCHAR(255),
    telefone_destinatario VARCHAR(15),
    total_compra DECIMAL(10, 2),
    funcionario_responsavel INT,
    unidade_responsavel INT,
    status VARCHAR(30) NOT NULL, -- feita, não feita, em tentativa, separação, não entregue
    data_pedido_gerado datetime NOT NULL,
    data_pedido_entregue datetime, 
    FOREIGN KEY (funcionario_responsavel) REFERENCES Funcionario(codigo_funcionario),
    FOREIGN KEY (unidade_responsavel) REFERENCES Unidade(codigo_unidade)
);

-- Criação da tabela Medicamento_Entrega
CREATE TABLE Medicamento_Entrega (
    codigo_medicamento INT,
    codigo_entrega INT,
    quantidade INT,
    PRIMARY KEY (codigo_medicamento, codigo_entrega),
    FOREIGN KEY (codigo_medicamento) REFERENCES Medicamento(codigo_medicamento),
    FOREIGN KEY (codigo_entrega) REFERENCES Entrega(codigo_entrega)
); 


