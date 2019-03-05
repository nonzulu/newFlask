import json
import pytest
from flaskbasic.wsgi import Functions


test_func = Functions()

assert test_func.check_name(1) == 1

	

		