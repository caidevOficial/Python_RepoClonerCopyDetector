import datetime
from modules.models.formatter import Formatter as FMT
from modules.models.config_manager import ConfigManager as CoMa
from modules.models.clone_messenger import CloneMessenger as CM
from modules import c_manager, r_manager


if __name__ == '__main__':
    # ?######### Start Basic Configuration ##########
    FILE_CONFIG_NAME: str = './modules/configs.json'
    config_manager = CoMa(FILE_CONFIG_NAME)
    start_time = datetime.datetime.now()
    # ?######### End Basic Configuration ##########
    
    # ?#########? Start Timer Config ##########
    message_manager = CM()
    time_manager = FMT()
    time_manager.crude_time = start_time
    # ?#########? End Timer Config ##########
    
    r_manager(config_manager)
    # c_manager(config_manager)

    message_manager.message = f"Elapsed Time: {time_manager.formatted_time_str}"
    message_manager.print_success_message()