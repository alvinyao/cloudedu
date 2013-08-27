from crud import views as crud_views
from models import DataDict
from tables import DataDictTable

class CreateView(crud_views.CreateView):
	model = DataDict
	app = 'basic'
	curr = 'datadict'

class DetailView(crud_views.DetailView):
	model = DataDict
	app = 'basic'
	curr = 'datadict'

class DeleteView(crud_views.DeleteView):
	model = DataDict
	app = 'basic'
	curr = 'datadict'

class ListView(crud_views.ListView):
	model = DataDict
	queryset = DataDict.objects.all()
	table_class = DataDictTable
	table_pagination = {'per_page': 10}
	template_name = "essential/list.html"

	app = 'basic'
	curr = 'datadict'
>>>>>>> 5d2884c8ebc5043fb53d4b828f757362f9d9eae7
