from dataclasses import dataclass


@dataclass
class Medicine:
    name: str
    product: str
    presentation: str
    pf: float
    pmc: float

    def __init__(self, name="", product="", presentation="", pf=0.0, pmc=0.0):
        self.name = name
        self.product = product
        self.presentation = presentation
        self.pf = pf
        self.pmc = pmc
