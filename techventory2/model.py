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
from ffbstatssa.lib import identity

# your data tables

# your_table = Table('yourtable', metadata,
#     Column('my_id', Integer, primary_key=True)
# )


# your model classes


# class YourDataClass(object):
#     pass


# set up mappers between your data tables and classes

# mapper(YourDataClass, your_table)


