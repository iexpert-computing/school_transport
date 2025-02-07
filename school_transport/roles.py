# school_transport/roles.py
from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'view_user': True,
        'add_user': True,
        'change_user': True,
        'delete_user': True,
        'manage_transport': True,
    }

class Driver(AbstractUserRole):
    available_permissions = {
        'view_schedule': True,
    }
