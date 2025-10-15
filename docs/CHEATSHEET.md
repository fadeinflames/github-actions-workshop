# GitHub Actions - Шпаргалка

## 📝 Основной синтаксис

### Структура workflow файла

```yaml
name: Название workflow

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:

env:
  GLOBAL_VAR: значение

jobs:
  job-name:
    runs-on: ubuntu-latest
    env:
      JOB_VAR: значение
    
    steps:
      - name: Название шага
        uses: action/name@version
        with:
          parameter: значение
      
      - name: Команда
        run: |
          команда 1
          команда 2
        env:
          STEP_VAR: значение
```

## 🎯 Триггеры (on)

```yaml
# Push в определенные ветки
on:
  push:
    branches: [ main, develop ]
    paths:
      - 'src/**'

# Pull Request
on:
  pull_request:
    branches: [ main ]
    types: [opened, synchronize, reopened]

# Расписание (cron)
on:
  schedule:
    - cron: '0 2 * * *'  # Каждый день в 2:00 UTC

# Ручной запуск
on:
  workflow_dispatch:
    inputs:
      environment:
        description: 'Environment to deploy'
        required: true
        default: 'staging'

# Несколько триггеров
on: [push, pull_request, workflow_dispatch]
```

## 🖥️ Runners

```yaml
# Ubuntu (самый популярный)
runs-on: ubuntu-latest
runs-on: ubuntu-22.04
runs-on: ubuntu-20.04

# Windows
runs-on: windows-latest
runs-on: windows-2022

# macOS
runs-on: macos-latest
runs-on: macos-13
```

## 🔧 Популярные Actions

### Checkout кода
```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 0  # Полная история
    submodules: true  # С субмодулями
```

### Установка Python
```yaml
- uses: actions/setup-python@v5
  with:
    python-version: '3.11'
    cache: 'pip'  # Встроенное кэширование
```

### Установка Node.js
```yaml
- uses: actions/setup-node@v4
  with:
    node-version: '20'
    cache: 'npm'
```

### Кэширование
```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/.cache/pip
      ~/.npm
    key: ${{ runner.os }}-${{ hashFiles('**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-
```

### Загрузка артефактов
```yaml
- uses: actions/upload-artifact@v4
  with:
    name: test-results
    path: |
      reports/
      logs/
    retention-days: 30
```

### Скачивание артефактов
```yaml
- uses: actions/download-artifact@v4
  with:
    name: test-results
    path: ./artifacts
```

## 🔀 Matrix Strategy

```yaml
jobs:
  test:
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest]
        python-version: ['3.9', '3.10', '3.11']
        exclude:
          - os: windows-latest
            python-version: '3.9'
        include:
          - os: ubuntu-latest
            python-version: '3.12'
            experimental: true
    
    runs-on: ${{ matrix.os }}
    
    steps:
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
```

## 🔗 Зависимости между Jobs

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building..."
  
  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: echo "Testing..."
  
  deploy:
    needs: [build, test]
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying..."
```

## ❓ Условное выполнение

```yaml
# Условие для job
jobs:
  deploy:
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps: [...]

# Условие для step
steps:
  - name: Deploy
    if: github.event_name == 'push'
    run: echo "Deploying..."

  - name: Only on success
    if: success()
    run: echo "Previous steps succeeded"
  
  - name: Only on failure
    if: failure()
    run: echo "Something failed"
  
  - name: Always run
    if: always()
    run: echo "Always runs"
```

## 🔐 Работа с Secrets

```yaml
steps:
  - name: Use secret
    run: |
      echo "Secret: ${{ secrets.MY_SECRET }}"
    env:
      API_KEY: ${{ secrets.API_KEY }}

  - name: Docker login
    uses: docker/login-action@v3
    with:
      username: ${{ secrets.DOCKERHUB_USERNAME }}
      password: ${{ secrets.DOCKERHUB_TOKEN }}
```

## 📦 Переменные окружения

```yaml
# Глобальные для workflow
env:
  APP_NAME: myapp
  VERSION: 1.0.0

jobs:
  build:
    # Для job
    env:
      BUILD_TYPE: release
    
    steps:
      # Для step
      - name: Build
        env:
          EXTRA_FLAGS: "--verbose"
        run: |
          echo "App: ${{ env.APP_NAME }}"
          echo "Version: $VERSION"
```

## 🎯 Контекстные переменные

```yaml
# GitHub контекст
${{ github.repository }}      # owner/repo
${{ github.ref }}             # refs/heads/main
${{ github.ref_name }}        # main
${{ github.sha }}             # commit SHA
${{ github.actor }}           # username
${{ github.event_name }}      # push, pull_request
${{ github.run_id }}          # уникальный ID запуска
${{ github.run_number }}      # порядковый номер

# Runner контекст
${{ runner.os }}              # Linux, Windows, macOS
${{ runner.name }}            # имя runner
${{ runner.temp }}            # временная директория

# Job контекст
${{ job.status }}             # success, failure, cancelled

# Steps контекст
${{ steps.step-id.outputs.result }}
```

## 🐳 Docker в GitHub Actions

```yaml
jobs:
  docker:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3
      
      - name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: user/app:latest
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

## 🧪 Тестирование

### Python + pytest
```yaml
- name: Install dependencies
  run: |
    pip install -r requirements.txt
    pip install pytest pytest-cov

- name: Run tests
  run: |
    pytest tests/ -v --cov=app --cov-report=xml

- name: Upload coverage
  uses: codecov/codecov-action@v4
  with:
    file: ./coverage.xml
```

### JavaScript + Jest
```yaml
- name: Install dependencies
  run: npm ci

- name: Run tests
  run: npm test -- --coverage

- name: Upload coverage
  uses: actions/upload-artifact@v4
  with:
    name: coverage
    path: coverage/
```

## 📊 Outputs между steps

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.get-version.outputs.version }}
    
    steps:
      - id: get-version
        run: |
          VERSION=$(cat version.txt)
          echo "version=$VERSION" >> $GITHUB_OUTPUT
  
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: |
          echo "Deploying version: ${{ needs.build.outputs.version }}"
```

## 🛠️ Полезные команды

```bash
# Проверка синтаксиса локально
act --list
act push

# Просмотр логов
gh run list
gh run view <run-id>

# Переменные в скриптах
echo "MY_VAR=value" >> $GITHUB_ENV
echo "MY_OUTPUT=value" >> $GITHUB_OUTPUT
```

## ⚡ Оптимизация

### Кэширование pip
```yaml
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
```

### Кэширование npm
```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
```

### Параллельный запуск тестов
```yaml
- name: Run tests
  run: pytest -n auto  # используем все CPU
```

### Отключение ненужных триггеров
```yaml
on:
  push:
    branches: [ main ]
    paths-ignore:
      - '**.md'
      - 'docs/**'
```

## 🎨 Badge в README

```markdown
![CI](https://github.com/username/repo/workflows/CI/badge.svg)

[![CI Status](https://github.com/username/repo/actions/workflows/ci.yml/badge.svg)](https://github.com/username/repo/actions/workflows/ci.yml)
```

## 🚨 Отладка

```yaml
# Вывод всех переменных
- name: Dump GitHub context
  env:
    GITHUB_CONTEXT: ${{ toJson(github) }}
  run: echo "$GITHUB_CONTEXT"

# Включить debug логи
# Settings → Secrets → Add: ACTIONS_STEP_DEBUG = true

# SSH доступ для отладки
- name: Setup tmate session
  uses: mxschmitt/action-tmate@v3
```

## 📚 Best Practices

✅ **DO:**
- Используйте конкретные версии actions (@v4, не @main)
- Кэшируйте зависимости
- Используйте secrets для чувствительных данных
- Давайте понятные имена jobs и steps
- Используйте matrix для параллелизации
- Настройте уведомления о падениях
- Ограничивайте permissions когда возможно

❌ **DON'T:**
- Не храните секреты в коде
- Не используйте нестабильные версии actions
- Не запускайте тяжелые задачи без необходимости
- Не дублируйте логику между workflows
- Не игнорируйте failed builds

## 🔗 Полезные ссылки

- [Документация](https://docs.github.com/actions)
- [Marketplace](https://github.com/marketplace?type=actions)
- [Awesome Actions](https://github.com/sdras/awesome-actions)
- [Workflow примеры](https://github.com/actions/starter-workflows)
