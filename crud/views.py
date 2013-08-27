"""
These views do nothing other than provide members of the 'plain' CRUD template
set as default template names.
"""
from django.views import generic
from django_tables2.views import SingleTableView

class CreateView( generic.CreateView ):
	template_name = 'crud/plain/form.html'
	app  = 'res'
	curr = 'datadict'

	def get_context_data(self, **kwargs):
		context = super(CreateView, self).get_context_data(**kwargs)
		if hasattr(self, 'app'):
			context['app'] = self.app
		if hasattr(self, 'curr'):
			context['curr'] = self.curr
		return context


class UpdateView( generic.UpdateView ):
	template_name = 'crud/plain/form.html'
	app  = 'res'
	curr = 'datadict'

	def get_context_data(self, **kwargs):
		context = super(UpdateView, self).get_context_data(**kwargs)
		if hasattr(self, 'app'):
			context['app'] = self.app
		if hasattr(self, 'curr'):
			context['curr'] = self.curr
		return context


class ListView( SingleTableView ):
	template_name = "crud/plain/list.html"
	app  = 'res'
	curr = 'datadict'

	def get_context_data(self, **kwargs):
		context = super(ListView, self).get_context_data(**kwargs)
		if hasattr(self, 'app'):
			context['app'] = self.app
		if hasattr(self, 'curr'):
			context['curr'] = self.curr
		return context


class DetailView( generic.DetailView ):
	template_name = 'crud/plain/detail.html'
	app  = 'res'
	curr = 'datadict'

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		if hasattr(self, 'app'):
			context['app'] = self.app
		if hasattr(self, 'curr'):
			context['curr'] = self.curr
		return context


class DeleteView( generic.DeleteView ):
	template_name = 'crud/plain/confirm_delete.html'
	app  = 'res'
	curr = 'datadict'

	def get_context_data(self, **kwargs):
		context = super(DeleteView, self).get_context_data(**kwargs)
		if hasattr(self, 'app'):
			context['app'] = self.app
		if hasattr(self, 'curr'):
			context['curr'] = self.curr
		return context

>>>>>>> 5d2884c8ebc5043fb53d4b828f757362f9d9eae7
