class Material:

 def __init__(self, information_text, attr1):
            self.information_text = information_text
            self.attr1 = attr1

def information_material(self):
    print(self.information_text)


class Material1(Material):

        def __init__(self, information_text, attr1):
            super().__init__(information_text, attr1)


class Material2(Material):

            def __init__(self, information_text, attr1):
                super().__init__(information_text, attr1)


class Material3(Material):

            def __init__(self, information_text, attr1):
                super().__init__(information_text, attr1)


class Material4(Material):

    def __init__(self, information_text, attr1):
        super().__init__(information_text, attr1)


class Material5(Material):

    def __init__(self, information_text, attr1):
        super().__init__(information_text, attr1)


"""Subjects"""


class Subject1(Material1):
    def __init__(self, information_text, attr1, subject_info_text):
        super().__init__(information_text, attr1)
        self.subject_info_text = subject_info_text

        def information(self):
            print(self.subject_info_text)


class Subject2(Material2):
    def __init__(self, information_text, attr1, subject_info_text):
        super().__init__(information_text, attr1)
        self.subject_info_text = subject_info_text

    def information(self):
        print(self.subject_info_text)


class Subject3(Material3):
    def __init__(self, information_text, attr1, subject_info_text):
        super().__init__(information_text, attr1)
        self.subject_info_text = subject_info_text

    def information(self):
        print(self.subject_info_text)


class Subject4(Material5):
    def __init__(self, information_text, attr1, subject_info_text):
        super().__init__(information_text, attr1)
        self.subject_info_text = subject_info_text

    def information(self):
             print(self.subject_info_text)


class Subject5(Material5):

    def __init__(self, information_text, attr1, subject_info_text):
        super().__init__(information_text, attr1)
        self.subject_info_text = subject_info_text

    def information(self):
        print(self.subject_info_text)


material1 = Material1('its material 1', 1212)
subject1 = Subject1('its awpdoajdw', 1290, 'awdoiawdnaoiwdnnoiawd')

material1.information_material()
subject1.information()