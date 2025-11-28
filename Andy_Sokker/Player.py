class Player:

    def __init__(self, ID:int=None, Name:str=None, TeamID:int=None, Age:int=None, Country:int=None,
                 Value:int=None, Salary:int=None, Price:int=None, EndOfSale:str=None,
                 Stamina=None, Speed:int=None, Technique:int=None, Passing:int=None,
                 GK:int=None, DEF:int=None, MID:int=None, ATT:int=None):

        self.ID = int(ID) if ID is not None else None
        self.Name = Name if Name is not None else None
        self.TeamID = TeamID if TeamID is not None else None
        self.Age = Age if Age is not None else None
        self.Country = int(Country) if Country is not None else None
        self.Value = int(Value) if Value is not None else None
        self.Salary = int(Salary) if Salary is not None else None
        self.Price = Price if Price is not None else None
        self.EndOfSale = EndOfSale if EndOfSale is not None else None

        self.Stamina = Stamina if Stamina is not None else None
        self.Speed = Speed if Speed is not None else None
        self.Technique = Technique if Technique is not None else None
        self.Passing = Passing if Passing is not None else None
        self.GK = GK if GK is not None else None
        self.DEF = DEF if DEF is not None else None
        self.MID = MID if MID is not None else None
        self.ATT = ATT if ATT is not None else None


class Empty_player:
    def __init__(self):
        pass