# using https://www.regextester.com/19 
import os

EMAIL_REGEX = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
SECRET_KEY = os.environ.get('WILEY_SECRET_KEY', 'old_arrack')
DB_CON_STRING = os.environ.get('WILEY_DB_CON_STRING', 'sqlite:////tmp/test.db')



 
