
import os
from design_config import DesignConfig, D, ___

class Config(DesignConfig):

    """ is D("") """
    PROP_ZERO = ___
    
    """ is 'hello' """
    PROP_ONE = 'Hello'

    """ 'World' if in init_data_dict not PROP_TWO
    As usually init_data_dict is os.environ """
    PROP_TWO = D('World')

    """ 'Hello World!' or 'hello {PROP_TWO}!' for any PROP_TWO """
    PROP_THREE = '{PROP_ONE} {PROP_TWO}!'

def test_base():
    """ Config() == Config(os.environ) """
    config = Config({'PROP_ONE': 'Hi', 'PROP_TWO': 'Alex'})

    assert config.PROP_THREE == "Hello Alex!"

    assert config['PROP_THREE'] == "Hello Alex!"
    assert config['{PROP_THREE}!!'] == "Hello Alex!!!"
    assert config['{PROP_FOUR}'] == "PROP_FOUR"

    assert config('{PROP_ONE} Tom') == "Hello Tom"
    assert config('PROP_FOUR', 'London') == "London"
    assert config('PROP_TWO', 'London') == "Alex"
    assert config('{PROP_ZERO}', 'London') == ""
    assert config('{PROP_FOUR}', 'London') == "PROP_FOUR"

    assert config.path('{PROP_ONE}', 'folder', '{PROP_TWO}2') == os.path.join("Hello","folder","Alex2")
