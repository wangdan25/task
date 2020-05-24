from josephus.adapter import file_reader as rd

def read_data(path):
    file_ = path.split(".")
    if file_[1] == "txt":
        reader = rd.TxtReader(path)
    elif file_[1] == "csv":
        reader = rd.CsvReader(path)
    else:
        raise FileNotFoundError
    return reader.read_data()
            