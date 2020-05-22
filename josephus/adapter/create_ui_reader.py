from josephus.adapter import file_reader as rd

class CreateUiReader():
    def __init__(self, path):
        self.path = path
        self.reader = None

    def create_ui_reader(self):
        file_ = self.path.split(".")
        if file_[1] == "txt":
            self.reader = rd.TxtReader(self.path)
        elif file_[1] == "CSV":
            self.reader = rd.TxtReader(self.path)
        else:
            raise("路径错误")
        return self.reader.read_data()
            