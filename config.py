import os
basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = 'MST3K'
    SQLALCHEMY_DATABASE_URI = 'postgresql://eyzqobwt:Nbg-dLcNC-PrIbskjfVVODnNslfd-QSP@fanny.db.elephantsql.com/eyzqobwt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # STRIPE_SECRET = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'
