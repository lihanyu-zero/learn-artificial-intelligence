import numpy as np
from unittest import TestCase

class TestNumpyStock(TestCase):
    # 读取数据
    def testReadFile(self):
        file_name = './../data/data_for_4.1.csv'
        end_prince, volumn = np.loadtxt(
            file_name, delimiter=',', usecols=(2, 6), unpack=True
        )
        print('end_prince={}'.format(end_prince))
        print('volumn={}'.format(volumn))

    # 计算极值
    def testMaxAndMin(self):
        file_name = './../data/data_for_4.1.csv'
        high_price, low = np.loadtxt(
            file_name, delimiter=',', usecols=(4, 5), unpack=True
        )
        print('max_price={}'.format(high_price.max()))
        print('min_price={}'.format(high_price.min()))

    # 计算极差
    def testPtp(self):
        file_name = './../data/data_for_4.1.csv'
        high_price, low_price = np.loadtxt(
            file_name, delimiter=',', usecols=(4, 5), unpack=True
        )
        print('ptp={}'.format(np.ptp(high_price)))
        print('ptp={}'.format(np.ptp(low_price)))

    # 计算均值
    def testAVG(self):
        file_name = './../data/data_for_4.1.csv'
        end_prince, volumn = np.loadtxt(
            file_name, delimiter=',', usecols=(2, 6), unpack=True
        )
        print('avg_price={}'.format(np.average(end_prince)))
        print('VWAP={}'.format(np.average(end_prince, weights=volumn)))

    # 计算中位数
    def testMedian(self):
        file_name = './../data/data_for_4.1.csv'
        end_prince, volumn = np.loadtxt(
            file_name, delimiter=',', usecols=(2, 6), unpack=True
        )
        print('median={}'.format(np.median(end_prince)))

    # 计算方差
    def testVar(self):
        file_name = './../data/data_for_4.1.csv'
        end_prince, volumn = np.loadtxt(
            file_name, delimiter=',', usecols=(2, 6), unpack=True
        )
        print('var={}'.format(np.var(end_prince)))

    def testVolatility(self):
        file_name = './../data/data_for_4.1.csv'
        end_prince, volumn = np.loadtxt(
            file_name, delimiter=',', usecols=(2, 6), unpack=True
        )
        log_return = np.diff(np.log(end_prince))

        annual_volatility = log_return.std() / log_return.mean() * np.sqrt(250) # 年波动(250个交易日)
        monthly_volatility = log_return.std() / log_return.mean() * np.sqrt(12) # 月波动
        print('log_return={}'.format(log_return))
        print('annual_volatility={}'.format(annual_volatility))
        print('monthly_volatility={}'.format(monthly_volatility))