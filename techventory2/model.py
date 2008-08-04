import pkg_resources
pkg_resources.require("SQLAlchemy>=0.3.10")
from turbogears.database import metadata, mapper
# import some basic SQLAlchemy classes for declaring the data model
# (see http://www.sqlalchemy.org/docs/04/ormtutorial.html)
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import relation
# import some datatypes for table columns from SQLAlchemy
# (see http://www.sqlalchemy.org/docs/04/types.html for more)
from sqlalchemy import String, Unicode, Integer, DateTime
from techventory2.lib.identity import *

# your data tables

# your_table = Table('yourtable', metadata,
#     Column('my_id', Integer, primary_key=True)
# )

servers_table = Table('servers', metadata,
    Column('id', Integer, primary_key=True),
    Column('tag', Integer),
    Column('name', Unicode),
    Column('description', Unicode)
)

# your model classes

# class YourDataClass(object):
#     pass

class Server(object):
    pass

# set up mappers between your data tables and classes

# mapper(YourDataClass, your_table)

mapper(Server, servers_table)