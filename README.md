# GitHub Actions Workshop - Calculator API

[![Базовый CI](https://github.com/fadeinflames/github-actions-workshop/actions/workflows/01-basic.yml/badge.svg)](https://github.com/fadeinflames/github-actions-workshop/actions/workflows/01-basic.yml)

[![CI с тестированием](https://github.com/fadeinflames/github-actions-workshop/actions/workflows/02-testing.yml/badge.svg)](https://github.com/fadeinflames/github-actions-workshop/actions/workflows/02-testing.yml)

[![Матричное тестирование](https://github.com/fadeinflames/github-actions-workshop/actions/workflows/03-matrix.yml/badge.svg)](https://github.com/fadeinflames/github-actions-workshop/actions/workflows/03-matrix.yml)

[![Production CI/CD](https://github.com/fadeinflames/github-actions-workshop/actions/workflows/04-production.yml/badge.svg)](https://github.com/fadeinflames/github-actions-workshop/actions/workflows/04-production.yml)

[![Продвинутые возможности](https://github.com/fadeinflames/github-actions-workshop/actions/workflows/05-advanced.yml/badge.svg)](https://github.com/fadeinflames/github-actions-workshop/actions/workflows/05-advanced.yml)

Учебный проект для демонстрации возможностей GitHub Actions в курсе DevOps.

## 📋 Описание проекта

Простое Flask API для выполнения математических операций. Проект демонстрирует построение полноценного CI/CD pipeline с использованием GitHub Actions.

## 🚀 Возможности приложения

- **REST API** для калькулятора
- Базовые математические операции: сложение, вычитание, умножение, деление, возведение в степень
- Health check endpoint
- Полное покрытие тестами
- Контейнеризация с Docker

## 🏗️ Структура проекта

```
.
├── app/
│   ├── __init__.py
│   ├── calculator.py      # Логика калькулятора
│   └── api.py            # Flask API
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py # Unit тесты
│   └── test_api.py       # Integration тесты
├── .github/
│   └── workflows/        # GitHub Actions workflows
│       ├── 01-basic.yml
│       ├── 02-testing.yml
│       ├── 03-matrix.yml
│       ├── 04-production.yml
│       └── 05-advanced.yml
├── requirements.txt
├── pytest.ini
├── Dockerfile
└── README.md
```

## 🧪 Запуск тестов локально

```bash
# Установка зависимостей
pip install -r requirements.txt

# Запуск всех тестов
pytest tests/ -v

# Запуск с покрытием
pytest tests/ --cov=app --cov-report=term-missing

# Параллельный запуск
pytest tests/ -n auto
```

## 🐳 Docker

```bash
# Сборка образа
docker build -t calculator-api .

# Запуск контейнера
docker run -p 5000:5000 calculator-api

# Проверка работоспособности
curl http://localhost:5000/health
```

## 📝 API Endpoints

### Health Check
```bash
GET /health
```

Ответ:
```json
{
  "status": "healthy",
  "service": "calculator-api",
  "version": "1.0.0"
}
```

### Calculate
```bash
POST /calculate
Content-Type: application/json

{
  "operation": "add",
  "a": 5,
  "b": 3
}
```

Поддерживаемые операции:
- `add` - сложение
- `subtract` - вычитание
- `multiply` - умножение
- `divide` - деление
- `power` - возведение в степень

Ответ:
```json
{
  "operation": "add",
  "a": 5,
  "b": 3,
  "result": 8
}
```

## 🔄 GitHub Actions Workflows

### 01-basic.yml
Базовый workflow для знакомства с синтаксисом.

### 02-testing.yml
Pipeline с установкой зависимостей, кэшированием и запуском тестов.

### 03-matrix.yml
Матричное тестирование на разных версиях Python и ОС.

### 04-production.yml
Production-ready pipeline с несколькими jobs, зависимостями и Docker.

### 05-advanced.yml
Продвинутые возможности: секреты, переменные, условное выполнение.

## 📚 Используемые технологии

- **Python 3.11** - язык программирования
- **Flask** - веб-фреймворк
- **pytest** - фреймворк для тестирования
- **pytest-cov** - покрытие кода тестами
- **pytest-xdist** - параллельный запуск тестов
- **Docker** - контейнеризация
- **GitHub Actions** - CI/CD

## 🎓 Цели обучения

1. Понимание структуры GitHub Actions workflows
2. Настройка автоматической сборки и тестирования
3. Работа с артефактами и кэшированием
4. Матричные стратегии тестирования
5. Зависимости между jobs
6. Условное выполнение
7. Интеграция с Docker
8. Best practices для CI/CD

## 📖 Дополнительные материалы

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow syntax reference](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
- [pytest Documentation](https://docs.pytest.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
