"""
Base Indicator Class for deriving your own indicators
to use within an ``analysis_engine.algo.BaseAlgo``
"""

import uuid
# import analysis_engine.consts as ae_consts
# import analysis_engine.utils as ae_utils
import spylunking.log.setup_logging as log_utils

log = log_utils.build_colorized_logger(name=__name__)


class BaseIndicator:
    """BaseIndicator"""

    def __init__(
            self,
            config_dict,
            path_to_module=None,
            name=None,
            verbose=False):
        """__init__

        Create the object

        :param config_dict:
        :param name:
        :param path_to_module: work in progress -
            this will allow loading indicators from
            outside the repo like the derived algorithm
            classes
            :param verbose:
        """
        self.name = name
        self.config = config_dict
        self.path_to_module = path_to_module
        self.verbose = verbose

        if not self.name:
            self.name = 'ind_{}'.format(
                str(uuid.uuid4()).replace('-', ''))

        if not self.config:
            raise Exception(
                'please provide a config_dict for loading '
                'the buy and sell rules for this indicator')

    # end of __init__

    def get_path_to_module(
            self):
        """get_path_to_module"""
        return self.path_to_module
    # end of get_path_to_module

    def get_name(
            self):
        """get_name"""
        return self.name
    # end of get_name

    def process(
            self,
            algo_id,
            ticker,
            dataset):
        """process

        Derive custom indicator processing to determine buy and sell
        conditions before placing orders. Just implement your own
        ``process`` method.

        :param algo_id: string - algo identifier label for debugging datasets
            during specific dates
        :param ticker: string - ticker
        :param dataset: ``pd.DataFrame`` to process
        """
        log.info(
            '{} process - start')
        log.info(
            '{} process - end')
    # end of process

# end of BaseIndicator
