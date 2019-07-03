from doctrace.DAL.sql_Groups import Groups


class Groups1:

    @classmethod
    def get_groups(cls):

        myGroup = Groups.getGroup()

        return myGroup