import mysql.connector
 
def get_connection(
    host="localhost",
    user="root",
    password="",
    database="conrad"
):
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
 
        if conn.is_connected():
            print(f"[SUCESSO] Conectado ao MySQL ({user}@{host}/{database})")
            return conn
 
    except Exception as e:
        print(f"[ERRO] Não foi possível conectar ao MySQL: {e}")
 
    return None
 
 
def test_connection():
    conn = get_connection()
    if conn:
        conn.close()
        print("[SUCESSO] Conexão encerrada com sucesso.")
        return True
    else:
        print("[ERRO] Falha ao conectar ao banco de dados.")
        return False