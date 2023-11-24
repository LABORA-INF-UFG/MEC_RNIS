from flask import Flask, jsonify, request
import sqlite3
import uuid
import requests

# Configuração do banco de dados
DB_NAME = 'applications.db'

# Cria a tabela contendo 
# id, ientifer,NotificationSubscription e callback_uri
def create_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id VARCHAR(36) PRIMARY KEY,
            identifier VARCHAR(36) NOT NULL,
            NotificationSubscription VARCHAR(50) NOT NULL,
            callback_uri VARCHAR(200) NOT NULL
        )
    ''')
    #c.execute('CREATE TABLE IF NOT EXISTS applications (id VARCHAR(36), identifier VARCHAR(36), NotificationSubscription VARCHAR(50), callback_uri VARCHAR(200))')
    conn.commit()
    conn.close()

# insert no bd
def insert_application(identifier, NotificationSubscription, callback_uri):
    # Verificar se a aplicação já está cadastrada
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM applications WHERE identifier = ?', (identifier,))
    result = c.fetchone()
    if result:
        conn.close()
        return result[0]  # Retorna o ID existente se a aplicação já estiver cadastrada

    # Gerar um novo ID
    id = str(uuid.uuid4())

    # Inserir a aplicação no banco de dados
    c.execute('INSERT INTO applications VALUES (?, ?, ?, ?)', (id, identifier, NotificationSubscription, callback_uri))
    conn.commit()
    conn.close()

    return id

# deleta algum cadastro do bd
def delete_application(id):
    # Deletar a aplicação do banco de dados
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM applications WHERE id = ?', (id,))
    conn.commit()
    conn.close()




#-----------------------------------------------------#

# lista os dados do bd
def get_application_list():

    # Obter a lista de IDs e identificadores cadastrados
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT id, identifier, NotificationSubscription, callback_uri FROM applications')
    rows = c.fetchall()
    conn.close()
    return [{'id': row[0], 'identifier': row[1], 'NotificationSubscription': row[2], 'callback_uri': row[3]} for row in rows]

    
def listar_callback_apps_por_notification(NotificationSubscription):
    try:
        
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute('SELECT callback_uri FROM applications WHERE NotificationSubscription = ?', (NotificationSubscription,))
        callback_uri = [row[0] for row in cursor.fetchall()]
        #resultados = cursor.fetchall()
        #callback_uri = [row[0] for row in resultados]
        conn.close()
        
        if not callback_uri:
            return jsonify({'erro': 'Nenhum cliente encontrado para o tópico especificado'}), 404
        
        return jsonify({'apps': callback_uri}), 200
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# Função para obter todos os clientes com o mesmo tópico
def listar_callback_apps_por_notification2(NotificationSubscription):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT callback_uri FROM applications WHERE NotificationSubscription = ?', (NotificationSubscription,))
    resultados = cursor.fetchall()
    conn.close()
    
    return resultados

# Função para obter todos os clientes e a lista de callback_uri
def listar_callback_apps():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT callback_uri, NotificationSubscription FROM applications')
    resultados = cursor.fetchall()
    conn.close()
    
    return resultados
    #return resultados
