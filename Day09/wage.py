# -*- coding: UTF-8 -*-
"""案例3：工资结算系统"""

"""
抽象类 / 方法重写 / 多态
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        """
        初始化方法

        :param name: 姓名
        """
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        """
        获得月薪

        :return: 月薪
        """
        pass


class Manager(Employee):
    """部门经理"""

    # 想一想: 如果不定义构造方法会怎么样
    def __init__(self, name):
        # 想一想: 如果不调用父类构造器会怎么样
        super().__init__(name)

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return 150.0 * self._working_hour


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


def main():
    emps = [
        Manager('经理-刘备'), Programmer('程序员-诸葛亮'),
        Manager('经理-曹操'), Salesman('销售-荀彧'),
        Salesman('销售-吕布'), Programmer('程序员-张辽'),
        Programmer('程序员-赵云')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
        elif isinstance(emp, Salesman):
            emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
        # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print(f'{emp.name}本月工资为: ￥{emp.get_salary()}元')


if __name__ == '__main__':
    main()
