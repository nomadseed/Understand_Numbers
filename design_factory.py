"""

All the different experiment designs are stored here.

"""
import logging

class DesignFactory():
    def __init__(self, design_name, **configs):
        self.raw_configs = configs
        self.design_configs = {'design_name': str(design_name).lower()}

        # init a logger for warnings
        self.logger = logging.getLogger('logger')

        self.parse_configs()
    
    def parse_configs(self):
        # parse arbitory config settings and save them into config dict
        for cfg_key, value in self.raw_configs.items():
            self.design_configs[cfg_key] = value

if __name__ == '__main__':
    df = DesignFactory(design_name='1', confidence = 0.2, iou_thresh = 0.5)
    print('end of debug')