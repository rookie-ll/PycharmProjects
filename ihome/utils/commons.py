from werkzeug.routing import BaseConverter


class ReBaseconverter(BaseConverter):
    """"""
    def __init__(self,url_map,regxt):

        super(ReBaseconverter, self).__init__(url_map)

        self.rgxt=regxt