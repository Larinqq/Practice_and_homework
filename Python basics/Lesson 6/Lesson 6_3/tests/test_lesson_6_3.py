import sys
sys.path.append("/Lesson 6/Lesson 6_3/")
from Validators_lesson_6_3 import check_name, check_pass, check_mail, check_pin


def test_check_name_func():
    assert check_name('Даниил')
    assert not check_name('Р_и_т_а')
    assert not check_name('К0нстантин')
    assert check_name('А Ф')
    assert check_name('Елена')


def test_check_pass_func():
    assert check_pass('secretd00r')
    assert check_pass('huskyeye5')
    assert not check_pass('secret')
    assert check_pass('m3wm3wm3w')
    assert not check_pass('fh43j_!')


def test_check_mail_func():
    assert check_mail('local@gmail.com')
    assert not check_mail('you(at)gmail.com')
    assert check_mail('me@gmail.ru')
    assert not check_mail('@abxaz')
    assert not check_mail('alarm@.mail.com')


def test_check_pin_func():
    assert check_pin('1239')
    assert not check_pin('3333')
    assert not check_pin('1234')
    assert not check_pin('00011')
    assert check_pin('8765')
