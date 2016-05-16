#!/usr/bin/env python

from ..embedextractor import EmbedExtractor

import re

class Sohu(EmbedExtractor):

    name = 'Sohu（搜狐)'

    def prepare(self):

        if re.search('my.tv.sohu.com', self.url):
            self.video_info.append(('mysohu',self.url))
        else:
            self.video_info.append(('tvsohu',self.url))


site = Sohu()
