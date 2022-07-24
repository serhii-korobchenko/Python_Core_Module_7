""" Для инициализации своего проекта, создайте вспомогательную функцию 
do_setup(args_dict), которая будет вызывать функцию setup с параметрами из 
словаря args_dict.

Структура словаря для параметра args_dicts должна быть следующей

{
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
} """


from setuptools import setup
args_dict = {
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}

def do_setup():
    result = setup(args_dict)
    print (result)

    
do_setup(args_dict)