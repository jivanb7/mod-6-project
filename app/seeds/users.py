from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    users = [
        User(username='angelangel', email='aaa@aa.io', password='pasword1!'),
        User(username='bellbell', email='bbb@aa.io', password='pasword1!'),
        User(username='candycandy', email='ccc@aa.io', password='pasword1!'),
        User(username='decordecor', email='ddd@aa.io', password='pasword1!'),
        User(username='evergreenevergreen', email='eee@aa.io', password='pasword1!'),
        User(username='frostyfrosty', email='fff@aa.io', password='pasword1!'),
        User(username='gingerbreadgingerbread', email='ggg@aa.io', password='pasword1!'),
        User(username='holidayholiday', email='hhh@aa.io', password='pasword1!'),
        User(username='icicleicicle', email='iii@aa.io', password='pasword1!'),
        User(username='jinglejingle', email='jjj@aa.io', password='pasword1!'),
        User(username='krampuskrampus', email='kkk@aa.io', password='pasword1!'),
        User(username='lightslights', email='lll@aa.io', password='pasword1!'),
        User(username='merrymerry', email='mmm@aa.io', password='pasword1!'),
        User(username='nutcrackernutcracker', email='nnn@aa.io', password='pasword1!'),
        User(username='ornamentornament', email='ooo@aa.io', password='pasword1!'),
        User(username='pineconepinecone', email='ppp@aa.io', password='pasword1!'),
        User(username='quiltquilt', email='qqq@aa.io', password='pasword1!'),
        User(username='reindeerreindeer', email='rrr@aa.io', password='pasword1!'),
        User(username='snowflakesnowflake', email='sss@aa.io', password='pasword1!'),
        User(username='tinseltinsel', email='ttt@aa.io', password='pasword1!'),
        User(username='unwrapunwrap', email='uuu@aa.io', password='pasword1!'),
        User(username='vixenvixen', email='vvv@aa.io', password='pasword1!'),
        User(username='winterwinter', email='www@aa.io', password='pasword1!'),
        User(username='xmasxmas', email='xxx@aa.io', password='pasword1!'),
        User(username='yuleyule', email='yyy@aa.io', password='pasword1!'),
        User(username='zestyzesty', email='zzz@aa.io', password='pasword1!')
    ]

    db.session.bulk_save_objects(users)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
