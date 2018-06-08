from nameko.rpc import rpc
import db
from db import Ilumination


class IluminationServer():
    name = "ilumination_server"

    @rpc
    def receive_ilumination(self, ilumination):
        i = Ilumination()
        i.value = ilumination
        db.session.add(i)
        db.session.commit()
        return ilumination
