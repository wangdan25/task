from josephus.adapter.josephus_txt_interface import TxtInterface

if __name__ == '__main__':
    interface = TxtInterface()
    reader = interface.create_reader()
    interface.show_original_data(reader)
    interface.show_result(reader)