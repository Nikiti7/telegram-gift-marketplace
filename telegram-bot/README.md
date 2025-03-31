# Как правильно подключить виртуальное окружение?

1️⃣ Создать виртуальное окружение
В корне проекта:

```python -m venv venv```

Где venv — название папки с окружением.

2️⃣ Активировать окружение

📌 Wind:

```venv\Scripts\activate```

📌 Mac/Linux:

```source venv/bin/activate```

3️⃣ Установить зависимости

```pip install aiogram requests```

4️⃣ Сохранить зависимости

```pip freeze > requirements.txt```

Файл requirements.txt нужен, чтобы другие разработчики могли установить те же зависимости.

5️⃣ Добавить venv в .gitignore

Создай (или дополни) файл .gitignore в корне проекта:

```venv/```

✅ Это исключит виртуальное окружение из репозитория, но оставит requirements.txt.

6️⃣ Как установить зависимости на другом ПК?

После клонирования репозитория:

```
python -m venv venv
source venv/bin/activate  # (или venv\Scripts\activate для Windows)
pip install -r requirements.txt
```
