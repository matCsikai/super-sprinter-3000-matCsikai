import csv

def data_import():
    
    with open("data.csv") as csv_file:
        imported_data = csv.reader(csv_file)
        database_as_list = [row for row in imported_data]
    #print(database_as_list)
    return database_as_list


def data_list_with_id():
    id_values = []
    database_as_list = data_import()
    for numbers in range(len(database_as_list)):
        id_values.append(numbers + 1)
    #print(id_values)
    index = 0
    for data_row in database_as_list:
        data_row.insert(0, id_values[index])
        index += 1
    #print(database_as_list)
    return database_as_list


data_list_with_id()