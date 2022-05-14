"""
    CS5003 Spring 2022
    Assignment number of info
    Name / Partner
"""


def foo(x):
    m_dic = {}
    for i in x:
        temp = i.lower()
        if temp in m_dic:
            m_dic[temp] += 1
        else:
            m_dic[temp] = 1
    print(m_dic)
