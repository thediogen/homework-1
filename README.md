# Django Homework #1

## Різниця Між:

* python manage.py makemigrations
* python manage.py migrate
* python manage.py migrate Market

`makemigrations` - просто створює файл з міграцією, де записані всі зміни в моделях. 
аналог в alembic - `alembic revision --autogenerate -m ""`.

`migrate` - підтягує всі міграції, робить апдейт бази даних, але: він бере ВСІ міграції з усіх наших додатків. 
аналог в alembic: `alembic upgrade head`.

`migrate Market` - також підтягує всі міграції (робить те ж саме, що й попередня команда), але бере міграції 
тільки з додатку Market.


<p style="color: #ed7455;">не впевнений що я правильно зрозумів різницю між останніми двома.</p>
