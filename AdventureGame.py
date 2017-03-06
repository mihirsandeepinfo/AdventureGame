import random
def msg(room):
    if room['msg']=='':
        return 'You have entered the '+room['name']
    else:
        return room['msg']
def get_choice(room,dir):
    if dir=='N':
        choice=0
    elif dir == 'E':
        choice = 1
    elif dir=='S':
        choice=2
    elif dir=='W':
        choice=3
    else:
        return -1

    if room['directions'][choice]==0:
        return 4
    else:
        return choice

def main():
    dirs = (0,0,0,0)
    entrance = {'name':'Entrance Way','directions':dirs,'msg':''}
    livingroom = {'name': 'Living Room', 'directions': dirs, 'msg': ''}
    kitchen = {'name': 'Kitchen', 'directions': dirs, 'msg': ''}
    hallway = {'name': 'Hallway', 'directions': dirs, 'msg': ''}
    diningroom = {'name': 'Dining Room', 'directions': dirs, 'msg': ''}
    familyroom = {'name': 'Family Room', 'directions': dirs, 'msg': ''}

    entrance['directions'] = (kitchen,livingroom,0,0)
    livingroom['directions'] = (diningroom,0, 0, entrance)
    kitchen['directions'] = (0, diningroom, entrance, hallway)
    hallway['directions'] = (0,kitchen,0, familyroom)
    diningroom['directions'] = (0, 0, livingroom, kitchen)
    familyroom['directions'] = (0, hallway, 0, 0)

    rooms = [livingroom,diningroom,kitchen,familyroom,hallway]
    rooms_with_eggs = random.choice(rooms)
    eggs_delivered = False
    room = entrance
    print('Welcome, Can you find Mihir\'s basket?')

    while True:
        if eggs_delivered and room['name']=='Entrance Way':
            print('Eggs delivered and returned to Entrance Congrats')
            break;
        elif not eggs_delivered and room['name']==rooms_with_eggs:
            eggs_delivered=True
            print('There\'s the basket, Now go deliver the eggs')
            room['msg']=('You are back in the '+room['name']+'You already delivered the eggs, Now get out')
        else:
            print(msg(room))
            room['msg'] = 'You are back in the '+ room['name']

        stuck = True
        while stuck:
            dir = input('Which direction do you want to go: N,E,S,W?')
            choice = get_choice(room,dir)
            if choice==-1:
                print('Please enter N,E,S,W?')
            elif choice==4:
                print('You cannot go in that direction!')
            else:
                room = room['directions'][choice]
                stuck=False
main()