from datetime import datetime
import os
from pathlib import Path


def  log_decor(pth = 0):
    def log_decor_(old_function):

        dt = "{:%d %B %Y %H:%M}".format(datetime.now())
        name = old_function.__name__

        def new_function(*args, **kwargs):
            aruments = f'{args}  {kwargs}'
            result = old_function(*args, **kwargs)
            lgtext = f'{dt}  {name}  {aruments} \n'
            # p = Path.home
            if pth :
                p = Path.home()
                print(p)
                pth_ = pth.split('/')
                for i in pth_:
                    p = p/i
                p = p/"log"

                if not os.path.exists(p):
                    os.makedirs(p)
                p = p/"log.txt"

            else:
                p = Path('log')
                if not os.path.exists(p):
                    os.makedirs(p)
                p = p/"log.txt"

            with open(p, 'a') as file_obj:
                file_obj.write(lgtext)
            
            return result
        return new_function
    return log_decor_