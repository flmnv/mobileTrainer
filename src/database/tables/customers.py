import sqlite3
import typing

from .config.database_config import DATABASE_PATH


class CustomersTableGet:
    """
    Base customers table get class
    """

    @staticmethod
    async def row_by_phone(phone: str) -> typing.Union[list, None, bool]:
        """
        Use this method to get row by phone

        :param phone: Customer phone number
        :type phone: :obj:`str`

        :return: On success, returns a list with row data or None,
        otherwise False
        :rtype: :obj:`typing.Union[list, None, bool]`
        """
        try:
            connect = sqlite3.connect(DATABASE_PATH)
            cursor = connect.cursor()

            insert_values = [phone]

            cursor.execute(
                '''
                SELECT * FROM customers
                WHERE phone = ?;
                ''', insert_values)

            return cursor.fetchone()
        except BaseException:
            return False

    @staticmethod
    async def id_by_phone(phone: str) -> typing.Union[int, None, bool]:
        """
        Use this method to get customer id by phone

        :param phone: Customer phone number
        :type phone: :obj:`str`

        :return: On success, returns int or None, otherwise False
        :rtype: :obj:`typing.Union[int, None, bool]`
        """
        try:
            connect = sqlite3.connect(DATABASE_PATH)
            cursor = connect.cursor()

            insert_values = [phone]

            cursor.execute(
                '''
                SELECT id FROM customers
                WHERE phone = ?;
                ''', insert_values)

            r_data = cursor.fetchone()

            if r_data:
                return r_data[0]

            return None
        except BaseException:
            return False

    @staticmethod
    async def start_date_by_phone(phone: str) -> typing.Union[str, None, bool]:
        """
        Use this method to get customer start date by phone

        :param phone: Customer phone number
        :type phone: :obj:`str`

        :return: On success, returns str or None, otherwise False
        :rtype: :obj:`typing.Union[str, None, bool]`
        """
        try:
            connect = sqlite3.connect(DATABASE_PATH)
            cursor = connect.cursor()

            insert_values = [phone]

            cursor.execute(
                '''
                SELECT start_date FROM customers
                WHERE phone = ?;
                ''', insert_values)

            r_data = cursor.fetchone()

            if r_data:
                return r_data[0]

            return None
        except BaseException:
            return False

    @staticmethod
    async def update_date_by_phone(phone: str) -> typing.Union[str, None, bool]:
        """
        Use this method to get customer update date by phone

        :param phone: Customer phone number
        :type phone: :obj:`str`

        :return: On success, returns str or None, otherwise False
        :rtype: :obj:`typing.Union[str, None, bool]`
        """
        try:
            connect = sqlite3.connect(DATABASE_PATH)
            cursor = connect.cursor()

            insert_values = [phone]

            cursor.execute(
                '''
                SELECT update_date FROM customers
                WHERE phone = ?;
                ''', insert_values)

            r_data = cursor.fetchone()

            if r_data:
                return r_data[0]

            return None
        except BaseException:
            return False

    @staticmethod
    async def end_date_by_phone(phone: str) -> typing.Union[str, None, bool]:
        """
        Use this method to get customer end date by phone

        :param phone: Customer phone number
        :type phone: :obj:`str`

        :return: On success, returns str or None, otherwise False
        :rtype: :obj:`typing.Union[str, None, bool]`
        """
        try:
            connect = sqlite3.connect(DATABASE_PATH)
            cursor = connect.cursor()

            insert_values = [phone]

            cursor.execute(
                '''
                SELECT end_date FROM customers
                WHERE phone = ?;
                ''', insert_values)

            r_data = cursor.fetchone()

            if r_data:
                return r_data[0]

            return None
        except BaseException:
            return False

    @staticmethod
    async def row_by_id(customer_id: int) -> typing.Union[list, None, bool]:
        """
        Use this method to get row by customer id

        :param customer_id: Customer id
        :type customer_id: :obj:`int`

        :return: On success, returns a list with row data or None,
        otherwise False
        :rtype: :obj:`typing.Union[list, None, bool]`
        """
        try:
            connect = sqlite3.connect(DATABASE_PATH)
            cursor = connect.cursor()

            insert_values = [customer_id]

            cursor.execute(
                '''
                SELECT * FROM customers
                WHERE id = ?;
                ''', insert_values)

            return cursor.fetchone()
        except BaseException:
            return False

    @staticmethod
    async def phone_by_id(customer_id: int) -> typing.Union[str, None, bool]:
        """
        Use this method to get customer phone number by customer id

        :param customer_id: Customer id
        :type customer_id: :obj:`int`

        :return: On success, returns str or None, otherwise False
        :rtype: :obj:`typing.Union[str, None, bool]`
        """
        try:
            connect = sqlite3.connect(DATABASE_PATH)
            cursor = connect.cursor()

            insert_values = [customer_id]

            cursor.execute(
                '''
                SELECT phone FROM customers
                WHERE id = ?;
                ''', insert_values)

            r_data = cursor.fetchone()

            if r_data:
                return r_data[0]

            return None
        except BaseException:
            return False

    @staticmethod
    async def start_date_by_id(customer_id: int) -> typing.Union[str, None, bool]:
        """
        Use this method to get customer start date by customer id

        :param customer_id: Customer id
        :type customer_id: :obj:`int`

        :return: On success, returns str or None, otherwise False
        :rtype: :obj:`typing.Union[str, None, bool]`
        """
        try:
            connect = sqlite3.connect(DATABASE_PATH)
            cursor = connect.cursor()

            insert_values = [customer_id]

            cursor.execute(
                '''
                SELECT start_date FROM customers
                WHERE id = ?;
                ''', insert_values)

            r_data = cursor.fetchone()

            if r_data:
                return r_data[0]

            return None
        except BaseException:
            return False

    @staticmethod
    async def update_date_by_id(customer_id: int) -> typing.Union[str, None, bool]:
        """
        Use this method to get customer update date by customer id

        :param customer_id: Customer id
        :type customer_id: :obj:`int`

        :return: On success, returns str or None, otherwise False
        :rtype: :obj:`typing.Union[str, None, bool]`
        """
        try:
            connect = sqlite3.connect(DATABASE_PATH)
            cursor = connect.cursor()

            insert_values = [customer_id]

            cursor.execute(
                '''
                SELECT update_date FROM customers
                WHERE id = ?;
                ''', insert_values)

            r_data = cursor.fetchone()

            if r_data:
                return r_data[0]

            return None
        except BaseException:
            return False

    @staticmethod
    async def end_date_by_id(customer_id: int) -> typing.Union[str, None, bool]:
        """
        Use this method to get customer end date by customer id

        :param customer_id: Customer id
        :type customer_id: :obj:`int`

        :return: On success, returns str or None, otherwise False
        :rtype: :obj:`typing.Union[str, None, bool]`
        """
        try:
            connect = sqlite3.connect(DATABASE_PATH)
            cursor = connect.cursor()

            insert_values = [customer_id]

            cursor.execute(
                '''
                SELECT end_date FROM customers
                WHERE id = ?;
                ''', insert_values)

            r_data = cursor.fetchone()

            if r_data:
                return r_data[0]

            return None
        except BaseException:
            return False


class CustomersTable:
    """
    Base customers table class
    """

    get = CustomersTableGet

    @staticmethod
    async def create() -> bool:
        """
        Use this method to create table

        :return: On success, returns true, otherwise False
        :rtype: :obj:`bool`
        """
        try:
            connect = sqlite3.connect(DATABASE_PATH)
            cursor = connect.cursor()

            cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS customers(
                    id INTEGER PRIMARY KEY,
                    phone TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    update_date TEXT NOT NULL,
                    end_date TEXT NOT NULL);
                ''')

            connect.commit()

            return True
        except BaseException:
            return False

    @staticmethod
    async def insert_row(phone: str, start_date: str,
                         update_date: str, end_date: str) -> typing.Union[int, bool]:
        """
        Use this method to insert row

        :param phone: Customer phone number
        :type phone: :obj:`str`
        :param start_date: Start date of customer access
        :type start_date: :obj:`str`
        :param update_date: Update date of customer access
        :type update_date: :obj:`str`
        :param end_date: End date of customer access
        :type end_date: :obj:`str`

        :return: On success, returns the last row id, otherwise False
        :rtype: :obj:`typing.Union[int, bool]`
        """
        try:
            connect = sqlite3.connect(DATABASE_PATH)
            cursor = connect.cursor()

            insert_values = [
                phone, start_date, update_date, end_date]

            cursor.execute(
                '''
                INSERT INTO customers (
                    phone, start_date, update_date, end_date)
                VALUES (?, ?, ?, ?);
                ''', insert_values)

            connect.commit()

            return cursor.lastrowid
        except BaseException:
            return False

    @staticmethod
    async def delete_row_by_phone(phone: str) -> bool:
        """
        Use this method to delete row by phone number

        :param phone: Customer phone number
        :type phone: :obj:`str`

        :return: On success, returns true, otherwise False
        :rtype: :obj:`bool`
        """
        try:
            connect = sqlite3.connect(DATABASE_PATH)
            cursor = connect.cursor()

            insert_values = [phone]

            cursor.execute(
                '''
                DELETE FROM customers
                WHERE phone = ?;
                ''', insert_values)

            connect.commit()

            return True
        except BaseException:
            return False

    @staticmethod
    async def delete_row_by_id(customer_id: int) -> bool:
        """
        Use this method to delete row by customer id

        :param customer_id: Customer id
        :type customer_id: :obj:`int`

        :return: On success, returns true, otherwise False
        :rtype: :obj:`bool`
        """
        try:
            connect = sqlite3.connect(DATABASE_PATH)
            cursor = connect.cursor()

            insert_values = [customer_id]

            cursor.execute(
                '''
                DELETE FROM customers
                WHERE id = ?;
                ''', insert_values)

            connect.commit()

            return True
        except BaseException:
            return False
