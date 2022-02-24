import hashlib
import time
a = 'YuOu.Momtime.Sign'
t=int(time.time())
sign=a+str(t)
m = hashlib.md5()
m.update(sign.encode("utf8"))
a_md5 = m.hexdigest()
print(a_md5,t)

