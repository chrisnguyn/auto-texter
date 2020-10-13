"""
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
deactive to exit virtual environment
"""

import os
from dotenv import load_dotenv

load_dotenv()
test_env = os.environ.get('TEST')

print(test_env)
