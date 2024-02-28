import abc

from pydantic import BaseModel


class EventAttributes(BaseModel, abc.ABC):

    class Config:
        allow_mutation = False
