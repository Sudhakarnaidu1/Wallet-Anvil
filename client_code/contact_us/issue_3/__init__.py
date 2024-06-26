from ._anvil_designer import issue_3Template
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server

class issue_3(issue_3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    open_form('contact_us')

  def link_8_click(self, **event_args):
    open_form('Home')

  def link_16_click(self, **event_args):
    open_form('contact_us')

  def button_3_click(self, **event_args):
    open_form('Login')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("contact_us.issue_3.Add_Bank")

  def link_3_click(self, **event_args):
    open_form("contact_us.issue_3.Verify_Phone")

  def link_5_click(self, **event_args):
    open_form('contact_us.issue_3.Verify_Email_Address')

  def link_4_click(self, **event_args):
    open_form("contact_us.issue_3.Wallet_Issue")