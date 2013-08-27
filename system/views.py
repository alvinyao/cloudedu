from crud import views as crud_views
from auth.models import User
from tables import UserTable

class ListView(crud_views.ListView):
	model = DataDict
	queryset = DataDict.objects.all()
	table_class = DataDictTable
	table_pagination = {'per_page': 10}
