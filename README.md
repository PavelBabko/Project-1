# Project-1
Для выполнения задания была создана ветвь Base в репозитории [Project-1](https://github.com/PavelBabko/Project-1/tree/Base).

Сначала был создан файл [project_22_1.py](https://github.com/PavelBabko/Project-1/blob/Base/project_22_1.py).  В нем было произведено формирование БД в том виде, в котором они были записаны в файл  result.pickle(файл [base1.db](https://github.com/PavelBabko/Project-1/blob/Base/base1.db)). Однако полученная БД не соответствовала 3-ей нормальной форме, поэтому была сформирована другая структура. Новая структура состоит из 2 таблиц: Weeks и Films(файл [base2.db](https://github.com/PavelBabko/Project-1/blob/Base/base2.db)).

Далее был изменен файл [project_21.py](https://github.com/PavelBabko/Project-1/blob/Base/project_21.py). Внесены изменения так, чтобы извлеченная информация сразу записывалась в БД (файл [base rezult.db](https://github.com/PavelBabko/Project-1/blob/Base/base%20rezult.db)), чтобы уменьшить трудоемкость. Для подключения к БД и анализа информации был отредактирован  файл [project_22.py](https://github.com/PavelBabko/Project-1/blob/Base/project_22.py). 
 
![Image alt](https://github.com/PavelBabko/Project-1/blob/Base/Figure_1.png)

***Рис. 1 График зависимости суммарного дохода за выходные от времени***
 
![Image alt](https://github.com/PavelBabko/Project-1/blob/Base/Figure_1-1.png)

***Рис.2 График зависимости посещаемости за выходные от времени***

![Image alt](https://github.com/PavelBabko/Project-1/blob/Base/Figure_1-2.png) 

***Рис.3 График зависимости средней цены на билет в кино за выходные от времени***

![Image alt](https://github.com/PavelBabko/Project-1/blob/Base/Figure_1-3.png)

***Рис.4  График зависимости суммарного дохода за выходные.
Разделенный на компоненты: тренд, сезонная составляющая и остаток***

Загружены файлы([Weeks.SQL](https://github.com/PavelBabko/Project-1/blob/Base/Weeks.sql) и [Films.SQL](https://github.com/PavelBabko/Project-1/blob/Base/Films.sql)) с SQL-скриптом, по которому СУБД может сгенерировать таблицы, полученные при проектировании.
