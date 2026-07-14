#!/bin/bash

# Проверка наличия аргумента
if [ -z "$1" ]; then
    echo "Ошибка: Передайте строку X в качестве аргумента."
    exit 1
fi

# Выполнение команд
git add .
git commit -m "Add $1"
git push

