#! /usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Dexter Scott Belmont"
__copyright__ = "Copyright 2021, Boxel LLC"
__credits__ = [ "Dexter Scott Belmont", "Benny Carbajal" ]
__tags__ = [ "Boxel", "Shotgun", "Frame.io" ]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Dexter Scott Belmont"
__email__ = "dexter@boxelstudio.com"
__status__ = "beta"


from frameioclient import FrameioClient
#from dotenv import load_dotenv
import os
import sys
#import csv
import getpass
import shotgun_api3


class ShotIO( object ) :

 """ShotIO Class definition"""

 def __init__( self ) :
  """Auto executed upon instantiation"""
  super( ShotIO, self ).__init__()
  #load_dotenv()
  self.location = os.path.dirname( os.path.realpath( __file__ ) )
  self.__load_env()

  if self.__fio_token is None :
   print( 'I was unable to get a Frame.io Token from your .env file or your environment variables' )
   thing = input( 'Please paste it here or edit the .env file located at' )
   self.__write_env( 'FRAME_IO_TOKEN', thing )
   self.__load_env()
  
  self.fio = FrameioClient( self.__fio_token )
  self.sg = shotgun_api3.Shotgun( self.sg_url, login=self.sg_user, password=self.__sg_pass )
 
 def __write_env( self, key, value ) :
  with open( self.location + '\\.env', 'a' ) as f :
   f.write( key + '=' + value + '\n')

 def __load_env( self ) :
  try :
   with open( self.location + '\\.env', 'r' ) as env :
    vars_dict = dict(
     tuple( line.replace( "\n", '' ).split( '=' ) )
     for line in env.readlines() if not line.startswith( '#' )
    )
   os.environ.update( vars_dict )
   self.__fio_token = os.environ.get( 'FRAME_IO_TOKEN' ) or os.environ.get( 'FIO_TOKEN' )
   self.sg_url = os.environ.get( 'SG_URL' )
   self.sg_user = os.environ.get( 'SG_USER' )
   self.__sg_pass = os.environ.get( 'SG_PASS' )
  except FileNotFoundError :
   self.__survey()
  except Exception as e:
   print( 'Error related to the .env file' )
   raise e # Could not read env file

 def __input( self, question ) :
  #error_stack = 0
  while True:
   try :
    response = input( question )
    if ( response ) :
     return response
   except ValueError:
    print( "Sorry, I didn't understand that." ) # User entered something unintelligible to the CLI 
    continue

 def __getpass( self, question ) :
 #error_stack = 0
  while True:
   try :
    response = getpass.getpass( prompt=question )
    if ( response ) :
     return response
   except ValueError:
    print( "Sorry, I didn't understand that, please try again." ) # User entered something unintelligible to the CLI 
    continue

 def __survey( self ) :
  print( "I was unable to locate the .env file at " + self.location + "\\.env" )
  if ( ( input( "Would you like to create a .env file now? [Y] / [n]" ) or 'y').lower() == 'y' ) :
   fio_token = self.__input( "Please enter your Frame.io token: " )
   self.__write_env( 'FRAME_IO_TOKEN', fio_token )
   sg_url = self.__input( "Please enter your Shotgun url (e.g. https://subdomain.shotgunstudio.com): " )
   self.__write_env( 'SG_URL', sg_url )
   sg_user = self.__input( "Please enter your Shotgun username: " )
   self.__write_env( 'SG_USER', sg_user )
   sg_pass = self.__getpass( "Please enter your Shotgun password (hidden): " )
   self.__write_env( 'SG_PASS', sg_pass )
   self.__load_env()
   print( "Entered all parameters " )
  else :
   sys.exit( "Exiting program, missing required environment variables." )

 def getTeamsFromAccount( self, client):
  """
  Builds a list of teams for the account.
  """
  acct = client.get_me()
  acct_id = acct['account_id']
  return client.get_teams(acct_id)
 
 def getProjectsFromTeam( self, client, team):
  """Returns a list of projects for a team."""
  projects_in_team = []
  data = client.get_projects(team.get('id'))
  team_name = team.get('name')
  for proj in data:
   proj['project_name'] = proj.get('name')
   proj['team_name'] = team_name
   projects_in_team.append(proj)
  return projects_in_team
 
 def getProjectsFromAccount( self, client):
  """Gets projects from all teams in the account."""
  projects_in_account = []
  teams = self.getTeamsFromAccount(client)
  for team in teams:
   projects_in_team = ( self.getProjectsFromTeam( client, team ) )
   projects_in_account.extend(projects_in_team)
  return projects_in_account



 def test( self ) :
  """Testing method"""
  me = self.fio.get_me()
  print( me[ 'id' ] )
  print( self.sg._connection )
  print( self.__fio_token )
  print( self.sg_url )
  print( self.sg_user )
  print( self.__sg_pass )
  print( "Location: " + self.location )
