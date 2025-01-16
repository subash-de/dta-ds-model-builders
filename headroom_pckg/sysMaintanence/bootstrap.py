import os
def load_config_campaign_type(file_name):
    """Loads config.yaml file and selects the appropriate section based on the value of campaign type
    Also formats the pipeline names

    Parameters
    ----------
    file_name : str, optional
        name of configuration file that is inside of the project folder, by default "config.yaml"
    file_name: str :
         (Default value = "config.yaml")

    Returns
    -------
    Config
        configuration class


    """
    print(os.path)
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    print(file_path)
load_config_campaign_type("cat_CH_config.yaml")