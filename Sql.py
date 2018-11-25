import pyodbc as sq


class Sql:

    def __init__(self, connect,  name, log):
        self.connect = connect
        self.name = name
        self.log = log

    def SearchGame(self, player, enemy):
        """
        Search game
        :param player: Player
        :param enemy: Enemy
        """
        try:
            con = sq.connect(self.connect)
            self.log.debug("Connection successful ")
        except Exception as e:
            self.log.debug(e)
            return False
        cursor = con.cursor()
        cursor.execute("select * from DB.dbo.SaveGame where userName = '" + self.name + "'")
        rows = cursor.fetchall()
        if len(rows) > 0:
            player.setHealth(int(rows[0][2]))
            enemy.setHealth(int(rows[0][1]))
        cursor.execute("select * from DB.dbo.settings where userName = '" + self.name + "'")
        rows = cursor.fetchall()
        if len(rows) > 0:
            player.setColor(int(rows[0][2]))
            enemy.setColor(int(rows[0][1]))
        con.commit()

    def SearchName(self, player, enemy, basic):
        try:
            con = sq.connect(self.connect)
            self.log.debug("Connection successful ")
        except Exception as e:
            self.log.debug(e)
            return False
        cursor = con.cursor()

        cursor.execute("select * from DB.dbo.users where name = '" + self.name + "'")
        count = 0
        rows = cursor.fetchall()
        if len(rows) == 1:
            count = 1
            self.SaveGame(player, enemy, basic)
        if count == 0:
            cursor.execute("insert into DB.dbo.users(name) VALUES ('" + self.name + "')")
            # self.log.debug("Insert users name =" + format(name))
            self.SaveGame(player, enemy, basic)
            self.log.debug("Insert users name =" + format(self.name))
        con.commit()
        return True

    def SetName(self, name):
        self.name = name

    def getName(self):
        return self.name


    def SaveGame(self, player, enemy, basic):
        try:
            con = sq.connect(self.connect)
            self.log.debug("Connection successful ")
        except Exception as e:
            self.log.debug(e)
            return False
        cursor = con.cursor()
        cursor.execute("select * from DB.dbo.SaveGame where userName = '" + self.name + "'")
        rows = cursor.fetchall()
        if len(rows) == 1:
            cursor.execute(
                "update DB.dbo.SaveGame set HealthEnemy = '" + format(enemy.getHealth()) + "', HealthMan = '" + format(
                    player.getHealth()) + "' where userName = '" + self.name + "'")
            self.log.debug("Update SaveGame name =" + format(self.name))
        if len(rows) == 0:
            cursor.execute("insert into DB.dbo.SaveGame(HealthEnemy, HealthMan, userName) VALUES ('" + format(
                enemy.getHealth()) + "','" + format(player.getHealth()) + "','" + self.name + "')")
            self.log.debug("Insert SaveGame name =" + format(self.name))
        cursor.execute("select * from DB.dbo.settings where userName = '" + self.name + "'")
        rows = cursor.fetchall()
        if len(rows) == 1:
            cursor.execute(
                "update DB.dbo.settings set ColorMen = '" + format(enemy.getColor()) + "', Background = '" + format(
                    basic.getColor()) + "' where userName = '" + self.name + "'")
            self.log.debug("Update settings name =" + format(self.name))
        if len(rows) == 0:
            cursor.execute("insert into DB.dbo.settings(ColorMen, Background, userName) VALUES ('" + format(
                enemy.getColor()) + "','" + format(basic.getColor()) + "','" + self.name + "')")
            self.log.debug("Insert settings name =" + format(self.name))
        con.commit()
