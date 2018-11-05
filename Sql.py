import pyodbc as sq

class Sql:

    def __init__(self, connect):
        self.connect = connect

    def Connect(self, name):

        try:
            con = sq.connect(self.connect)
        except Error as e:
            print(e)

        return None

    def SearchGame(self, name, player, Enemy, basic):
        con = sq.connect(self.connect)
        cursor = con.cursor()
        cursor.execute("select * from DB.dbo.SaveGame where userName = '" + name + "'")
        rows = cursor.fetchall()
        if len(rows) > 0:
            player.setHealth(int(rows[0][2]))
            Enemy.setHealth(int(rows[0][1]))
        cursor.execute("select * from DB.dbo.settings where userName = '" + name + "'")
        rows = cursor.fetchall()
        if len(rows) > 0:
            player.setColor(int(rows[0][2]))
            Enemy.setColor(int(rows[0][1]))
        con.commit()
        return True

    def SearchName(self, name, player, Enemy, basic):
        con = sq.connect(self.connect)
        cursor = con.cursor()
        cursor.execute("select * from DB.dbo.users where name = '" + name + "'")
        count = 0
        rows = cursor.fetchall()
        if len(rows) == 1:
            count = 1
            self.SaveGame(name, player, Enemy, basic)
        if count == 0:
            cursor.execute("insert into DB.dbo.users(name) VALUES ('" + name + "')")

        con.commit()
        return True


    def SaveGame(self, name, player, Enemy, basic):
        con = sq.connect(self.connect)
        cursor = con.cursor()
        cursor.execute("select * from DB.dbo.SaveGame where userName = '" + name + "'")
        rows = cursor.fetchall()
        if len(rows) == 1:
            cursor.execute(
                "update DB.dbo.SaveGame set HealthEnemy = '" + format(Enemy.getHealth()) + "', HealthMan = '" + format(
                    player.getHealth()) + "' where userName = '" + name + "'")

        if len(rows) == 0:
            cursor.execute("insert into DB.dbo.SaveGame(HealthEnemy, HealthMan, userName) VALUES ('" + format(
                Enemy.getHealth()) + "','" + format(player.getHealth()) + "','" + name + "')")

        cursor.execute("select * from DB.dbo.settings where userName = '" + name + "'")
        rows = cursor.fetchall()
        if len(rows) == 1:
            cursor.execute(
                "update DB.dbo.settings set ColorMen = '" + format(Enemy.getColor()) + "', Background = '" + format(
                    basic.getColor()) + "' where userName = '" + name + "'")

        if len(rows) == 0:
            cursor.execute("insert into DB.dbo.settings(ColorMen, Background, userName) VALUES ('" + format(
                Enemy.getColor()) + "','" + format(basic.getColor()) + "','" + name + "')")
        con.commit()
