import argparse
import configparser
from model.objects import IssueTracking

#Config parameters
repository_path = None
issue_tracking_system = None
issue_tracking_url = None
database_engine = None
database_file = None
database_name = None
database_user = None
database_user_password = None
database_host = None
database_port = None
number_of_threads = None
number_of_database_sessions = None
programming_languages = []

DIALECT_SQLITE = 'sqlite'
DIALECT_MYSQL = 'mysql'
DIALECT_POSTGRES = 'postgresql'

def argument_parser():
    parser = argparse.ArgumentParser(description='GtSoog - git data miner')

    #CLI parameters
    parser.add_argument('-f', action="store", required=True, dest="config_file", help='Specify config file')

    args = parser.parse_args()

    config_file = args.config_file
    config_parser(config_file)


def config_parser(config_file):
    if config_file:
        config = configparser.ConfigParser()
        config.read(config_file)

        #Config parameters
        try:
            global programming_languages
            for item in config.items('PROGRAMMINGLANGUAGES'):
                programming_languages.append(item)
        except KeyError:
            raise EnvironmentError('Programming languages not specified in config file')

        try:
            global number_of_threads
            number_of_threads = int(config['REPOSTIROYMINER']['number_of_threads'])
        except KeyError:
            number_of_threads = 1

        try:
            global database_engine
            database_engine = config['DATABASE']['database_engine']
        except KeyError:
            raise EnvironmentError('Database engine not specified in config file')

        try:
            global database_file
            database_file = config['DATABASE']['database_file']
        except KeyError:
            if database_engine == str(DIALECT_SQLITE):
                raise EnvironmentError('SQLite database file is missing in config file')

        try:
            global database_name
            database_name = config['DATABASE']['database_name']
        except KeyError:
            raise EnvironmentError('Database name is missing in config file')

        try:
            global database_user
            database_user = config['DATABASE']['database_user']
        except KeyError:
            if (database_engine == str(DIALECT_MYSQL)) or (database_engine == str(DIALECT_POSTGRES)):
                raise EnvironmentError('Database user is missing in config file')

        try:
            global database_user_password
            database_user_password = config['DATABASE']['database_user_password']
        except KeyError:
            if (database_engine == str(DIALECT_MYSQL)) or (database_engine == str(DIALECT_POSTGRES)):
                raise EnvironmentError('Database user password is missing in config file')

        try:
            global database_host
            database_host = config['DATABASE']['database_host']
        except KeyError:
            if (database_engine == str(DIALECT_MYSQL)) or (database_engine == str(DIALECT_POSTGRES)):
                raise EnvironmentError('Database host is missing in config file')

        try:
            global database_port
            database_port = int(config['DATABASE']['database_port'])
        except KeyError:
            if (database_engine == str(DIALECT_MYSQL)) or (database_engine == str(DIALECT_POSTGRES)):
                raise EnvironmentError('Database port is missing in config file')

        try:
            global number_of_database_sessions
            number_of_database_sessions = int(config['REPOSTIROYMINER']['number_of_database_sessions'])
        except KeyError:
            number_of_database_sessions = 1

        if database_engine == DIALECT_SQLITE:
            number_of_database_sessions = 0

        try:
            global repository_path
            repository_path = config['REPOSITORY']['repository_path']
        except KeyError:
            raise EnvironmentError('Repository Path is missing in config file')

        try:
            global issue_tracking_system
            issue_tracking_system = config['REPOSITORY']['issue_tracking_system']
            if ( issue_tracking_system != str(IssueTracking.TYPE_GITHUB)) and ( issue_tracking_system != str(IssueTracking.TYPE_JIRA)):
                raise EnvironmentError('Unsupported issue tracking system. Use GITHUB or JIRA')
        except KeyError:
            raise EnvironmentError('Issue Tracking System is missing in config file')

        try:
            global issue_tracking_url
            issue_tracking_url = config['REPOSITORY']['issue_tracking_url']
        except KeyError:
            raise EnvironmentError('IssueTracking URL is missing in config file')