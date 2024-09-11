from authz import ma
from authz.model import User

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
    id = ma.auto_field(dump_only=True)
    username = ma.auto_field()
    password = ma.auto_field(loadonly=True)
    register_at = ma.auto_field(dump_only=True)
    last_active_at = ma.auto_field(dump_only=True)
    last_failed_at = ma.auto_field(dump_only=True)
    status = ma.auto_field()