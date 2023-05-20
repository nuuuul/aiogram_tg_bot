import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('activities.db')
    cur = base.cursor()
    if base:
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(activity TEXT PRIMARY KEY, city TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?)', tuple(data.values()))
        base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_message(message.from_user.id, f'Активность: {ret[1]}\nГород: {ret[0]}\nЦена: {ret[2]}')


async def sql_read2():
    return cur.execute('SELECT * FROM menu').fetchall()

async def sql_read_param(message):
    if message == 'city':
        for ret in cur.execute('SELECT * FROM menu').fetchall():
            await bot.send_message(message.from_user.id, f'{ret[0]}')


async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE activity == ?', (data,))
    base.commit()
    print(f'{data} deleted!')