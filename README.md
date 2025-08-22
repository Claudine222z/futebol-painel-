# 📊 Dashboard Football - Monitoramento

Dashboard web para acompanhar em tempo real os dados do sistema de coleta de futebol.

## 🌐 Acesso

**Dashboard Online:** [https://claudine222z.github.io/football-dashboard](https://claudine222z.github.io/football-dashboard)

## 📋 Funcionalidades

### 🔌 Status do Sistema
- Status da conexão com banco MySQL
- Última atualização dos dados
- Partidas ao vivo
- Partidas do dia

### 🗄️ Dados no Banco
- Contadores de todas as tabelas:
  - Países
  - Ligas
  - Temporadas
  - Times
  - Estádios
  - Treinadores
  - Jogadores
  - Classificações
  - Partidas
  - Estatísticas
  - Odds
  - Previsões

### ⚽ Partidas ao Vivo
- Lista de partidas em andamento
- Tempo de jogo
- Status atualizado

### 📅 Últimas Partidas
- Últimas 10 partidas coletadas
- Data e status

## 🔧 Como Funciona

Este dashboard é uma interface web estática que se conecta a um servidor API rodando na VPS para obter dados em tempo real do banco MySQL.

### Arquitetura:
```
GitHub Pages (Frontend) → VPS API (Backend) → MySQL Database
```

### APIs Utilizadas:
- `GET /api/stats` - Estatísticas do banco
- `GET /api/live-matches` - Partidas ao vivo
- `GET /api/recent-fixtures` - Partidas recentes

## 🎨 Características

- **Responsivo**: Funciona em desktop, tablet e mobile
- **Atualização Automática**: Dados atualizados a cada 30 segundos
- **Interface Moderna**: Design com gradientes e animações
- **Tempo Real**: Conexão direta com o banco de dados

## 🚀 Tecnologias

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python Flask (rodando na VPS)
- **Database**: MySQL
- **Hosting**: GitHub Pages

## 📱 Compatibilidade

- ✅ Chrome/Edge
- ✅ Firefox
- ✅ Safari
- ✅ Mobile browsers

## 🔒 Segurança

- Apenas dados de monitoramento são expostos
- Nenhuma informação sensível é transmitida
- Conexão segura via HTTPS (GitHub Pages)

---

**🏆 Sistema de Coleta de Dados de Futebol - Monitoramento em Tempo Real**
