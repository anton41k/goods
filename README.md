Написать Web-приложение на Django со следующей функциональностью:

1) Приложение должно уметь динамически создавать классы моделей в памяти, используя текстовое описание моделей (например, из xml (или yaml) файла), должны поддерживаться типы char, int, date.
2) Таблицы в бд надо создать стандартными средствами django (syncdb), для изменения необходимо использовать south (в консоли, если модели правильно созданы, то syncdb и south их подхватывают);
3) Для этих таблиц должно быть доступно редактирование в админке django;
4) Главная страница приложения, для просмотра и редактирования введенных.
данных. пример - http://habrastorage.org/storage2/b00/1c7/cfb/b001c7cfbd1cb0b38ad5633d5a781612.png. При щелчке на ячейку данных, поле должно заменяться полем редактирования в зависимости от типа данных (для типа “дата” должен показываться виджет выбора даты), и после ввода и валидации отправляться на сервер. Должна быть возможность добавления новой строки. Язык - JavaScript.
5) Надо написать тесты для создаваемых моделей и запросов.

Слева - список таблиц, справа - данные. При выборе таблицы, в правый блок аяксом загружаются структура и  данные таблицы. Главное требование - никаких html блоков при получении этих данных.
