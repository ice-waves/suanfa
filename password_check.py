"""
给定用户密码输入流nput，输入流中字符＜表示退格，可以清除前一个输入的字符，请你编写程序，输出最终得到的密码字符，并判断密码是否满足如下的密码安全要求。
密码安全要求如下：
1.密码长度>=8;
2.密码至少需要包含1个大写字母，
3.密码至少需要包含1个小写宇母,
4.密码至少需要包含1个数字;
5.密码至少需要包含1个字母和数字以外的非空白持殊字符
注意空串退格后仍然为空串，旦用户输入的字符丰不包含<字符和空白字符。
"""


def passwordCheck(password: str) -> str:
    resultList = []
    upperChars = []
    lowerChars = []
    intChars = []
    specialChars = []
    for char in password:
        if char == '<':
            if len(resultList) == 0:
                continue
            popVal = resultList.pop()
            if popVal.isupper():
                upperChars.pop() 
            elif popVal.islower():
                lowerChars.pop()
            elif popVal.isdigit():
                intChars.pop()
            elif not popVal.isalnum() and not popVal.isspace():
                specialChars.pop()
            continue
                 
        if 65 <= ord(char) <= 90: # 大写字符判段
            resultList.append(char)
            upperChars.append(char)
        elif 97 <= ord(char) <= 122: # 小写字符判断
            resultList.append(char)
            lowerChars.append(char)
        elif 48 <= ord(char) <= 57: # 数字判断
            resultList.append(char)
            intChars.append(char)
        elif not char.isspace() and not char.isalnum(): # 特殊字符判断
            resultList.append(char)
            specialChars.append(char)
        
    result = ''.join(resultList)
    if len(upperChars) >= 1 and len(lowerChars) >= 1 and len(intChars) >= 1 and len(specialChars) >= 1:
        return result + ',' + 'true'
    
    return result + ',' + 'false'


if __name__ == '__main__':
    print(passwordCheck('ABC<c89%000<'))




