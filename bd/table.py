from flask import Flask, jsonify, request
import sqlite3
import uuid

# Configuração do banco de dados
DB_NAME = 'applications.db'

def create_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS applications (id TEXT, NotificationSubscription TEXT)')
    conn.commit()
    conn.close()

def insert_application(NotificationSubscription):
    # Verificar se a aplicação já está cadastrada
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM applications WHERE NotificationSubscription = ?', (NotificationSubscription,))
    result = c.fetchone()
    if result:
        conn.close()
        return result[0]  # Retorna o ID existente se a aplicação já estiver cadastrada

    # Gerar um novo ID
    id = str(uuid.uuid4())

    # Inserir a aplicação no banco de dados
    c.execute('INSERT INTO applications VALUES (?, ?)', (id, NotificationSubscription))
    conn.commit()
    conn.close()

    return id

def delete_application(id):
    # Deletar a aplicação do banco de dados
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM applications WHERE id = ?', (id,))
    conn.commit()
    conn.close()