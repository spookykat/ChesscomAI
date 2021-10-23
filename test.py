import boardcom
import browser

driver = browser.Driver()

newBoard = boardcom.Boardcom(driver.all_pieces)
print(newBoard.board)