import browser
import ai
import math
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.chess.com/analysis")
print("Press enter when logged in... ")
input()

board = browser.Chesscom(driver)
Ai1 = ai.Ai()

while True:
    print("Press a button to print board... ")
    input()
    board.pullBoard()
    board.printBoard()
    print("Who to move? (black or white) ")
    color = input()
    print(Ai1.minimax(5,-math.inf, math.inf,color == "white",board.getBoard()))