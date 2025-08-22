#!/usr/bin/env python3
"""
📊 DASHBOARD MONITOR - VERSÃO CORRIGIDA
=======================================
Dashboard com CORS habilitado para GitHub Pages
Credenciais corretas do Coolify
"""

from flask import Flask, jsonify, render_template_string
from flask_cors import CORS  # IMPORTANTE: Habilita CORS
import mysql.connector
import time
import json
from datetime import datetime, timedelta
import os

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Configuração do banco CORRIGIDA com dados do Coolify
DB_CONFIG = {
    'host': '72.60.1.170',
    'port': 3306,
    'database': 'default',  # Nome correto do banco
    'user': 'football_user',  # Usuário correto
    'password': 'x9fR6snV9PT4K04qlqXlFxzwhTqGadzntJvud1zH5Tw5CyMT1LJT3RQ4bz8M5o9j'  # Senha correta
}

def get_db_connection():
    """Cria conexão com o banco MySQL"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Exception as e:
        print(f"❌ Erro ao conectar no banco: {e}")
        return None

def get_database_stats():
    """Obtém estatísticas do banco de dados"""
    try:
        conn = get_db_connection()
        if not conn:
            return {"error": "Falha na conexão com banco", "status": "error"}
        
        cursor = conn.cursor()
        stats = {}
        
        # Conta registros por tabela
        tables = ['countries', 'leagues', 'seasons', 'teams', 'venues', 'coaches', 'players', 'standings', 'fixtures', 'statistics', 'odds', 'predictions']
        
        for table in tables:
            try:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                stats[f"{table}_count"] = count
            except:
                stats[f"{table}_count"] = 0
        
        # Últimas atualizações
        try:
            cursor.execute("SELECT MAX(created_at) FROM fixtures")
            last_fixture = cursor.fetchone()[0]
            stats['last_fixture_update'] = str(last_fixture) if last_fixture else "N/A"
        except:
            stats['last_fixture_update'] = "N/A"
        
        # Partidas ao vivo
        try:
            cursor.execute("SELECT COUNT(*) FROM fixtures WHERE status = 'Live'")
            live_count = cursor.fetchone()[0]
            stats['live_matches'] = live_count
        except:
            stats['live_matches'] = 0
        
        # Partidas hoje
        try:
            today = datetime.now().strftime('%Y-%m-%d')
            cursor.execute("SELECT COUNT(*) FROM fixtures WHERE DATE(fixture_date) = %s", (today,))
            today_count = cursor.fetchone()[0]
            stats['matches_today'] = today_count
        except:
            stats['matches_today'] = 0
        
        cursor.close()
        conn.close()
        
        stats['last_update'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        stats['status'] = 'connected'
        
        return stats
        
    except Exception as e:
        return {"error": str(e), "status": "error"}

def get_recent_fixtures():
    """Obtém partidas recentes"""
    try:
        conn = get_db_connection()
        if not conn:
            return []
        
        cursor = conn.cursor(dictionary=True)
        
        # Últimas 10 partidas
        cursor.execute("""
            SELECT team_home_name, team_away_name, status, fixture_date, league_id
            FROM fixtures 
            ORDER BY created_at DESC 
            LIMIT 10
        """)
        
        fixtures = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return fixtures
        
    except Exception as e:
        return []

def get_live_matches():
    """Obtém partidas ao vivo"""
    try:
        conn = get_db_connection()
        if not conn:
            return []
        
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("""
            SELECT team_home_name, team_away_name, status, elapsed_time, league_id
            FROM fixtures 
            WHERE status = 'Live'
            ORDER BY created_at DESC
        """)
        
        matches = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return matches
        
    except Exception as e:
        return []

# Rotas da API
@app.route('/')
def home():
    """Página inicial"""
    return jsonify({
        "message": "Dashboard API funcionando!",
        "status": "online",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    """Healthcheck para GitHub Pages"""
    stats = get_database_stats()
    if stats.get('status') == 'connected':
        return jsonify({
            'status': 'healthy',
            'message': 'Dashboard funcionando',
            'database': 'connected',
            'timestamp': datetime.now().isoformat()
        }), 200
    else:
        return jsonify({
            'status': 'unhealthy',
            'message': 'Problema na conexão com banco',
            'database': 'disconnected',
            'timestamp': datetime.now().isoformat()
        }), 503

@app.route('/api/stats')
def api_stats():
    """API para estatísticas do banco"""
    return jsonify(get_database_stats())

@app.route('/api/live-matches')
def api_live_matches():
    """API para partidas ao vivo"""
    return jsonify(get_live_matches())

@app.route('/api/recent-fixtures')
def api_recent_fixtures():
    """API para partidas recentes"""
    return jsonify(get_recent_fixtures())

@app.route('/test')
def test():
    """Rota de teste"""
    return jsonify({
        "message": "API funcionando!",
        "cors": "habilitado",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("🚀 Iniciando Dashboard Monitor (Versão Corrigida)...")
    print("🌐 Dashboard disponível em: http://72.60.1.170:5000")
    print("📋 APIs disponíveis:")
    print("   - GET / - Página inicial")
    print("   - GET /health - Healthcheck")
    print("   - GET /test - Teste de CORS")
    print("   - GET /api/stats - Estatísticas do banco")
    print("   - GET /api/live-matches - Partidas ao vivo")
    print("   - GET /api/recent-fixtures - Partidas recentes")
    print("🔧 CORS habilitado para GitHub Pages")
    print("🗄️ Conectando no banco: football_stats_mysql (Coolify)")
    
    app.run(host='0.0.0.0', port=5000, debug=False)
