# 🚀 VK Hybrid Test Automation Framework

[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Pytest](https://img.shields.io/badge/pytest-7.0%2B-green.svg)](https://docs.pytest.org/)
[![Selenium](https://img.shields.io/badge/selenium-4.0%2B-brightgreen.svg)](https://www.selenium.dev/)
![CI](https://github.com/lolipusechka/vk-hybrid-test-framework/actions/workflows/ci.yml/badge.svg)

## 📖 О проекте

Этот репозиторий содержит **собственный гибридный фреймворк автоматизации тестирования**, разработанный для проверки веб-сервисов ВКонтакте. 

Ключевая идея проекта — демонстрация продвинутых навыков QA Automation / SDET через **связку UI и API тестирования** в рамках единого тестового сценария. Такой подход позволяет проверять синхронизацию состояния между бэкендом и фронтендом без необходимости каждый раз перезагружать страницу или выполнять рутинные действия через UI.

## 🏆 Ключевые особенности

- **Гибридная стратегия тестирования (UI + API)**  
  Тест создаёт сущности через API (например, пост на стене) и тут же проверяет их отображение в UI. Это демонстрирует понимание архитектуры современных веб-приложений и значительно ускоряет выполнение тестов.

- **Собственная обёртка над Selenium**  
  Вместо использования «голого» Selenium реализован слой абстракции (`BaseElement`, `Button`, `Label`, `TextBox`, `Alert`), который инкапсулирует явные ожидания (explicit waits), логирование и обработку исключений.

- **Архитектура Page Object Model (POM)**  
  Строгое разделение локаторов UI-элементов и тестовой логики, что обеспечивает высокую поддерживаемость и масштабируемость фреймворка.

- **Модели данных и внешняя конфигурация**  
  Все настройки браузера, API-эндпоинты и тестовые данные вынесены в JSON-файлы. Взаимодействие с API инкапсулировано в модели (`Post`, `Comment`, `Photo`, `Like`, `User`).

- **Детальное логирование**  
  Интеграция с `pytest` и собственный логгер с форматированием времени, уровней и шагов теста.

## 🛠 Технологический стек

| Категория         | Технологии                            |
|-------------------|---------------------------------------|
| Язык              | Python 3                              |
| UI-автоматизация  | Selenium WebDriver, Chrome            |
| API-автоматизация | Requests                              |
| Тест-раннер       | Pytest                                |
| Архитектура       | POM, Factory, Custom Waits            |
| Конфигурация      | JSON                                  |

## 🧪 Основной сценарий теста

Главный тест реализует полный жизненный цикл работы с постом, переключаясь между API и UI:

| Шаг | Уровень | Действие |
|-----|---------|----------|
| 1   | **UI**  | Авторизация и переход на страницу профиля |
| 2   | **API** | Создание поста со случайным текстом через VK API |
| 3   | **UI**  | Проверка появления поста на стене **без перезагрузки страницы** |
| 4   | **API** | Редактирование поста: изменение текста и загрузка изображения |
| 5   | **UI**  | Верификация обновлённого текста и картинки в UI |
| 6   | **API** | Добавление комментария к посту через API |
| 7   | **UI**  | Проверка, что комментарий появился в UI |
| 8   | **UI**  | Постановка лайка посту через интерфейс |
| 9   | **API** | Проверка наличия лайка от нужного пользователя через `wall.getLikes` |
| 10  | **API** | Удаление поста через API |
| 11  | **UI**  | Финальная проверка исчезновения поста со стены |

## ⚙️ Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/lolipusechka/vk-hybrid-test-framework.git
cd vk-hybrid-test-framework
```

### 2. Установка зависимостей
```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 3. Настройка конфигурации
Создайте собственные конфиги на основе примеров:
```bash
cp config/api_config.example.json config/api_config.json
cp config/test_config.example.json config/test_config.json
```

Заполните файлы своими данными:
- `access_token` — токен VK API
- `owner_id`, `user_id` — идентификаторы пользователя
- `login`, `password` — данные для авторизации в UI

> ⚠️ **Важно:** никогда не коммитьте реальные токены и пароли в публичный репозиторий.

### 4. Запуск тестов
```bash
pytest
```

Запуск с подробным выводом в консоль:
```bash
pytest -v -s
```

Запуск в headless-режиме (без окна браузера) настраивается в `config/general.json`:
```json
{
  "headless": 1
}
```

## 📂 Структура проекта

```text
vk-hybrid-test-framework/
├── src/
│   ├── core/           # Базовые классы (BaseElement, Browser, Driver, Waits)
│   ├── pages/          # Page Objects (LoginPage, FeedPage, MyProfilePage)
│   ├── api/            # API-клиенты и модели данных (Post, Comment)
│   └── utils/          # Хелперы (JSON-parser, random utils, logger)
├── tests/              # Pytest-тесты
├── resources/          # Тестовые данные (изображения и т.д.)
├── config/             # Примеры конфигураций (.example.json)
├── .github/workflows/  # GitHub Actions CI/CD
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## 📌 Заметки

- Логирование пишется в файл `log/pytest.log` (директория создаётся автоматически).
- Для стабильной работы рекомендуется использовать **Chrome последней версии** и соответствующий **ChromeDriver**.

## 👤 Автор

**lolipusechka**  
QA Automation Engineer / SDET  
📫 GitHub: [@lolipusechka](https://github.com/lolipusechka)