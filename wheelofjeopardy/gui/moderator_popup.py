'''
This is an internal class called when "submit answer" button is clicked.

@author = Miranda Link, mirandanlink@gmail.com
'''

from os import sys
from PyQt4.QtGui import *
from wheelofjeopardy.gui.pyqt.ui_moderator_popup import Ui_ModeratorPopup
from wheelofjeopardy.events import Events


class ModeratorPopup(QDialog, Ui_ModeratorPopup):
  def __init__(self, events, parent=None):
    super(ModeratorPopup, self).__init__(parent)
    self.setupUi(self)
    self.events = events
    
    # initialize variables
    #
    #self.correctAnswer.setText(correct_answer)
    #self.playerAnswer.setText(player_answer)

  # button clicks
  #
  #@pyqtSignature("")
  def _on_playerCorrectRadio_clicked(self):
    self.events.broadcast('gui.correct_answer_received')
    self.events.broadcast('moderator.update_score')

  #@pyqtSignature("")
  def _on_playerIncorrectRadio_clicked(self):
    self.events.broadcast('gui.incorrect_answer_received')


#Display GUI.
if __name__ == '__main__':
  application = QApplication(sys.argv)
  application.setApplicationName("Moderator Popup")
  events = Events()
  gui = ModeratorPopup(events)
  gui.show()
  gui.raise_()
  application.exec_()

# subscriptions
#
events.subscribe('gui.answer_received', ModeratorPopup)
