import uuid
from Scheduler.db.mysql.base import session, Business


b = Business(business_id=str(uuid.uuid4()),email="leiyang_ace@163.com",mobile="17072951861",module="1,2")
session.add(b)
session.commit()
session.remove()