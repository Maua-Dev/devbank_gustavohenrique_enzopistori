from dotenv import load_dotenv
from enum import Enum
import os

from .errors.environment_errors import EnvironmentNotFound

from .repo.item_repository_interface import IItemRepository
from .repo.user_repository_interface import IUserRepository

class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    PROD = "PROD"
    TEST = "TEST"


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.TEST.value

    def load_envs(self):
        if "STAGE" not in os.environ or os.environ["STAGE"] == STAGE.DOTENV.value:
            self._configure_local()

        self.stage = STAGE[os.environ.get("STAGE")]

    @staticmethod
    def get_item_repo() -> IItemRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from .repo.item_repository_mock import ItemRepositoryMock
            return ItemRepositoryMock
        # use "elif" conditional to add other stages
        else:
            raise EnvironmentNotFound("STAGE")  

    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage})

        """
        envs = Environments()
        envs.load_envs()
        return envs
    
    @staticmethod
    def get_tran_repo() -> IItemRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from .repo.transaction_repository_mock import TransacRepositoriMock
            return TransacRepositoriMock
        else:
            raise EnvironmentNotFound("STAGE")

    @staticmethod
    def get_user_repo() -> IUserRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from .repo.user_repository_mock import userRepositoryMock
            return userRepositoryMock
        else:
            raise EnvironmentNotFound("STAGE")
        
    def __repr__(self):
        return self.__dict__
    

class Environments2:
    """
    Handles environment-specific configurations for user setups.
    """

    def __init__(self):
        self.configure_local()

    def configure_local(self):
        """
        Loads environment variables from a.env file or sets default values.
        """
        load_dotenv()
        self.user_repo_path = os.getenv('USER_REPO_PATH', 'path/to/default/user/repository')

    def get_user_repo() -> IUserRepository:
        """
        Returns the path to the user repository based on the environment.
        """
        from .repo.user_repository_mock import userRepositoryMock
        return userRepositoryMock

    def get_envs() -> "Environments2":
        """
        Returns the Environments2 object configured for the current environment.
        """
        envs = Environments2()
        envs.configure_local()
        return envs

    def __repr__(self):
        return f"user_repo_path: {self.user_repo_path}"