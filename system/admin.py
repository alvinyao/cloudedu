from system import site
from auth.models import User, Group

site.register(User)
site.register(Group)
