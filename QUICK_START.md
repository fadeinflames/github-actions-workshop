# 🚀 Быстрый старт - GitHub Actions Workshop

## 📦 Что в этом пакете?

Полный набор материалов для проведения воркшопа по GitHub Actions:

### Приложение:
- **app/** - Flask API калькулятора
- **tests/** - Unit и integration тесты
- **requirements.txt** - Python зависимости
- **Dockerfile** - контейнеризация

### GitHub Actions Workflows:
- **01-basic.yml** - базовый workflow для введения
- **02-testing.yml** - workflow с тестированием и кэшированием
- **03-matrix.yml** - матричное тестирование
- **04-production.yml** - production-ready pipeline
- **05-advanced.yml** - продвинутые возможности

### Документация:
- **README.md** - общее описание проекта
- **docs/WORKSHOP_SCENARIO.md** - подробный сценарий вебинара (90 мин)
- **docs/INSTRUCTOR_GUIDE.md** - инструкции для преподавателя
- **docs/CHEATSHEET.md** - шпаргалка для участников
- **docs/PRESENTATION.md** - слайды презентации

---

## ⚡ Быстрый запуск (5 минут)

### 1. Создайте репозиторий на GitHub

```bash
# Перейдите в директорию с материалами
cd github-actions-workshop

# Инициализируйте git
git init
git add .
git commit -m "Initial commit: GitHub Actions workshop materials"

# Создайте репозиторий на github.com и добавьте remote
git remote add origin https://github.com/ваш-username/github-actions-workshop.git
git push -u origin main
```

### 2. Проверьте что GitHub Actions запустились

1. Откройте ваш репозиторий на GitHub
2. Перейдите на вкладку **Actions**
3. Вы должны увидеть запущенные workflows
4. Дождитесь завершения (обычно 2-3 минуты)

### 3. Локальная проверка

```bash
# Установите зависимости
pip install -r requirements.txt

# Запустите тесты
pytest tests/ -v

# Все тесты должны пройти успешно ✅
```

---

## 📚 Подготовка к вебинару

### Для преподавателя:

1. **Прочитайте** `docs/INSTRUCTOR_GUIDE.md`
2. **Изучите** `docs/WORKSHOP_SCENARIO.md`
3. **Подготовьте** слайды из `docs/PRESENTATION.md`
4. **Проверьте** что все workflows работают в вашем репозитории

### Для участников:

**Отправьте им за неделю до вебинара:**

```
Требования для воркшопа:
1. Аккаунт на GitHub
2. Git установлен
3. Python 3.9+ установлен
4. Любой текстовый редактор

Подготовка:
1. Форкните репозиторий: https://github.com/ваш-username/github-actions-workshop
2. Клонируйте свой форк
3. Установите зависимости: pip install -r requirements.txt
4. Запустите тесты: pytest tests/ -v

Если все работает - вы готовы! 🎉
```

---

## 📖 Структура вебинара (90 минут)

| Время | Тема | Материалы |
|-------|------|-----------|
| 00:00-00:20 | Введение и основы | PRESENTATION.md (слайды 1-10) |
| 00:20-00:40 | Создание первого workflow | Live coding + 01-basic.yml |
| 00:40-00:55 | Оптимизация и кэширование | 02-testing.yml |
| 00:55-01:10 | Матрицы и параллелизация | 03-matrix.yml |
| 01:10-01:25 | Production pipeline | 04-production.yml |
| 01:25-01:30 | Практика и Q&A | Практическое задание |

**Детальный сценарий:** `docs/WORKSHOP_SCENARIO.md`

---

## 🎯 Что делать дальше?

### Перед вебинаром (за 1 день):
```bash
# Проверьте технику
□ Интернет-соединение стабильное
□ Демонстрация экрана работает
□ Микрофон настроен
□ Увеличен шрифт в IDE

# Подготовьте окружение для live coding
□ Откройте репозиторий на GitHub
□ Откройте вкладку Actions
□ Откройте IDE с кодом
□ Закройте все лишние приложения
```

### Во время вебинара:
1. Следуйте сценарию из `WORKSHOP_SCENARIO.md`
2. Пишите код вживую, объясняя каждую строку
3. После каждого изменения - коммитьте и показывайте результат в GitHub
4. Делайте паузы для вопросов каждые 10-15 минут

### После вебинара:
1. Выложите запись
2. Отправьте участникам ссылку на репозиторий
3. Соберите обратную связь
4. Ответьте на вопросы

---

## 💡 Полезные команды

```bash
# Запуск тестов
pytest tests/ -v

# Запуск с покрытием
pytest tests/ --cov=app --cov-report=html

# Проверка кода
flake8 app/ tests/

# Запуск приложения
python -m app.api

# Проверка health endpoint
curl http://localhost:5000/health

# Docker
docker build -t calculator-api .
docker run -p 5000:5000 calculator-api
```

---

## 📞 Поддержка

**Если что-то не работает:**

1. Проверьте версию Python: `python --version` (нужна 3.9+)
2. Проверьте что все зависимости установлены: `pip list`
3. Посмотрите логи GitHub Actions в вашем репозитории
4. Проверьте синтаксис YAML: https://www.yamllint.com/

**Частые проблемы:**
- Workflow не запускается → проверьте что файлы в `.github/workflows/`
- Тесты падают → убедитесь что установлены все зависимости
- Кэш не работает → проверьте ключ и путь в workflow

---

## 📚 Дополнительные ресурсы

- **Документация GitHub Actions:** https://docs.github.com/actions
- **Marketplace:** https://github.com/marketplace?type=actions
- **Awesome Actions:** https://github.com/sdras/awesome-actions
- **Примеры workflows:** https://github.com/actions/starter-workflows

---

## ✅ Чек-лист готовности к вебинару

### Технические требования:
- [ ] Репозиторий создан на GitHub
- [ ] Все workflows запускаются и проходят успешно
- [ ] Тесты работают локально
- [ ] Форк создан участниками (если применимо)

### Преподаватель:
- [ ] Прочитан INSTRUCTOR_GUIDE.md
- [ ] Изучен WORKSHOP_SCENARIO.md
- [ ] Подготовлены слайды
- [ ] Проверено оборудование
- [ ] Подготовлена среда для live coding

### Участники:
- [ ] Получили инструкции за неделю
- [ ] Установили требуемое ПО
- [ ] Форкнули и клонировали репозиторий
- [ ] Успешно запустили тесты локально

---

## 🎉 Готово!

Теперь у вас есть все необходимое для проведения отличного воркшопа по GitHub Actions!

**Вопросы?** Создайте issue в репозитории.

**Удачи на вебинаре! 🚀**
