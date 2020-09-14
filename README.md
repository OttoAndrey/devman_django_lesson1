# Интересные места в мире
Devman. Django. Первый урок.

Сайт реализован в рамках курса Django на devman.org

## Фронт проекта
Проект представляет из себя карту мира. На которую можно наносить достопримечательности.
Фронт взят [отсюда](https://github.com/devmanorg/where-to-go-frontend)

![front](.gitbook/assets/project.PNG) 

## Кастом админка
Процесс добавления точки реализован через кастомизированную админку.

![admin_one](.gitbook/assets/admin1.PNG)

Изображения можно добавлять прямо на странице места.

![admin_two](.gitbook/assets/admin2.PNG) 

## Используемые библиотеки

* [WYSIWYG-редактор](https://github.com/aljosa/django-tinymce) - редактор текста

* [django-admin-sortable2](https://pypi.org/project/django-admin-sortable2/) - чтобы менять порядок изображений места с помощью drag-and-drop
