# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashCircos(Component):
    """A DashCircos component.
Dash Circos is a library used to analyze and interpret
data using a circular layout, based on the popular 
'Circos' graph. This Dash Bio component is a useful tool
for showcasing relationships bewtween data/datasets in a
beautiful way. Please checkout the Dash Bio repository
on github to learn more about this API.

Keyword arguments:
- id (string; optional): The ID of the component to be used in Dash callbacks
- style (dict; optional): The CSS styling of the div wrapping the component
- eventDatum (dict; optional): A Dash prop that returns data on clicking or hovering of the tracks.
Depending on what is specified for prop "selectEvent".
- selectEvent (dict; optional): A dictionary used to choose whether tracks should return
data on click, hover, or both, with the dash prop "eventDatum".
The keys of the dictionary represent the index of the list
specified for "tracks".

Ex:                 
selectEvent={
        "0": "hover",
        "1": "click",
        "2": "both"
    },
- layout (list; required): The overall layout of the Circos graph, provided
as a list of dictionaries.
- config (dict; optional): Configuration of overall layout of the graph.
- size (number; optional): The overall size of the SVG container holding the
graph. Set on initilization and unchangeable thereafter.
- tracks (list; optional): Tracks that specify specific layouts.
For a complete list of tracks and usage, 
please check the docs.

Available events: """
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, style=Component.UNDEFINED, eventDatum=Component.UNDEFINED, selectEvent=Component.UNDEFINED, layout=Component.REQUIRED, config=Component.UNDEFINED, size=Component.UNDEFINED, tracks=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'style', 'eventDatum', 'selectEvent', 'layout', 'config', 'size', 'tracks']
        self._type = 'DashCircos'
        self._namespace = 'dash_bio'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['id', 'style', 'eventDatum', 'selectEvent', 'layout', 'config', 'size', 'tracks']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['layout']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashCircos, self).__init__(**args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('DashCircos(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'DashCircos(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')