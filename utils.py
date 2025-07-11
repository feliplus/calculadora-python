"""
Utilitários para o projeto
"""

import json
from datetime import datetime

def save_data_to_json(data, filename):
    """Salva dados em arquivo JSON"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_data_from_json(filename):
    """Carrega dados de arquivo JSON"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def format_timestamp():
    """Retorna timestamp formatado"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

Commit simulado em 2022-05-23 12:00:00

Commit simulado em 2022-06-24 12:00:00

Commit simulado em 2022-07-01 12:00:00

Commit simulado em 2022-04-08 12:00:00
