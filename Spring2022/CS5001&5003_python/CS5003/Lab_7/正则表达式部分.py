"""
    CS5001-5003 Spring 2022
    Template for most Python coding assignments
    Name / Partner
"""
import re

def main():
    numRegex = re.compile(r'(-)?(\d+.\d+|\d+)')
    # test empty files
    result1 = numRegex.search(' \n  ')
    print(result1)  # 返回None,如果使用group()方法会报错

    # test integer
    result2 = numRegex.search('   -234   \n')
    result3 = numRegex.search('  234')
    print(result2.group())  # -234
    print(result3.group())  # 234

    # test float
    result4 = numRegex.search('-2.34 ')
    result5 = numRegex.search('\n  2.34')
    print(result4.group())  #-2.34
    print(result5.group())  #2.34

if __name__ == '__main__':
    main()    
