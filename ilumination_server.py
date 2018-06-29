from nameko.rpc import rpc
import db
from db import Ilumination
from psycopg2 import OperationalError


class IluminationServer():
    name = "ilumination_server"

    @rpc
    def receive_ilumination(self, ilumination):
        i = Ilumination()
        i.value = ilumination
        try:
            db.session.add(i)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return ilumination
