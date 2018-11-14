import pyodbc as sq

class Sql:

    def __init__(self, connect, log):
        self.connect = connect
        self.log = log

    def SearchGame(self, name, player, Enemy):

        try:
            con = sq.connect(self.connect)
            self.log.debug("Connection successful ")
        except Exception as e:
            self.log.debug(e)
            return False
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
        try:
            con = sq.connect(self.connect)
            self.log.debug("Connection successful ")
        except Exception as e:
            self.log.debug(e)
            return False
        cursor = con.cursor()

        cursor.execute("select * from DB.dbo.users where name = '" + name + "'")
        count = 0
        rows = cursor.fetchall()
        if len(rows) == 1:
            count = 1
            self.SaveGame(name, player, Enemy, basic)
        if count == 0:
            cursor.execute("insert into DB.dbo.users(name) VALUES ('" + name + "')")
            self.log.debug("Insert users name =" + format(name))
        con.commit()
        return True


    def SaveGame(self, name, player, Enemy, basic):
        try:
            con = sq.connect(self.connect)
            self.log.debug("Connection successful ")
        except Exception as e:
            self.log.debug(e)
            return False
        cursor = con.cursor()
        cursor.execute("select * from DB.dbo.SaveGame where userName = '" + name + "'")
        rows = cursor.fetchall()
        if len(rows) == 1:
            cursor.execute(
                "update DB.dbo.SaveGame set HealthEnemy = '" + format(Enemy.getHealth()) + "', HealthMan = '" + format(
                    player.getHealth()) + "' where userName = '" + name + "'")
            self.log.debug("Update SaveGame name =" + format(name))
        if len(rows) == 0:
            cursor.execute("insert into DB.dbo.SaveGame(HealthEnemy, HealthMan, userName) VALUES ('" + format(
                Enemy.getHealth()) + "','" + format(player.getHealth()) + "','" + name + "')")
            self.log.debug("Insert SaveGame name =" + format(name))
        cursor.execute("select * from DB.dbo.settings where userName = '" + name + "'")
        rows = cursor.fetchall()
        if len(rows) == 1:
            cursor.execute(
                "update DB.dbo.settings set ColorMen = '" + format(Enemy.getColor()) + "', Background = '" + format(
                    basic.getColor()) + "' where userName = '" + name + "'")
            self.log.debug("Update settings name =" + format(name))
        if len(rows) == 0:
            cursor.execute("insert into DB.dbo.settings(ColorMen, Background, userName) VALUES ('" + format(
                Enemy.getColor()) + "','" + format(basic.getColor()) + "','" + name + "')")
            self.log.debug("Insert settings name =" + format(name))
        con.commit()
