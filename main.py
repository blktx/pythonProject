# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def intraday_stockprice():
    ts = TimeSeries(key='GAMRCFEXTWTC2G5A', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol='IMAX', interval='1min', outputsize='full')
    print(data)
    data['4. close'].plot()
    plt.title('Intraday Times Series for the IMAX stock (1 min)')
    plt.show()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    intraday_stockprice()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
