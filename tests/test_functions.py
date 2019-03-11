<<<<<<< HEAD
# from flask_sqlalchemy import SQLAlchemy
=======
from flask_sqlalchemy import SQLAlchemy
>>>>>>> 2efc853f569b31bed390d3159bb9fb07d4dc6549
# from flaskbasic.wsgi import *
from src.flaskbasic.functions import functions
import pytest

fun = functions

def test_student_name():
<<<<<<< HEAD
    assert fun.readName('Lwando',1) == 'Lwando'

def test_all_results():
    assert fun.readResults(1, 'Lwando',10,60,10) == (1, 'Lwando', 10, 60, 10)
=======
    assert fun.readName('Lwando',6) == 'Lwando'

def test_all_results():
    assert fun.readResults(6, 'Lwando',50,60,90) == (6, 'Lwando', 50, 60, 90)
>>>>>>> 2efc853f569b31bed390d3159bb9fb07d4dc6549

    
    
	

		