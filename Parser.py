import SeleniumScripts

# тут можно захардкодить интерфейс, но это без меня
class Avito(object):

    def __init__(self, uri=None, vacancy=None):
        self.uri = uri
        self.vacancy = vacancy
        self.__start()

    def __start(self):
        expended = False
        if self.uri is None:
            print("Вы можете ввести полный URL-адрес страницы или настроить поиск в процессе.")
            self.uri = input("Введите URL для осуществления быстрого поиска по Avito; или введите город, просмотр вакансий по которому осуществит программа: ")
            if "https" not in self.uri:
                expended = True
                self.town = self.uri
                self.schedule = input("Выберите график работы:\n1. Полный день\n2. Неполный день\n3. Свободный\n4. Сменный\n5. Вахтовый\n 5/2\n 6/1 [Вы можете ввести последовательность цифр, чтобы выбрать несколько вариантов.]")
                self.salary = input("Заработная плата в формате от до [10000-20000]:")
                self.payout_frequency = input("Частота выплат:\n1. Частота выплат\n2. Каждый день\n3. Дважды в месяц\n4. Раз в неделю\n5. Три раза в месяц\n6. Раз в месяц")
                self.uri = self.town + "?" + self.schedule + "?" + self.salary + "?" + self.payout_frequency
                vacancy = input("Общее количество вакансий по умолчанию 2000, введите сюда необходимое для вас количество вариантов или нажмите enter.")
                self.vacancy = 2000 if vacancy == "" else vacancy
        with SeleniumScripts.Driver() as driver:
            while self.uri != "END":
                self.uri = driver.parsing(self.uri, expended, self.vacancy)
