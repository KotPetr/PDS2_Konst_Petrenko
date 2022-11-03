
class TextProcessor:

    def __init__(self):
        self.__punct = (',', '.', '!', ':', ';', '?', '-', '(', ')', '[', ']', '\"', '\\', '/', '*')


    def is_punktiantian(self, char : str):
        return char in self.__punct


    def get_clean_string(self, string):
        new_string = ''
        for char in string:
            if not self.is_punktiantian(char):
                new_string += char
        return new_string




class TextLoader:

    def __init__(self, text_processor : TextProcessor):
        self.__text_processor = text_processor
        self.__clean_string = ''

    @property
    def clean_string(self):
        print()
        print('This string is clean: ')
        return self.__clean_string


    def set_clean_text(self, string):
        self.__clean_string = self.__text_processor.get_clean_string(string)
        return


class DataInterface:

    def __init__(self, text_loader : TextLoader):
        self._text_loader = text_loader

    def process_texts(self, text):
        for row in text:
            self._text_loader.set_clean_text(row)
            print(self._text_loader.clean_string)


tp = TextProcessor()
print(tp.get_clean_string('Hel?lo, w:o]r/ld!'))

tl = TextLoader(tp)
tl.set_clean_text('Hel?lo, w:o]r/ld!')
print(tl.clean_string)

di = DataInterface(tl)
str_list = ['Hello!', '\Py_charm,', '?Hi-', 'Py.th:on']
di.process_texts(str_list)

