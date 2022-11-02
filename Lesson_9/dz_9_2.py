
class TextProcessor:

    def __init__(self):
        self.__is_punct = False


    def is_punktiantian(self, char : str):
        punct = (',', '.', '!', ':', ';', '?', '-', '(', ')', '[', ']', '\"', '\\', '/')
        self.__is_punct = True if char in punct else False


#    @classmethod
    def get_clean_string(self, string):
        new_string = ''
        for char in string:
            self.is_punktiantian(char)
            if not self.__is_punct:
                new_string += char
        return new_string


class TextLoader:

    def __init__(self):
        self.__text_processor = tp
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

    def __init__(self):
        self._text_loader = tl

    def process_texts(self, text):
        for row in text:
            self._text_loader.set_clean_text(row)
            print(self._text_loader.clean_string)


tp = TextProcessor()
print(tp.get_clean_string('Hel?lo, w:o]r/ld!'))

tl = TextLoader()
tl.set_clean_text('Hel?lo, w:o]r/ld!')
print(tl.clean_string)

dt = DataInterface()
text = ['Hello!', '\Py_charm,', '?Hi-', 'Py.th:on']
dt.process_texts(text)

