from models import Auditions, Roles,engine
from sqlalchemy.orm import sessionmaker

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

audition1 = Auditions(location='Location 1', phone='Phone 1', hired=True)
audition2 = Auditions(location='Location 2', phone='Phone 2', hired=False)

role1 = Roles(charactor_name='Character 1')
role2 = Roles(charactor_name='Character 2')

audition1.role = role1
audition2.role = role2

session.add(audition1)
session.add(audition2)
session.add(role1)
session.add(role2)

session.commit()

print(audition1.location)
print(audition2.location)
print(role1.charactor_name)
print(role2.charactor_name)







