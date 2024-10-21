from sqlalchemy import create_engine


class Database:

    def __init__(self, connection_string: str, echo: bool = False):
        self.__connection_string = connection_string
        self.connection = create_engine(
            self.__connection_string,
            echo=echo,
        )

    def execute_one(self, sql):
        with self.connection.connect() as connection:
            result = connection.execute(sql)
            return result

    def execute_batch(self, sql_list: list) -> list:
        result_list = [None] * len(sql_list)
        with self.connection.connect() as connection:
            with connection.begin():
                for idx, sql in enumerate(sql_list):
                    # try/except block
                    result = connection.execute(sql)
                    result_list[idx] = result

        return result_list
