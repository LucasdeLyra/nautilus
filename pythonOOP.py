class AUV:
    def __init__(
            self,
            num_thursters,
            sensors_list,
            build_year,
            vehicle,
            dimensions,
            total_budget):

        self.num_thursters = num_thursters
        self.sensors_list = sensors_list
        self.build_year = build_year
        self.vehicle = vehicle
        self.dimensions = dimensions
        self.total_budget = total_budget


class Nautilus:
    def __init__(self):
        self.lAUV = []

    def add_auv(self, AUV):
        self.lAUV.append(AUV)

    def show(self, AUV_name):
        for AUV in self.lAUV:
            if AUV.__dict__["vehicle"] == AUV_name:
                return print(AUV.__dict__)
        return print('not found')

    def show_all(self, lAUV=None):
        if lAUV is None:
            lAUV = self.lAUV
        for AUV in lAUV:
            print(f'{AUV.__dict__}')

    def __bubble_sort(self, param):
        lordened = self.lAUV.copy()
        exchange = True
        while exchange:
            exchange = False
            for i in range(len(lordened) - 1):
                if lordened[i].__dict__[
                        param] > lordened[i + 1].__dict__[param]:
                    aux = lordened[i]
                    lordened[i] = lordened[i + 1]
                    lordened[i + 1] = aux
                    exchange = True
        return lordened

    def rank_age(self):
        return self.show_all(self.__bubble_sort('build_year'))

    def rank_budget(self):
        return self.show_all(self.__bubble_sort('total_budget'))


# testando tudo
"""
a = AUV(2, [2,3,4], 2021, 'a', [2,3,4], 2387823)
b = AUV(3, [55,3,2], 2020, 'b', [5,6,7], 43897924)

nautilus = Nautilus()
nautilus.add_auv(a)
nautilus.add_auv(b)
nautilus.show_all()
nautilus.show('c')
nautilus.rank_age()
nautilus.rank_budget()"""
