import models


if __name__ == '__main__':
    ticket_office = models.TicketOffice()
    for route in ticket_office.routes:
        print(route.stations)
        for train, time in route.trains.items():
            print(train.number, time)
            for carriage in train.carriages:
                print(carriage.get_free_seats_amount(), carriage.price)
                print(carriage.take_seat())
                print(carriage.take_seat())
                print(carriage.get_free_seats_amount(), carriage.price)