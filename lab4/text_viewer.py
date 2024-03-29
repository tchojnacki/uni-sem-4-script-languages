import subprocess
from inspect import cleandoc
from re import findall
from file_viewer import FileViewer
from text_buffer import TextBuffer


class TextStats:
    '''
    Calculates statistics regarding the text buffer read from file.
    '''

    def __init__(self):
        super().__init__()
        self.number_of_lines = 0
        self.number_of_words = 0
        self.number_of_nonalpha = 0

    def compute(self, text: str):
        self.number_of_lines = len(text.splitlines())
        self.number_of_words = len(text.split())
        self.number_of_nonalpha = len(findall(r'[^\w]', text))

    def __repr__(self):
        return cleandoc(f'''
        number_of_lines: {self.number_of_lines}
        number_of_words: {self.number_of_words}
        number_of_nonalpha: {self.number_of_nonalpha}
        ''')


class TextViewer(TextBuffer, FileViewer):
    def __init__(self, path: str):
        self._stats = TextStats()
        super().__init__(path)

    def view(self):
        subprocess.run(['notepad.exe', self.path], check=True)

    def get_data(self):
        return self._stats

    def read_from_file(self, path: str):
        super().read_from_file(path)
        self._stats.compute(self.text)
