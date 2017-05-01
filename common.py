import csv


# reads data from data.csv
def data_import():
    with open("data.csv") as csv_file:
        imported_data = csv.reader(csv_file)
        database_as_list = [row for row in imported_data]
    return database_as_list


# adds ID to data rows
def data_list_with_id():
    id_values = []
    database_as_list = data_import()
    for numbers in range(len(database_as_list)):
        id_values.append(numbers + 1)
    index = 0
    for data_row in database_as_list:
        data_row.insert(0, id_values[index])
        index += 1
    return database_as_list


# deletes data row by ID (defunct)
def delete_row(story_id):
    database_as_list = data_import()
    database_as_list.remove(database_as_list[story_id - 1])
    return database_as_list






