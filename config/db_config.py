import configparser
import os

config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
config = configparser.ConfigParser()
config.read(config_path)


class DataConfig:
    @classmethod
    def untime_db_config(cls, read):
        """
        Untime DB
        :return: connect object
        """
        conf = config['UNTIME_DATABASE']

        db_config = {'host': conf['db_host'], 'user': conf['db_user'],
                    'password': conf['db_password'], 'port': int(conf['db_port']), 'charset': 'utf8mb4',
                    'database': 'db_user'}
        db_config_kw = {'pool_size': int(conf['pool_size']), 'max_overflow': int(conf['max_overflow']), **{'recycle': int(conf['recycle'])}}

        return db_config, db_config_kw