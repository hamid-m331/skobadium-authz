from os import environ

class Config:
    ###  GLOBAL CONFIGs  ###

    ENV = environ.get("SKOB_AUTHZ_ENV", "production")
    DEBUG = int(environ.get("SKOB_AUTHZ_DEBUG", "0"))
    TESTING = int(environ.get("SKOB_AUTHZ_TESTING", "0"))

    ###  DATABASE CONFIG  ###

    SQLALCHEMY_DATABASE_URI = environ.get("SKOB_AUTHZ_DATABASE_URI", None)
    SQLALCHEMY_TRACK_MODIFICATIONS = TESTING

    ###  USER CONFIGs  ###
    
    USER_DEFAULT_RULE = environ.get("SKOB_AUTHZ_USER_DEFAULT_RULE", "member")
    USER_DEFAULT_STATUS = environ.get("SKOB_AUTHZ_USER_DEFAULT_STATUS", "inactive")