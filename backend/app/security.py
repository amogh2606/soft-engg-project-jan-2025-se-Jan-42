from app.models import db, User, Role
from flask_security import Security, SQLAlchemyUserDatastore



user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(datastore=user_datastore, register_blueprint=False)


@security.want_json
def want_json(request):
    return True

