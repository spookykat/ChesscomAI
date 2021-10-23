from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import piececom
class Driver:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.chess.com/analysis")

        time.sleep(5)
        self.GetBoard()

    def GetBoard(self):
        board = self.driver.find_element(By.CLASS_NAME,'board')

        all_pieces_raw = board.find_elements(By.CSS_SELECTOR,'*')
        all_pieces_classes = []
        self.all_pieces = []

        for test in all_pieces_raw:
            class_name = str(test.get_attribute("class"))
            if class_name.startswith("piece"):
                all_pieces_classes.append(class_name)
        
        for test in all_pieces_classes:
            self.all_pieces.append(piececom.PieceCom(test))