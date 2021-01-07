

class DisabledFormMixin():
    def __init__(self):
        for (_, fields) in self.fields.items():
            fields.widget.attrs['disabled'] = True
            fields.widget.attrs['readonly'] = True
