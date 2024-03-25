import sys
sys.path.append("/home/larinqq/Practice_and_homework/Lesson 6_3/")

from Validators_lesson_6_3 import check_name, check_pass, check_mail, check_pin


def test_check_name_func():
    assert True == check_name('Даниил')
    assert False == check_name('Р_и_т_а')
    assert False == check_name('К0нстантин')
    assert True == check_name('А Ф')
    assert True == check_name('Елена')


def test_check_pass_func():
    assert True == check_pass('secretd00r')
    assert True == check_pass('huskyeye5')
    assert False == check_pass('secret')
    assert True == check_pass('m3wm3wm3w')
    assert False == check_pass('fh43j_!')


def test_check_mail_func():
    assert True == check_mail('local@gmail.com')
    assert False == check_mail('you(at)gmail.com')
    assert True == check_mail('me@gmail.ru')
    assert False== check_mail('@abxaz')
    assert False == check_mail('alarm@.mail.com')


def test_check_pin_func():
    assert True == check_pin('1239')
    assert False == check_pin('3333')
    assert False == check_pin('1234')
    assert False == check_pin('00011')
    assert True == check_pin('8765')



