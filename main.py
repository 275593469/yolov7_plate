# -*- coding=utf-8
from detect_rec_plate import main_handler

if __name__ == '__main__':
    path = "imgs"
    event = {"dictionary" : path}
    context = None
    main_handler(event, context)

