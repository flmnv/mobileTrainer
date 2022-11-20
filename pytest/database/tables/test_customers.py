from datetime import datetime

import pytest

from ....src.database.tables.customers import CustomersTable


@pytest.mark.asyncio
async def test_create():
    result = await CustomersTable.create()
    assert result is True


@pytest.mark.asyncio
async def test_insert():
    start_date = datetime(2001, 1, 1)
    update_date = datetime(2002, 2, 2)
    end_date = datetime(2003, 3, 3)

    result_1 = await CustomersTable.insert_row('70000000000', start_date, update_date, end_date)
    result_2 = await CustomersTable.insert_row('70000000001', start_date, update_date, end_date)

    assert (result_1, result_2) == (1, 2)


@pytest.mark.asyncio
async def test_get_row_by_phone():
    start_date = datetime(2001, 1, 1)
    update_date = datetime(2002, 2, 2)
    end_date = datetime(2003, 3, 3)

    result = await CustomersTable.get.row_by_phone('70000000000')
    assert result == (1, '70000000000', str(start_date),
                      str(update_date), str(end_date))


@pytest.mark.asyncio
async def test_get_id_by_phone():
    result = await CustomersTable.get.id_by_phone('70000000000')
    assert result == 1


@pytest.mark.asyncio
async def test_get_id_by_phone_return_none():
    result = await CustomersTable.get.id_by_phone('123')
    assert result is None


@pytest.mark.asyncio
async def test_get_start_date_by_phone():
    start_date = datetime(2001, 1, 1)

    result = await CustomersTable.get.start_date_by_phone('70000000000')
    assert result == str(start_date)


@pytest.mark.asyncio
async def test_get_start_date_by_phone_return_none():
    result = await CustomersTable.get.start_date_by_phone('123')
    assert result is None


@pytest.mark.asyncio
async def test_get_update_date_by_phone():
    update_date = datetime(2002, 2, 2)

    result = await CustomersTable.get.update_date_by_phone('70000000000')
    assert result == str(update_date)


@pytest.mark.asyncio
async def test_get_update_date_by_phone_return_none():
    result = await CustomersTable.get.update_date_by_phone('123')
    assert result is None


@pytest.mark.asyncio
async def test_get_end_date_by_phone():
    end_date = datetime(2003, 3, 3)

    result = await CustomersTable.get.end_date_by_phone('70000000000')
    assert result == str(end_date)


@pytest.mark.asyncio
async def test_get_end_date_by_phone_return_none():
    result = await CustomersTable.get.end_date_by_phone('123')
    assert result is None


@pytest.mark.asyncio
async def test_get_row_by_id():
    result = await CustomersTable.get.row_by_id(2)
    assert result[0] == 2


@pytest.mark.asyncio
async def test_get_phone_by_id():
    result = await CustomersTable.get.phone_by_id(2)
    assert result == '70000000001'


@pytest.mark.asyncio
async def test_get_phone_by_id_return_none():
    result = await CustomersTable.get.phone_by_id(345)
    assert result is None


@pytest.mark.asyncio
async def test_get_start_date_by_id():
    start_date = datetime(2001, 1, 1)

    result = await CustomersTable.get.start_date_by_id(2)
    assert result == str(start_date)


@pytest.mark.asyncio
async def test_get_start_date_by_id_return_none():
    result = await CustomersTable.get.start_date_by_id(345)
    assert result is None


@pytest.mark.asyncio
async def test_get_update_date_by_id():
    update_date = datetime(2002, 2, 2)

    result = await CustomersTable.get.update_date_by_id(2)
    assert result == str(update_date)


@pytest.mark.asyncio
async def test_get_update_date_by_id_return_none():
    result = await CustomersTable.get.update_date_by_id(345)
    assert result is None


@pytest.mark.asyncio
async def test_get_end_date_by_id():
    end_date = datetime(2003, 3, 3)

    result = await CustomersTable.get.end_date_by_id(2)
    assert result == str(end_date)


@pytest.mark.asyncio
async def test_get_end_date_by_id_return_none():
    result = await CustomersTable.get.end_date_by_id(345)
    assert result is None


@pytest.mark.asyncio
async def test_delete_row_by_phone():
    result = await CustomersTable.delete_row_by_phone('70000000000')
    row_data = await CustomersTable.get.row_by_phone('70000000000')

    assert (result, row_data) == (True, None)


@pytest.mark.asyncio
async def test_delete_row_by_id():
    result = await CustomersTable.delete_row_by_id(2)
    row_data = await CustomersTable.get.row_by_id(2)

    assert (result, row_data) == (True, None)
