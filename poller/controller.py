from poller.pooler import pooler
from poller.filter import filter
import random
import time
from threading import current_thread
 
def print_delay(df):
    n = random.randrange(1,10)
    print("Sleeping for :",n,"Secs",current_thread().ident)
    print(df)
    time.sleep(n)

q = list()
po1 = pooler()
fl1 = filter()
fl1.main()

df = fl1.filter_tickets()
q = po1.put_q(df,q)
po1.pool(print_delay,q)