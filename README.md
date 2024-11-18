# TrainTickets
## Легенда
Кассиру в ЖД кассе нужна программа, которая бы помогала бы продавать путешественникам билеты на поезд. 
Кассир вводит в программу начальную и конечную точку маршрута и получает в сообщение о возможных поездах.

## Краткая информация
В рамках данного задания практикума вам предстоит реализовать эмулятор кассы по продаже ЖД-билетов в город Маёвск. Данный эмулятор будет работать в терминале и не потребует реализации графического интерфейса. Цель данного практикума — отработать использование принципов ООП.
## Сроки сдачи
Сдать задание необходимо в срок до 16 января 2025 (включительно). Задание считается сданным, если его программный код залит в Gitlab и преподавателю выдан доступ к проекту для его проверки.
## Требования к программе
### Визуальное оформление
В рамках данного задания просьба не тратить время на реализацию графического интерфейса. Когда-то давно, когда не было видеокарт и привычных нам графических интерфейсов, программисты использовали прием, называемый в наше время псевдографикой. Т.е. все, что мы видим на экране, — это символы, напечатанные при помощи функции print(). Если вам сильно хочется “красивости”, просьба воспользоваться именно этим приемам, не прибегая к использованию графических библиотек. Всему свое время.
### Запуск программы
Файл с программой назовите ticket_office.py.
Запускаться программа должна следующим образом: python ticket_office.py.
### Цикл работы программы
После запуска программа должна поприветствовать пользователя и кратко объяснить алгоритм взаимодействия, который необходимо выполнить для покупки билета.
Далее программа должна вывести список доступных маршрутов. Каждая строка должна содержать номер поезда, время отправления, общее количество свободных мест и минимальную стоимость билета. Список должен быть отсортирован по времени отправления.
        №        ОТПРАВЛЕНИЕ    СВОБОДНО МЕСТ    ЦЕНА ОТ 
        3452     13:20          12/40            2000 руб.
        1212     17:15          26/66            500 руб.
Пользователь выбирает номер маршрута и вводит его с клавиатуры.
Программа должна вывести детальную информацию об этом маршруте, а именно:
Продублировать номер маршрута и время отправления
Детальный прайс

    НОМЕР: 1212
    ОТПРАВЛЕНИЕ: 17:15
    БИЛЕТЫ:
    1 - СИДЯЧЕЕ (10/20): 500 руб.
    2 - ПЛАЦКАРТ (13/18): 1000 руб.
    3 - КУПЕ (1/24): 2000 руб.
    4 - СВ (2/4): 5000 руб.


Пользователь вводит с клавиатуры номер, соответствующий типу билета, который он желает приобрести.
Далее программа спрашивает учетные данные пассажира (ФИО, номер телефона), которые пользователь вводит с клавиатуры
В ответ на это программа выдает ему информацию о приобретенном билете. При этом этиже данные необходимо записать в отдельный файл, имя которого соответствует номеру проданного билета. 

    ПАССАЖИР: Петров Иван Андреевич, 8 495 234 23 43
    №      МАРШРУТ    ОТПРАВЛЕНИЕ    ВАГОН    МЕСТО    ЦЕНА
    256    1212       17:15          6        27       2000 руб.


Затем программа должна снова вывести информацию обо всех доступных маршрутах и подготовиться к обслуживанию следующего клиента. Учтите, что только что купленное место должно уменьшить количество доступных на данном маршруте.
### Структура программы
В программе должны быть реализованы следующие классы (их названия должны быть именно такими):
TicketOffice — основной класс программы, отвечающий за взаимодействие с пользователем.
Route — класс, содержащий два параметра: поезд, который пойдет по маршруту и время отправления.
Train — класс, содержащий информацию о поезде. Содержит свойство со списком вагонов.
Carriage — класс для хранения информации о вагоне. Этот класс абстрактный, от него следует наследовать вагоны конкретных типов. Содержит одно свойство — список мест. Также содержит переменную класса с ценой места. Для абстрактного вагона ее значение должно быть None.
SeatCarriage — класс сидячего вагона. Цена места в данном вагоне 500 руб. Он содержит 60 мест.
EconomCarriage — плацкартный вагон. 1000 руб. 30 мест.
CoupeCarriage — купе. 2000 руб. 20 мест.
FirstClassCarriage — вагон СВ. 5000 руб. 10 мест.
Seat — класс места. Содержит один параметр — занятость (True/False).

### Данные
Все иходные данные для работы вышей программы считаюиться из файлов и при необходимости могу быть дополнены сгенерироваными случайным образом путем дополнения файлов с исходными данными (при этом они должны выглядеть правдоподобно). К примеру, в поезде не должно быть 200 вагонов.
Постарайтесь подобрать числа таким образом, чтобы отображаемая информация выглядела аккуратно, не вылезала за границы строк.
Места и вагоны нумеруйте с единицы, а не с нуля. Номера маршрутов и билетов сделайте многозначными.
В каждом поезде должны быть вагоны разных типов (не обязательно всех). Учтите, что это важно при подсчете цены билета в графе “ЦЕНА ОТ”. Также учтите, что места могут заканчиваться, тогда “ЦЕНА ОТ” для данного маршрута изменится.
### Описание файлов с исходными данными

Файл Stations.conf содержит сведенья о возможных местах остановки поездов и имеет следующий вид

    0 Тамбов
    1 Самара
    ...
    22 Москва Курская
    ...
    24 Санкт-Питербург Московский
    ...
где первая цифра код станции, а вторая ее называние.

Route.ini - содержит информацию о доступных маршрутах и поездах на этих маршрутах.

    [Route]
    0 = 22-24
    1 = 24-22
    ...
    [Train]
    1014 = 0
    2044 = 1
    ...
    [Shedule]
    1014 = Mon 10:00; Wen 21:00
    2044 = Mon 10:00; Wen 21:00
    ...

где в секции Route значение до равно определяет номер маршрута, а последовательность после равно номера станций в порядке следования; в секции Train значение до равно определяет номер поезда, а после равно маршрут следования; в секции Shedule - значение справа определяет номер поезда, а значение слева от равно оперделяют день недели и время отправления. Время в часах, которое поезд проводит в пути между станциями определяется как разность их номеров. 
     
Таким образом, интерпретировать содержимое файлов нужно следующим образом:
Поезд с номером 1014 следует по маршруту Москва Курская - Санкт-Петербург (22-24) и отправляется в понедельник в 10 утра из Москвы и прибывает в Санкт-Петербург в 12 часов дня или в среду в 9 вечера и прибывает в Санкт-Петербург в 11 вечера.

Файлы Train<num>.ini определяют характеристики поезда: количество вагонов разного типа (секция CountCarriages), количество мест в одном вагоне указанного типа (секция CountSeatCarriages), стоимость полного (от начальной до конечной станции следования) проезда (секция PriceCarriages). <num> в названии файла определяет номер поезда.
    [CountCarriages]
    SeatCarriage = 2
    EconomCarriage = 3
    CoupeCarriage = 4
    FirstClassCarriage = 5

    [CountSeatCarriages]
    SeatCarriage = 80
    EconomCarriage = 54
    CoupeCarriage = 36
    FirstClassCarriage = 18

    [PriceCarriages]
    SeatCarriage = 200
    EconomCarriage = 3000
    CoupeCarriage = 4000
    FirstClassCarriage = 50000
Таким образом, интерпретировать содержимое файлов нужно следующим образом:
В поезед с номером 1014 (файл Train1014.ini): 2 вагона с сидямичи местами, в каждом по 80 мест, стоимость проезда в которых от Москва Курская до  Санкт-Петербург составляет 200 рублей; 3 плацкартных вагона, по 54 места в каждом, стоимость проезда от Москва Курская до Санкт-Петербург составляет 3000 рублей;  4 вагона-купе, по 36 мест в каждом, стоимость проезда от Москва Курская до Санкт-Петербург составляет 4000 рублей; 5 вагонов СВ, по 18 мест в каждом, стоимость проезда от Москва Курская до Санкт-Петербург составляет 50000 рублей.
### Технические условия
Все действия пользователя необходимо логировать в отдельный файл. При этом лог-файл создаетс при каждом запуске программы новый и не затирает лог-файлы с предыдущих запусков. Для выполнения этого условия можно реализовать функцию декоратор для логирования.
Информацию о всех проданных за смену (за один запуск программы) билетах нужно записывать в отдельный файлы-билетов.
Можно использовать вспомагательные модули для работы с конфигурационными файлами например configparser.
    
## Задание на дополнительную оценку 5
Разработать еще одну программу, которая на основании данных, которые вводит пользователь с клавиатуры дополняет конфигурациионные файлы новыми маршрутами, поездами, типа вагонов, расписанием и прочей исходной информацией для работы кассы.

