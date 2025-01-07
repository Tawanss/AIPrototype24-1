import argparse
from datetime import datetime
def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--bd',
        type=lambda s: datetime.strptime(s, '%Y-%m-%d'),
        required=True,
        help= 'birthday of the user'     
    )
    
    parser.add_argument(
        '--name',
        type=str,
        default="wuttichai",
        help= 'input the name of people who are using the app' #เวลาคนต้องการดูว่าฟังก์ชั่นนี้ทำยังไงหรือคืออะไร     
    )
   
    args = parser.parse_args()
    return args

def printHello(who):
    print(f"Hello world, {who}!!")
def cal_todayVbd(bd):
    td = datetime.today().strftime('%Y-%m-%d')
    return bd-datetime(td)
if __name__ == "__main__":
    input_V = parse_input()
    print('this is my first .py file.')
    printHello(input_V.name)
    print(f'your birthday is {cal_todayVbd(input_V.bd)} from to day')