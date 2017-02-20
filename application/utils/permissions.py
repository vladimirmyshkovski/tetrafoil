from permission import Permission
from .rules import VisitorRule, UserRule, ManagerRule, AdminRule, SuperAdminRule


class VisitorPermission(Permission):
    def rule(self):
        return VisitorRule()


class UserPermission(Permission):
    def rule(self):
        return UserRule()


class ManagerPermission(Permission):
    def rule(self):
        return UserRule()


class AdminPermission(Permission):
    def rule(self):
        return AdminRule()


class SuperAdminPermission(Permission):
    def rule(self):
        return SuperAdminRule()
