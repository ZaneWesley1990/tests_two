import requests
import unittest
import json

TARGET_API = "https://deckofcardsapi.com/api/deck/"
EXPECTED_HTTP = 200

class test_api(unittest.TestCase):

    def test_1(self):
        response = requests.get("https://deckofcardsapi.com")
        self.assertEqual(response.status_code, EXPECTED_HTTP)

        with open("api.txt", "w") as file:
            file.write(f'REPORT\n\nStatus_code ==>\n{response.status_code}\n\n')

    def test_2(self):
        response = requests.get(f'{TARGET_API}new/shuffle/?deck_count=1')
        data = response.json()
        s = (json.dumps(response.json(), indent=2))

        global deck_id
        deck_id = data['deck_id']

        with open("api.txt", "a") as file:
            file.write(f'Deck_count ==>\n{s}\n')

    def test_3(self):
        response = requests.get(f'{TARGET_API}{deck_id}/shuffle/?remaining=true')
        s = (json.dumps(response.json(), indent=2))

        with open("api.txt", "a") as file:
            file.write(f'Remaining_cards ==>\n{s}\n')

    def test_4(self):
        response = requests.get(f'{TARGET_API}{deck_id}/draw/?count=3')
        data = response.json()
        s = (json.dumps(response.json(), indent=2))
        v = []
        c = []

        for el in data["cards"]:
            v.append(el['value'])
            c.append(el['code'])
            global str1
            str1 = (''.join(str(e) + ',' for e in c)).strip(",")
            global str1_one
            str1_one = (''.join(str(e) + ',' for e in v)).strip(",")

        d = v.copy()
        for i in range(len(d)):
            if d[i] in ['JACK', 'QUEEN', 'KING', 'ACE']:
                d[i] = 10
            elif d[i] == 'ACE':
                d[i] = 1

        global n
        res = [int(i) for i in d]
        n = sum(res)

        with open("api.txt", "a") as file:
            file.write(f'Player1 ==>\n{s}\nPlayer1 - cards in hand ==>\nCode - {str1}\nValues - {str1_one}\nTotal - {n}\n\n')

    def test_5(self):
        response = requests.get(f'{TARGET_API}{deck_id}/draw/?count=3')
        data = response.json()
        p = (json.dumps(response.json(), indent=2))
        u = []
        t = []

        for el in data["cards"]:
            u.append(el['value'])
            t.append(el['code'])
            global str2
            str2 = (''.join(str(e) + ',' for e in t)).strip(",")
            global str2_one
            str2_one = (''.join(str(e) + ',' for e in u)).strip(",")

        a = u.copy()
        for i in range(len(a)):
            if a[i] in ['JACK', 'QUEEN', 'KING', 'ACE']:
                a[i] = 10
            elif a[i] == 'ACE':
                a[i] = 1

        global b
        resres_two = [int(i) for i in a]
        b = sum(resres_two)

        with open("api.txt", "a") as file:
            file.write(f'Player2 ==>\n{p}\nPlayer2 - cards in hand ==>\nCode - {str2}\nValues - {str2_one}\nTotal - {b}\n\n')

    def test_6(self):
        pile_one = "player1"
        pile_two = "player2"

        response_plone = requests.get(f'{TARGET_API}{deck_id}/pile/{pile_one}/add/?cards={str1}')
        s1 = (json.dumps(response_plone.json(), indent=2))
        response_plone_one = requests.get(f'{TARGET_API}{deck_id}/pile/{pile_one}/shuffle/')
        w1 = (json.dumps(response_plone_one.json(), indent=2))
        response_plone_two = requests.get(f'{TARGET_API}{deck_id}/pile/{pile_one}/list/')
        cards_one = (json.dumps(response_plone_two.json(), indent=2))

        response_pltwo = requests.get(f'{TARGET_API}{deck_id}/pile/{pile_two}/add/?cards={str2}')
        s2 = (json.dumps(response_pltwo.json(), indent=2))
        response_pltwo_one = requests.get(f'{TARGET_API}{deck_id}/pile/{pile_two}/shuffle/')
        w2 = (json.dumps(response_pltwo_one.json(), indent=2))
        response_pltwo_two = requests.get(f'{TARGET_API}{deck_id}/pile/{pile_two}/list/')
        cards_two = (json.dumps(response_pltwo_two.json(), indent=2))

        with open("api.txt", "a") as file:
            file.write(f'Player1 ==>\n{s1}\nPlayer1 - cards in hand ==>\n{cards_one}\nCards for player1 ==>{w1}\n\n')

        with open("api.txt", "a") as file:
            file.write(f'Player2 ==>\n{s2}\nPlayer2 - cards in hand ==>\n{cards_two}\nCards for player2 ==>{w2}\n\n')

    def test_7(self):
        if b < n <= 21:
            with open("api.txt", "a") as file:
                file.write(f'WINNER ==>\nPLAYER1\n')
        elif n < b <= 21:
            with open("api.txt", "a") as file:
                file.write(f'WINNER ==>\nPLAYER2\n')
        elif n <= 21 < b:
            with open("api.txt", "a") as file:
                file.write(f'WINNER ==>\nPLAYER1\n')
        elif b <= 21 < n:
            with open("api.txt", "a") as file:
                file.write(f'WINNER ==>\nPLAYER2\n')
        else:
            with open("api.txt", "a") as file:
                file.write(f'WINNER ==>\nCASINO\n')

if __name__ == '__main__':
    unittest.main()