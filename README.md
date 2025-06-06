# Telegram Gift Market — Mini App

Telegram Mini-приложение для покупки и продажи подарков прямо внутри Telegram.  
Работает через WebApp + Telegram Bot + Backend (Node.js + MySQL).

## Стек технологий

- **Frontend**: React(Telegram WebApp)
- **Backend**: Node.js(Express)
- **Database**: MySQL
- **Telegram Bot**: Python (aiogram / pyTelegramBotAPI)

## Установка и запуск

 ```
docker-compose up --build

# Перезапусти проект
docker-compose down
docker-compose up -d --build
 ```

1. Клонируй репозиторий:

```
git clone https://github.com/yourname/telegram-gift-market.git
cd telegram-gift-marketplace
```

## Структура проекта
```
telegram-gift-marketplace/
│
├── backend/               # Node.js backend (Express + PostgreSQL)
│   ├── controllers/       # Обработка запросов (API-логика)
│   ├── routes/            # Эндпоинты API
│   ├── models/            # Модели и работа с БД
│   ├── migrations/        # SQL-миграции для создания таблиц
│   ├── seed/              # Тестовые данные (наполнение БД)
│   └── .env               # Переменные окружения

├── bot/                   # Telegram-бот (Python или Node.js)
│   ├── nft.py            # Точка входа
│   └── .env               # BOT_TOKEN и настройки

├── webapp/                # Веб-интерфейс (React/Vite)
│   ├── src/               # Компоненты и Telegram WebApp SDK
│   ├── public/
│   └── .env               # API_URL и настройки WebApp

├── CHANGELOG.md           # Документирование изменений в проекте
├── README.md              # Документация проекта
├── docker-compose.yml     # Настройки Docker для сервера
└── .gitignore             # Исключения Git
```


## Лицензия
MIT

## Авторы
Команда Flux
