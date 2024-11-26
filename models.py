import config_parse

class TicketOffice:
    def __init__(self):
        self.routes = [Route(route_num) for route_num in config_parse.get_routes()]
    
        

class Route:
    def __init__(self, route_num):
        info = config_parse.get_route_info_by_number(route_num)
        self.stations = info['stations']
        self.trains = dict(map(lambda x: (Train(int(x[0])), x[1]), info['trains'].items())) 


class Train:
    def __init__(self, number):
        self.number = number
        self.carriages = []
        info = config_parse.get_train_carriages_info_by_number(number)

        for carriage_type, carriage_count in info['CountCarriages'].items():
            for _ in range(int(carriage_count)):

                seats_count = int(info['CountSeatCarriages'][carriage_type])
                price = int(info['PriceCarriages'][carriage_type])

                match carriage_type:
                    case 'seatcarriage':
                        new_carriage = SeatCarriage(seats_count, price)
                    case 'economcarriage':
                        new_carriage = EconomCarriage(seats_count, price)
                    case 'coupecarriage':
                        new_carriage = CoupeCarriage(seats_count, price)
                    case 'firstclasscarriage':
                        new_carriage = FirstClassCarriage(seats_count, price)
                
                self.carriages += [new_carriage]








class Carriage:
    def __init__(self, seats_amount=0, price=None):
        self.seats = {i: Seat() for i in range(1, seats_amount + 1)}
        self.price = price 
    
    def get_seats_amount(self):
        return len(self.seats)
    
    def get_free_seats_amount(self):
        coun = 0
        for elem in self.seats.values():
            if not elem.is_taken:
                coun += 1
        return coun
    
    def take_seat(self):
        for key, value in self.seats.items():
            if not value.is_taken:
                value.take_seat()
                return key
        return None


class SeatCarriage(Carriage):
    def __init__(self, seats_amount=80, price=500):
        super().__init__(seats_amount=seats_amount, price=price)
        


class EconomCarriage(Carriage):
    def __init__(self, seats_amount=30, price=1000):
        super().__init__(seats_amount=seats_amount, price=price)
        

class CoupeCarriage(Carriage):
    def __init__(self, seats_amount=20, price=2000):
        super().__init__(seats_amount=seats_amount, price=price)
        

class FirstClassCarriage(Carriage):
    def __init__(self, seats_amount=10, price=5000):
        super().__init__(seats_amount=seats_amount, price=price)
        




class Seat:
    def __init__(self):
        self.is_taken = False
    

    def take_seat(self):
        self.is_taken = True

