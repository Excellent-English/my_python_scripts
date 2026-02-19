from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Player:

    def __init__(self, Season:int=None, Round:int=None, ID:int=None, Name:str=None, TeamID:int=None, Age:int=None, Country:int=None,
                 Value:int=None, Salary:int=None, Price:int=None, EndOfSale:str=None,
                 Matches:int=None, Goals:int=None, Assists:int=None,
                 Stamina=None, Speed:int=None, Technique:int=None, Passing:int=None,
                 GK:int=None, DEF:int=None, MID:int=None, ATT:int=None):

        self.Season = int(Season) if Season is not None else None
        self.Round = int(Round) if Round is not None else None
        self.ID = int(ID) if ID is not None else None
        self.Name = Name if Name is not None else None
        self.TeamID = TeamID if TeamID is not None else None
        self.Age = Age if Age is not None else None
        self.Country = int(Country) if Country is not None else None
        self.Value = int(Value) if Value is not None else None
        self.Salary = int(Salary) if Salary is not None else None
        self.Price = Price if Price is not None else None
        self.EndOfSale = EndOfSale if EndOfSale is not None else None
        self.Matches = int(Matches) if Matches is not None else None
        self.Goals = int(Goals) if Goals is not None else None
        self.Assists = int(Assists) if Assists is not None else None

        self.Stamina = Stamina if Stamina is not None else None
        self.Speed = Speed if Speed is not None else None
        self.Technique = Technique if Technique is not None else None
        self.Passing = Passing if Passing is not None else None
        self.GK = GK if GK is not None else None
        self.DEF = DEF if DEF is not None else None
        self.MID = MID if MID is not None else None
        self.ATT = ATT if ATT is not None else None

#     def get_first_player_from_transfer_list(self):
#         Sokker.go_to_transfer_list(self)
#
#         xpath_name = '/html/body/main/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/a'
#         wait = WebDriverWait(self.driver, 15)
#         name_el = wait.until(EC.visibility_of_element_located((By.XPATH, xpath_name)))
#
#         self.Name = name_el.text.strip()
#         print(self.Name)
#         return self.Name
#
# if __name__ == "__main__":
#     driver = webdriver.Chrome()
#     first_player = Player(driver=driver)  # ← to jest poprawne
#     first_player.get_first_player_from_transfer_list()
#     driver.quit()
