
class Text(object):
    def __init__(self, *elements, **context):
        self.elements = elements
        self.context = context

        self.defaults = {
            'format': None,
        }

        self.index = {}

    def render(self, format):
        pass

    def __str__(self):
        return self.render(self.defaults['format'])

    def __unicode__(self):
        return unicode(self.__str__())
