# the2nd_l07_06_practice.py
"""
Дан список словарей фильмов  movies. Каждый словарь в списке содержит два ключа: «name» и «movies».
Используя tuple comprehension необходимо:
1) Получить кортеж actors с именами актеров и количестве фильмов. Формат: ((A, M), (A, M), (A, M)), где A - актер, M - количество фильмов


"""
angelina_jolie = ["В поисках выхода", "Киборг 2: Стеклянная тень", "Хакеры",  "Без улик", "Луна пустыни", "Итальянские любовники", "Ложный огонь", "Изображая Бога", "Настоящие женщины", "Адский котёл", "Превратности любви", "Управляя полётами", "Власть страха", "Прерванная жизнь", "Угнать за 60 секунд", "Лара Крофт: Расхитительница гробниц", "Соблазн", "Жизнь или что-то вроде того", "Лара Крофт: Расхитительница гробниц. Колыбель жизни", "За гранью", "Лихорадка", "Забирая жизни", "Небесный капитан и мир будущего", "Александр", "Мистер и миссис Смит", "Ложное искушение", "Беовульф", "Её сердце", "Особо опасен", "Подмена", "Солт", "Турист", "Малефисента", "Лазурный берег", "Малефисента 2"]


brad_pitt = ["Нет выхода", "Нейтральная полоса", "Меньше, чем ноль", "Тёмная сторона Солнца", "Счастливы вместе", "Пропуск занятий", "Гонки по кругу", "Джонни Замша", "Тельма и Луиза", "Контакт", "Параллельный мир", "Там, где течёт река", "Калифорния", "Настоящая любовь", "Услуга", "Интервью с вампиром: Хроника жизни вампира", "Легенды осени", "Семь", "12 обезьян", "Спящие", "Собственность дьявола", "Семь лет в Тибете", "Знакомьтесь, Джо Блэк", "Бойцовский клуб", "Большой куш", "Мексиканец", "Шпионские игры", "Одиннадцать друзей Оушена", "Признания опасного человека", "Троя", "Двенадцать друзей Оушена", "Мистер и миссис Смит", "Вавилон", "Тринадцать друзей Оушена", "Как трусливый Роберт Форд убил Джесси Джеймса", "После прочтения сжечь", "Загадочная история Бенджамина Баттона", "Бесславные ублюдки", "Древо жизни", "Человек, который изменил всё", "Ограбление казино", "Война миров Z", "12 лет рабства", "Советник", "Ярость", "Лазурный берег", "Игра на понижение", "Союзники", "Машина войны", "Дэдпул 2", "К звёздам", "Однажды в Голливуде"]


george_clooney = ["Возвращение в школу ужасов", "Возвращение помидоров-убийц", "Красный прибой", "Сансет Бит", "Урожай", "От заката до рассвета", "Один прекрасный день", "Бэтмен и Робин", "Миротворец", "Вне поля зрения", "Тонкая красная линия", "Три короля", "Взрыв", "О, где же ты, брат?", "Идеальный шторм", "Дети шпионов", "Одиннадцать друзей Оушена", "Добро пожаловать в Коллинвуд", "Солярис", "Признания опасного человека", "Дети шпионов 3: Игра окончена", "Невыносимая жестокость", "Двенадцать друзей Оушена", "Доброй ночи и удачи", "Сириана", "Хороший немец", "Тринадцать друзей Оушена", "Майкл Клейтон", "Любовь вне правил", "После прочтения сжечь", "Безумный спецназ", "Мне бы в небо", "Американец", "Потомки", "Мартовские иды", "Гравитация", "Охотники за сокровищами", "Земля будущего", "Аве, Цезарь!", "Финансовый монстр"]

movies = [
        {'name':'Angelina Jolie', 'movies': angelina_jolie},
        {'name':'Brad Pitt', 'movies': brad_pitt},
        {'name':'George Clooney', 'movies': george_clooney}
        ]

actors = tuple((i['name'],len(i['movies']))for i in movies)

print("Задание 1:", actors)
