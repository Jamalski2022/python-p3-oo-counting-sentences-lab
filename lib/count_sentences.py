#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            self._value = ""
        else:
            self._value = new_value

    def is_sentence(self):
        return self.value.strip().endswith('.')

    def is_question(self):
        return self.value.strip().endswith('?')

    def is_exclamation(self):
        return self.value.strip().endswith('!')

    def count_sentences(self):
        import re
        
        sentences = re.split('(?<=[.!?])\\s+', self.value.strip())
        
        return sum(1 for sentence in sentences if sentence.strip())
  # pass
