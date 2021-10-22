from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import piece

driver = webdriver.Firefox()
driver.get("https://www.chess.com/analysis")

time.sleep(5)


board = driver.find_element(By.CLASS_NAME,'board')
all_pieces_raw = board.find_elements(By.CSS_SELECTOR,'*')
all_pieces_classes = []
all_pieces = []

for test in all_pieces_raw:
    class_name = str(test.get_attribute("class"))
    if class_name.startswith("piece"):
        all_pieces_classes.append(class_name)


for test in all_pieces_classes:
    all_pieces.append(piece.Piece(test))
