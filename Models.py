from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Utterance:
    id = int
    content = str

    def __str__(self):
        return f"Utterance: {len(self.content)} -> {self.content}\n"


@dataclass
class Speaker:
    id = int
    name = str
    title = str
    utterances = [] #List[Utterance]

    def __str__(self):
        return f"Speaker: {self.name} - ({self.title})"
    
@dataclass
class Section:
    id = int
    title = str

    def __str__(self):
        return f"Section: {self.title}"

@dataclass
class Document:
    id = int
    title = str
    date = datetime
    sections = [Section]
    speakers = [Speaker]
    def __str__(self):
        sections  = '\n      -'.join([str(sec) for sec in self.sections])
        return f"Document: {self.title} - ({self.date}) - Size Section: {len(self.sections)} -> {sections}\n"


@dataclass
class Company:
    id = int
    ticker = str
    name = str
    documents = [Document] 

    def __str__(self):
        documents = '\n   -'.join([str(doc) for doc in self.documents])
        return f"Company: {self.name} - ({self.ticker}) - Size Documents: {len(self.documents)} -> {documents}"


