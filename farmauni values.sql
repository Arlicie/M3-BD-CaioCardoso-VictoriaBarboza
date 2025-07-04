use farmauni;

-- Inserindo dados na tabela Unidade
INSERT INTO Unidade (codigo_unidade, endereco, cep) VALUES
(1, 'Rua A, 123', '12345-000'),
(2, 'Rua B, 456', '54321-000');

-- Inserindo dados na tabela Funcionario
INSERT INTO Funcionario (codigo_funcionario, nome, cargo, salario, cpf, email_interno, numero_telefone, data_nascimento, unidade_de_trabalho) VALUES
(1, 'Carlos Silva', 'Gerente', 5000.00, '12345678901', 'carlos@empresa.com', '11999999999', '1985-01-15', 1),
(2, 'Maria Oliveira', 'Analista', 3000.00, '10987654321', 'maria@empresa.com', '11888888888', '1990-05-20', 2);

-- Inserindo dados na tabela Medicamento
INSERT INTO Medicamento (codigo_medicamento, nome, descricao, laboratorio, preco, qtde_estoque) VALUES
(1, 'Paracetamol', 'Analgesico e antitérmico', 'Laboratório A', 10.50, 100),
(2, 'Ibuprofeno', 'Anti-inflamatório', 'Laboratório B', 12.00, 50);

-- Inserindo dados na tabela Entrega
INSERT INTO Entrega (codigo_entrega, nome_destinatario, endereco_destinatario, telefone_destinatario, total_compra, status, data_pedido_gerado, data_pedido_entregue, funcionario_responsavel, unidade_responsavel) VALUES
(1, 'João da Silva', 'Av. Central, 789', '11777777777', 100.00, 'não entregue', '2025-07-01 10:30:00', NULL, 1, 1),
(2, 'Ana Paula', 'Rua D, 321', '11666666666', 150.00, 'separação', '2025-07-01 11:35:00', NULL, 2, 2);

-- Inserindo dados na tabela Medicamento_Entrega
INSERT INTO Medicamento_Entrega (codigo_medicamento, codigo_entrega, quantidade) VALUES
(1, 1, 2),
(2, 1, 1),
(1, 2, 3);