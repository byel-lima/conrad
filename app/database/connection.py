# teste_conexao.py
from schema.sql import test_connection
 
class Suporte:
    def executar_teste_conexao(self):
        print("Iniciando teste de conexão de suporte...")
        ok = test_connection()
 
        if ok:
            print("Teste da suporte: conexão OK.")
        else:
            print("Teste da suporte: conexão falhou.")
 
    TelaSuporte().executar_teste_conexao()