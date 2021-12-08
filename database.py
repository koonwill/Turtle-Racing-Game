import csv
from operator import itemgetter


class Database:

    def __init__(self):
        """Initialize(data)"""
        self.data = []
        with open('data.csv', 'r') as data_file:
            data = csv.DictReader(data_file)
            for each_data in data:
                each_data['win'] = int(each_data['win'])
                self.data.append(each_data)

    def update_data(self):
        """update data into file"""
        with open('data.csv', 'w') as file:
            write_file = csv.DictWriter(file, fieldnames=['name', 'win'])
            write_file.writeheader()
            for data in self.data:
                write_file.writerow(data)

    def save(self, name: str, win: int):
        """saving the progress of playing"""
        for data in self.data:
            if data['name'] == name:
                data['win'] = win
        self.update_data()

        print('Save.')

    def load(self, name: str):
        """loading the info of player but if not have it will create a new one"""
        with open('data.csv', 'r') as save_file:
            save = csv.DictReader(save_file)
            for data in save:
                if data['name'] == name:
                    data['win'] = int(data['win'])
                    return data

            else:
                print('No Save found')
                new_data = {'name': name, 'win': 0}
                self.data.append(new_data)
                return new_data

    def update_score(self, name: str, amount: int):
        "update the score"
        record_data = self.load(name)
        self.save(name, record_data['win'] + amount)

    def record(self):
        """"make a list of tuple then sorted list by descending of wincount """
        record_data = {data['name']: int(data['win']) for data in self.data}
        return sorted(record_data.items(), key=itemgetter(1), reverse=True)
