from crud import views as crud_views
from models import DataDict
from tables import DataDictTable

class CreateView(crud_views.CreateView):
	model = DataDict

class DetailView(crud_views.DetailView):
	model = DataDict

class DeleteView(crud_views.DeleteView):
	model = DataDict

class ListView(crud_views.ListView):
	model = DataDict
	queryset = DataDict.objects.all()
	table_class = DataDictTable
	table_pagination = {'per_page': 10}
