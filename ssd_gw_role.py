'''
    This file contains the Role class.
'''
import datetime
from dbmanager import DBManager
from permission import Permission

class Role:
    '''
        A parent class for the system roles.
    '''
    def __init__(self, name):
        self._name = name
        self._created_at = None
        self._updated_at = None
        self._role_id = None # return from database

        # initialise instance of DBManager
        self.db_manager = DBManager()

        # set current_time to now
        self.current_time = datetime.datetime.now().timestamp # convert to UNIX timestamp

    def add_role(self):
        # update created_at and updated_at attributes
        if self._created_at is None:
            self._created_at = self.current_time
        self._updated_at = self.current_time

        # prepare the data for updating the role table
        values = (self._name, self._role_id, self._created_at, self._updated_at)

        # call do_insert method from DBManager
        query = " INSERT INTO roles (name, role_id, created_at, updated_at) \
            VALUES (?, ?, ?, ?)"
        self.db_manager.do_insert(query, [values], dry=False)

    def update_role(self):
        # update the 'updated_at' attribute.
        self._updated_at = self.current_time

        # perform database query to update permission attributes.
        query = "UPDATE roles SET name=?, updated_at=? WHERE role_id=?"
        values = (self._name, self._updated_at, self._role_id)

        # call do_update method from DBmanager.
        self.db_manager.do_update(query, values)

    def delete_role(self):
        # identify records to delete with id
        query = "DELETE FROM roles WHERE id = ?"
        where = (self._role_id)

        # call do_delete method from DBManager
        result = self.db_manager.do_delete(query, where, dry=True)
        
        # if id is matched, records will be deleted.
        if result:
            print(f"Deleted {len(result)} record(s) from roles table.")
            return True
        
        # if id is not matched, records will not be deleted.
        else:
            print("No records deleted.")
            return False
    
    def role_has_permissions(self, role_id, permission_id):
        # access permission_id from Permission class
        self.permission_id = Permission._permission_id

        # prepare the data to update the role_has_permissions table
        query = "INSERT INTO role_has_permissions (role_id, permission_id) \
            VALUES (?, ?)"
        values = (role_id, permission_id)

        # Check if the role_id exists in the referenced table before inserting
        check_query = "SELECT COUNT(*) FROM roles WHERE id = ?;"
        check_values =(role_id,)
        self.db_manager.__db_cursor.execute(check_query, check_values)
        role_exists = self.db_manager.__db_cursor.fetchone()[0] > 0

        # Check if the permission_id exists in the referenced table before inserting
        check_query = "SELECT COUNT(*) FROM permissions WHERE id = ?;"
        check_values =(permission_id,)
        self.db_manager.__db_cursor.execute(check_query, check_values)
        permission_exists = self.db_manager.__db_cursor.fetchone()[0] > 0

        # if both foreign keys (ids) exist, insert into role has permissions table
        if role_exists and permission_exists:
            self.db_manager.do_insert(query, values)
        else:
            print("Invalid role_id or permission_id. The values don't exist in the referenced tables.")
