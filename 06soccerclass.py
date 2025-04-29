#04.29 객체지향
class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
        print(f'init 실행')

    def change_back_number(self, new_number):
        self.back_number = new_number
        print(f'선수 번호 교체{self.back_number}가 {new_number}')
    def __str__(self):
        return f'저의 이름은 {self.name}, 위치는 {self.position}, 번호는 {self.back_number}'

jh = SoccerPlayer('김종현', 'mf','10')

print(jh)
print(jh.name)

jh.change_back_number(20)
print(f'{jh.back_number=}')

names = ['Messi', 'Ramos', 'Ronaldo', 'Park', 'Son']
position = ['MF', 'DF', 'CF', 'WF' ,'GK']
numbers = [10, 9, 8, 7, 1]

players = [[name, position, number] for name, position, number in zip(names, position, numbers)]
print(players)
print(players[0])

messi = SoccerPlayer(players[0][0], players[0][1], players[0][2])
print(messi.name)

player_ojects = [SoccerPlayer(name, position, number) for name, position, number in zip(names, position, numbers)]
print(player_ojects[0])