

class DatabaseConfig:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'aninditadey15@'
        self.db = 'employees'

    def get_config(self):
        return {
            'localhost': self.host,
            'root': self.user,
            'aninditadey15@': self.password,
            'employees': self.db
        }
