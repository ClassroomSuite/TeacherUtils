import ipywidgets as widgets
from IPython import display


class Widgets:
    def __init__(self):
        self.wg = dict()
        self.create()

    def create(self):
        default_layout = widgets.Layout(width='500px')
        self.wg['url'] = widgets.Text(
            value='',
            description='URL: ',
            layout=default_layout
        )
        self.wg['update_url'] = widgets.Button(description='Update')
        self.wg['request_status'] = widgets.Valid(layout=default_layout)
        self.wg['search_filter'] = widgets.Text(
            value='',
            placeholder='Must contain',
            description='Filter',
            layout=default_layout
        )
        self.wg['dropdown'] = widgets.Dropdown(
            description='Select',
            layout=default_layout
        )
        self.wg['num_results'] = widgets.Label()

        self.wg['update_interval'] = widgets.IntSlider(
            value=5,
            min=1,
            max=60,
            step=1,
            layout=default_layout,
            continuous_update=True
        )
        self.wg['interrupt_button'] = widgets.Button(description='Interrupt')
        self.wg['resume_button'] = widgets.Button(description='Resume')

    def add_image(self, index, image):
        self.wg.setdefault('images', list())
        img_wg = widgets.Image(
            value=image,
            format='png',
            width=300,
            height=400
        )
        self.wg['images'].append(img_wg)
        display.display(img_wg)
        # display.display(widgets.HBox((img_wg)))

    def _display(self, out: widgets.Output):

        @out.capture()
        def _display():
            display.display(widgets.HBox((self.wg['url'], self.wg['update_url'], self.wg['request_status'])))
            display.display(self.wg['search_filter'])
            display.display(widgets.HBox((self.wg['dropdown'], self.wg['num_results'])))
            display.display(widgets.HBox((widgets.Label('Update interval (seconds)'), self.wg['update_interval'])))
            display.display(widgets.HBox((self.wg['interrupt_button'], self.wg['resume_button'])))

        _display()

    def __getitem__(self, item):
        return self.wg[item]

    def update_dropdown(self, choices):
        self.wg['dropdown'].options = ['All'] + choices
        self.wg['num_results'].value = f'({len(choices)} results)'

    def update_image(self, index, image):
        try:
            if 'images' in self.wg:
                self.wg['images'][index].value = image
        except:
            self.add_image(index, image)
