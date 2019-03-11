# Referencing the modules
from flask_sqlalchemy import SQLAlchemy
# from flaskbasic.wsgi import *
from src.flaskbasic.functions import functions
import pytest

fun = functions
#  test by name and id
def test_student_name():
    assert fun.readName('Zukisa',2) == 'Zukisa'

# test all results
def test_all_results():
    assert fun.readResults(2, 'Zukisa',10,60,5) == (2, 'Zukisa', 10, 60, 5)

    
    
	

		