from a2ml.api.base_a2ml import BaseA2ML
from a2ml.api.utils.show_result import show_result

class A2MLDataset(BaseA2ML):
    """Contains the dataset CRUD operations that interact with provider."""
    def __init__(self, ctx, provider):
        """Initializes a new a2ml dataset.

        Args:
            context (object): An instance of the a2ml Context.
            provider (str): The automl provider/s you wish to run. For example 'auger,azure,google'.
        
        Returns:
            A2MLDataset object

        Examples:
            .. code-block:: python

                ctx = Context()
                dataset = A2MLDataset(ctx, 'auger, azure')
        """
        super(A2MLDataset, self).__init__()
        self.ctx = ctx
        self.runner = self.build_runner(ctx, provider, 'dataset')

    @show_result
    def list(self):
        """List all of the DataSets for the Project specified in the .yaml.

        Note:
            You will need to user the `iter <https://www.programiz.com/python-programming/methods/built-in/iter>`_ function to access the dataset elements.
        
        Returns:
            Results for each provider. ::

                {
                    'auger': {
                        'result': True,
                        'data': {
                            'datasets': <object> 
                        }
                    }
                }

        Examples:
            .. code-block:: python

                ctx = Context()
                dataset_list = A2MLDataset(ctx, 'auger, azure').list()
                for provider in ['auger', 'azure']
                    if dataset_list[provider].result is True:
                        for dataset in iter(dataset_list[provider].data.datasets):
                            ctx.log(dataset.get('name'))
                    else:
                        ctx.log('error %s' % dataset_list[provider].data)
        """
        return self.runner.execute('list')

    @show_result
    def create(self, source = None):
        """Create a new DataSet for the Project specified in the .yaml.

        Args:
            source(str): path to local or link to remote file.

        Returns:
            Results for each provider. ::

                    {
                        'auger': {
                            'result': True,
                            'data': {
                                'created': 'dataset.csv' 
                            }
                        }
                    }

        Examples:
            .. code-block:: python

                ctx = Context()
                dataset = DataSet(ctx, 'auger, azure').create('../dataset.csv')
        """
        return self.runner.execute('create', source)

    @show_result
    def delete(self, name = None):
        """
        Deletes a DataSet for the Project specified in the .yaml.

        Args:
            name(str): name of dataset.

        Returns:
            Results for each provider. ::

                    {
                        'auger': {
                            'result': True,
                            'data': {
                                'deleted': 'dataset.csv' 
                            }
                        }
                    }

        Examples:
            .. code-block:: python

                ctx = Context()
                DataSet(ctx, 'auger, azure').delete(dataset_name)
                ctx.log('Deleted dataset %s' % dataset_name)
        """
        return self.runner.execute('delete', name)

    @show_result

    def select(self, name = None):
        """
        Sets a DataSet name in the context.

        Args:
            name(str): name of dataset.

        Returns:
            Results for each provider. ::

                {
                    'auger': {
                        'result': True,
                        'data': {
                            'selected': 'fortunetest'
                        }
                    }
                }

        Examples:
            .. code-block:: python

            ctx = Context()
            DataSet(ctx, 'auger, azure').select(dataset_name)
        """
        return self.runner.execute('select', name)

