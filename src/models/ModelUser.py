from .entities.User import User


class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, username, password, email, fullname, role, code FROM users 
                    WHERE username = '{}'""".format(user.username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], User.check_password(row[2], user.password), row[3], row[4], row[5], row[6])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def register(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO users (username, password, email, fullname, role, code)
                    VALUES ('{}', '{}', '{}', '{}', '{}', '{}')""".format(user.username, User.generate_password(user.password), user.email, user.fullname, user.role, user.code)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, username, password, email, fullname, role, code FROM users WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = User(row[0], row[1], None, row[3], row[4], row[5], row[6])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
