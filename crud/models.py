from django.core.urlresolvers import reverse

class CRUDModelMixin( object ):

    def __init__( self, *args, **kwargs ):
        super( CRUDModelMixin, self ).__init__( *args, **kwargs )
        self._crud_name = self.__class__.__name__.lower()

    def get_absolute_url( self ):
        return reverse('%s-detail' % self._crud_name, kwargs={'pk': self.pk } ) 

    def get_create_url( self ):
        return reverse('%s-create' % self._crud_name )

    def get_delete_url( self ):
        return reverse('%s-delete' % self._crud_name, kwargs={'pk': self.pk } ) 

    def get_list_url( self ):
        return reverse('%s-list' % self._crud_name )

    def get_update_url( self ):
        return reverse('%s-update' % self._crud_name, kwargs={'pk': self.pk } )
