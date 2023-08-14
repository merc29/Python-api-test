import requests


class api_of_joke() :
    def __int__(self):
        pass
    '''Собираем массив категорий'''
    def getting_categories(self):
        categories = requests.get("https://api.chucknorris.io/jokes/categories")
        print(categories.text)
        assert categories.status_code == 200
        if categories.status_code == 200:
            print("Собрали массив")
        else:
            print('не получилось по причине ниже')
            print(categories.status_code)

        '''Загоняем полученный json в массив'''
        massive = categories.json()
        return massive


    '''Основной тест проверки наличия шуток'''
    def test_joke_of_chuck(__itter__,massive):

        '''Берем элемент массива и используем как часть урла'''
        for f in massive:
            print(f)
            url = "https://api.chucknorris.io/jokes/random?category=" + f
            result = requests.get(url)
            res = result.json()

            '''Цикл на проверку'''
            if result.status_code == 200 :
                print("YEP") #Если все нормально- печатай шутку
                print(res['value'])
                legend = "Chuck"
                assert legend in res['value'] # проверим, что имя легенды участвует
            else:
                print('NOPE') #Если все НЕ нормально- печатай статус
                print("что-то пошло не так... статус " + str(result.status_code))

first_api_test = api_of_joke()
def test_of_get_jokes():
    first_api_test.test_joke_of_chuck(first_api_test.getting_categories())
    '''Делаем негативный тест'''

def test_of_get_jokes_negative():
    first_api_test.test_joke_of_chuck('v')
