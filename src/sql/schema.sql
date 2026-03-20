-- ===================================================
    -- Base de Dados: gestor_despesas
    -- Descrição: Estrutura da base de dados do sistema
    -- de gestão de despesas pessoais
    -- Autor: Erivaldo Jorge Centeio Lopes
    -- Data: 13/03/2026
    -- Curso: NST PROG28 - Programador de Infromática
-- ===================================================

-- Criação da base de dados
DROP DATABASE IF EXISTS gestor_despesas;
CREATE DATABASE gestor_despesas;

USE gestor_despesas;

-- Tabela de categorias de despesas
DROP TABLE IF EXISTS categorias;
CREATE TABLE categorias(
	id_categoria 			INT AUTO_INCREMENT PRIMARY KEY,
    nome 					VARCHAR(20) NOT NULL
);

-- Tabela de despesas
DROP TABLE IF EXISTS despesas;
CREATE TABLE despesas(
	id_despesa 				INT AUTO_INCREMENT PRIMARY KEY,
    descricao 				VARCHAR(30) NOT NULL,
    valor					DECIMAL(10, 2) NOT NULL,
    data					DATE NOT NULL,	
    id_categoria			int,
    
    CONSTRAINT id_categoria_FK FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);

-- Tabela de rendimentos
DROP TABLE IF EXISTS rendimentos;
CREATE TABLE rendimentos(
	id_despesas				INT AUTO_INCREMENT PRIMARY KEY,
    descricao				VARCHAR(30) NOT NULL,
    valor					DECIMAL(10, 2) NOT NULL,
    data					DATE NOT NULL
);

-- INSERT INTO categorias (NOME) 
-- VALUES ('Alimentação'),
-- 		('Transporte'),
--         ('Habitação'),
--         ('Lazer'),
--         ('Saude'),
--         ('Vestuario');

-- insert into despesas (descricao, valor, data, id_categoria)
-- values ('Supermercado',50.06, '2026-01-25',1),
-- 		('Consulta e exames', 95.00, '2026-01-23', 5)

-- insert into rendimentos (descricao, valor, data)
-- values ('Salário Janeiro ',1050.50, '2026-01-25'),
-- 		('Cartão alimentação', 120, '2026-01-23')