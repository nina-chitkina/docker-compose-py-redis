import redis

r = redis.Redis(host='localhost' , port='6379')

try:
    r.set('A' , '5')
    print("set complete")
except Exception as e:
    print(e)
    print("fail")



try:
    r.get('A')
    print("get complete")
except Exception as e:
    print(e)
    print("fail")    
